import tkinter as tk
from tkinter import messagebox, font

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                raise ValueError("Cannot divide by zero.")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation.")

        label_result.config(text=f"Result: {result}")
        history_list.insert(tk.END, f"{num1} {operation} {num2} = {result}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def clear():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    label_result.config(text="Result: ")
    history_list.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Colorful Calculator")
root.configure(bg="#f0f0f0")

# Create input fields
label_num1 = tk.Label(root, text="Enter first number:", bg="#f0f0f0", font=("Arial", 12))
label_num1.pack(pady=5)

entry_num1 = tk.Entry(root, font=("Arial", 12), width=15)
entry_num1.pack(pady=5)

label_num2 = tk.Label(root, text="Enter second number:", bg="#f0f0f0", font=("Arial", 12))
label_num2.pack(pady=5)

entry_num2 = tk.Entry(root, font=("Arial", 12), width=15)
entry_num2.pack(pady=5)

# Create operation selection
operation_var = tk.StringVar(value="Add")
operations = ["Add", "Subtract", "Multiply", "Divide"]
for operation in operations:
    radio = tk.Radiobutton(root, text=operation, variable=operation_var, value=operation, bg="#f0f0f0", font=("Arial", 12))
    radio.pack(pady=2)

# Create calculate button
button_calculate = tk.Button(root, text="Calculate", command=calculate, bg="#4CAF50", fg="white", font=("Arial", 12))
button_calculate.pack(pady=10)

# Create clear button
button_clear = tk.Button(root, text="Clear", command=clear, bg="#f44336", fg="white", font=("Arial", 12))
button_clear.pack(pady=5)

# Create result label
label_result = tk.Label(root, text="Result: ", bg="#f0f0f0", font=("Arial", 12))
label_result.pack(pady=10)

# Create history listbox
label_history = tk.Label(root, text="History:", bg="#f0f0f0", font=("Arial", 12))
label_history.pack(pady=5)

history_list = tk.Listbox(root, width=50, height=10, font=("Arial", 10))
history_list.pack(pady=5)

# Start the GUI event loop
root.mainloop()