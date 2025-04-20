import tkinter as tk
from tkinter import messagebox

# Denominations (you can customize this)
DENOMINATIONS = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

def calculate_denominations():
    try:
        amount = int(entry_amount.get())
        if amount < 0:
            raise ValueError

        result_text.delete('1.0', tk.END)  # Clear previous results

        remaining = amount
        result_text.insert(tk.END, f"Amount: ₹{amount}\n\nBreakdown:\n")

        for denom in DENOMINATIONS:
            count = remaining // denom
            if count:
                result_text.insert(tk.END, f"{denom} x {count} = ₹{denom * count}\n")
            remaining %= denom

        if remaining == 0:
            result_text.insert(tk.END, "\nCalculation complete!")
        else:
            result_text.insert(tk.END, f"\nRemaining: ₹{remaining}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive integer.")

# GUI Setup
root = tk.Tk()
root.title("Denomination Calculator")
root.geometry("400x400")
root.config(padx=20, pady=20)

# Title Label
title_label = tk.Label(root, text="Denomination Calculator", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Amount Entry
entry_label = tk.Label(root, text="Enter amount (₹):", font=("Helvetica", 12))
entry_label.pack()

entry_amount = tk.Entry(root, font=("Helvetica", 12))
entry_amount.pack(pady=5)

# Calculate Button
btn_calculate = tk.Button(root, text="Calculate", font=("Helvetica", 12), command=calculate_denominations)
btn_calculate.pack(pady=10)

# Result Display
result_text = tk.Text(root, height=15, font=("Courier", 12), bg="#f7f7f7")
result_text.pack()

# Run the app
root.mainloop()
