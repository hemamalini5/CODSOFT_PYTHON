import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "You lose!"

# Function to play the game
def play_game(user_choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(user_choice, computer_choice)

    # Update the result label
    label_result.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\nResult: {result}")

    # Update scores
    if result == "You win!":
        global user_score
        user_score += 1
    elif result == "You lose!":
        global computer_score
        computer_score += 1

    # Update score labels
    label_user_score.config(text=f"Your Score: {user_score}")
    label_computer_score.config(text=f"Computer's Score: {computer_score}")

# Function to ask if the user wants to play again
def play_again():
    if messagebox.askyesno("Play Again", "Do you want to play another round?"):
        label_result.config(text="")
    else:
        root.quit()

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.configure(bg="#f0f0f0")

# Initialize scores
user_score = 0
computer_score = 0

# Create title label
label_title = tk.Label(root, text="Rock-Paper-Scissors", bg="#f0f0f0", font=("Arial", 24, "bold"))
label_title.pack(pady=20)

# Create buttons for user choices
button_rock = tk.Button(root, text="Rock", command=lambda: [play_game("Rock"), play_again()], bg="#FF5733", fg="white", font=("Arial", 14))
button_rock.pack(pady=10)

button_paper = tk.Button(root, text="Paper", command=lambda: [play_game("Paper"), play_again()], bg="#33FF57", fg="white", font=("Arial", 14))
button_paper.pack(pady=10)

button_scissors = tk.Button(root, text="Scissors", command=lambda: [play_game("Scissors"), play_again()], bg="#3357FF", fg="white", font=("Arial", 14))
button_scissors.pack(pady=10)

# Create result label
label_result = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 16))
label_result.pack(pady=20)

# Create score labels
label_user_score = tk.Label(root, text="Your Score: 0", bg="#f0f0f0", font=("Arial", 14))
label_user_score.pack(pady=5)

label_computer_score = tk.Label(root, text="Computer's Score: 0", bg="#f0f0f0", font=("Arial", 14))
label_computer_score.pack(pady=5)

# Start the GUI event loop
root.mainloop()