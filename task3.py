import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    # Define the character sets to use for password generation
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + special_characters

    # Ensure the password contains at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Join the list into a string and return
    return ''.join(password)

def on_generate():
    try:
        length = int(entry_length.get())
        if length < 4:
            messagebox.showerror("Error", "Password length should be at least 4.")
            return
        password = generate_password(length)
        label_result.config(text=f"Generated Password: {password}")
        messagebox.showinfo("Success", "Password generated successfully!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

# Create the main window
root = tk.Tk()
root.title(" Password Generator")
root.configure(bg="#f0f0f0")

# Create input field for password length
label_length = tk.Label(root, text="Enter desired password length:", bg="#f0f0f0", font=("Arial", 12))
label_length.pack(pady=10)

entry_length = tk.Entry(root, font=("Arial", 12), width=10)
entry_length.pack(pady=5)

# Create generate button
button_generate = tk.Button(root, text="Generate Password", command=on_generate, bg="#4CAF50", fg="white", font=("Arial", 12))
button_generate.pack(pady=20)

# Create result label
label_result = tk.Label(root, text="Generated Password: ", bg="#f0f0f0", font=("Arial", 12))
label_result.pack(pady=10)

# Start the GUI event loop
root.mainloop()