import tkinter as tk
from tkinter import messagebox
import string

def check_password_strength():
    password = password_entry.get()

    upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
    lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
    specialchar = any([1 if c in string.punctuation else 0 for c in password])
    digits = any([1 if c in string.digits else 0 for c in password])

    characters = [upper_case, lower_case, specialchar, digits]

    length = len(password)

    score = 0

    with open('common_password.txt', 'r') as f:
        common = f.read().splitlines()

    if password in common:
        messagebox.showwarning("Weak Password", "Password is common! Please choose a different one.")
        return

    if length >= 8:
        score += 1

    if length > 12:
        score += 1

    if length > 16:
        score += 1

    if length > 18:
        score += 1

    if length > 20:
        score += 1

    if sum(characters) > 1:
        score += 1
    if sum(characters) > 2:
        score += 1
    if sum(characters) > 3:
        score += 1
    if sum(characters) > 4:
        score += 1

    if score < 4:
        messagebox.showwarning("Weak Password", f"Password is quite weak!! Strengthen it. Score: {score}/10")
    elif score == 4:
        messagebox.showinfo("Moderate Password", f"Password is ok but needs modifications. Score: {score}/10")
    elif score > 4 and score < 6:
        messagebox.showinfo("Strong Password", f"Password is great. Score: {score}/10")
    elif score >= 6:
        messagebox.showinfo("Excellent Password", f"Excellent password. Score: {score}/10")


# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

password_label = tk.Label(frame, text="Enter Password:")
password_label.grid(row=0, column=0, sticky="w")

password_entry = tk.Entry(frame, show="*")
password_entry.grid(row=0, column=1, padx=5, pady=5)

check_button = tk.Button(frame, text="Check", command=check_password_strength)
check_button.grid(row=1, columnspan=2, pady=10)

root.mainloop()
