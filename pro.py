import tkinter as tk
from tkinter import messagebox

def check_strength():
    password = entry.get()
    length = len(password)
    
    if length == 0:
        result_label.config(text="Please enter a password", fg="red")
    elif length < 6:
        result_label.config(text="Password Strength: Weak", fg="red")
    elif 6 <= length <= 10:
        result_label.config(text="Password Strength: Medium", fg="orange")
    else:
        result_label.config(text="Password Strength: Strong", fg="green")

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x200")
root.config(bg="#f0f0f0")

# Create a label and entry for the password
label = tk.Label(root, text="Enter your password:", font=("Arial", 12), bg="#f0f0f0")
label.pack(pady=10)

entry = tk.Entry(root, show="*", font=("Arial", 12), width=25)
entry.pack()

# Create a button to check password strength
check_button = tk.Button(root, text="Check Strength", command=check_strength, font=("Arial", 12))
check_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f0f0f0")
result_label.pack(pady=5)

# Run the application
root.mainloop()
