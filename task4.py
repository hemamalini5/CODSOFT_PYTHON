import tkinter as tk
import random

# Function to calculate result
def play_game(user_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    
    result = ""
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        result = "You win!"
        update_score("user")
    else:
        result = "You lose!"
        update_score("computer")
    
    display_result(user_choice, computer_choice, result)

# Function to display result and choices
def display_result(user_choice, computer_choice, result):
    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")

# Function to update scores
def update_score(winner):
    global user_score, computer_score
    if winner == "user":
        user_score += 1
    else:
        computer_score += 1
    
    score_label.config(text=f"Score: You {user_score} - Computer {computer_score}")

# Function to restart the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text=f"Score: You {user_score} - Computer {computer_score}")
    result_label.config(text="")

# Initialize scores
user_score = 0
computer_score = 0

# Set up GUI
root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Score Label
score_label = tk.Label(root, text=f"Score: You {user_score} - Computer {computer_score}", font=("Helvetica", 14))
score_label.pack()

# Result Label
result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack()

# Buttons for user choices
rock_button = tk.Button(root, text="Rock", command=lambda: play_game('rock'))
rock_button.pack(side=tk.CENTER)

paper_button = tk.Button(root, text="Paper", command=lambda: play_game('paper'))
paper_button.pack(side=tk.CENTER)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game('scissors'))
scissors_button.pack(side=tk.CENTER)

# Reset Button
reset_button = tk.Button(root, text="Reset Scores", command=reset_game)
reset_button.pack()

# Start the GUI event loop
root.mainloop()