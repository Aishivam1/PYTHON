import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Expense Tracker GUI")
root.geometry("400x500")

expenses = []

def add_expense():
    category = category_entry.get()
    try:
        amount = float(amount_entry.get())
        if category and amount > 0:
            expenses.append({"category": category, "amount": amount})
            messagebox.showinfo("Success", "Expense added!")
            category_entry.delete(0, tk.END)
            amount_entry.delete(0, tk.END)
            update_display()
        else:
            messagebox.showerror("Error", "Enter valid data!")
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number!")

def update_display():
    display.config(state=tk.NORMAL)
    display.delete(1.0, tk.END)
    if expenses:
        for i, exp in enumerate(expenses, 1):
            display.insert(tk.END, f"{i}. {exp['category']}: ${exp['amount']}\n")
        total = sum(exp['amount'] for exp in expenses)
        display.insert(tk.END, f"\nTotal: ${total:.2f}")
    display.config(state=tk.DISABLED)

def delete_expense():
    try:
        index = int(index_entry.get()) - 1
        if 0 <= index < len(expenses):
            del expenses[index]
            messagebox.showinfo("Success", "Expense deleted!")
            index_entry.delete(0, tk.END)
            update_display()
        else:
            messagebox.showerror("Error", "Invalid index!")
    except ValueError:
        messagebox.showerror("Error", "Enter a number!")

tk.Label(root, text="Category:", font=("Arial", 12)).pack(pady=5)
category_entry = tk.Entry(root, width=30)
category_entry.pack()

tk.Label(root, text="Amount:", font=("Arial", 12)).pack(pady=5)
amount_entry = tk.Entry(root, width=30)
amount_entry.pack()

tk.Button(root, text="Add Expense", command=add_expense, bg='green', fg='white').pack(pady=10)

display = tk.Text(root, height=12, width=45, state=tk.DISABLED)
display.pack(pady=10)

tk.Label(root, text="Delete by index:", font=("Arial", 10)).pack()
index_entry = tk.Entry(root, width=10)
index_entry.pack()

tk.Button(root, text="Delete Expense", command=delete_expense, bg='red', fg='white').pack(pady=5)

root.mainloop()
