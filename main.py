import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import string

# Global variables for widgets
root = None
entry = None
result_label = None
copy_button = None

def get_user_input():
    global root, entry
    user_input = simpledialog.askstring("Password Generator", "Please enter length of password (int)", parent=root)
    return user_input

def generate_password(length):
    u = list(string.ascii_uppercase)
    s = list(string.ascii_lowercase)
    special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', ':', '<', '.', '>', '/', '?']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    password = random.choice(s) + random.choice(u) + random.choice(numbers) + random.choice(special_characters)
    while length - len(password) > 0:
        password += random.choice(u + s + special_characters + numbers)
    return password

def show_output():
    global root, result_label, copy_button

    user_input = entry.get()

    try:
        length = int(user_input)
        if length > 3:
            password = generate_password(length)
            result_label.config(text=f"Generated Password: {password}")
            copy_button.pack(pady=10)  # Show the copy button after generating the password
        else:
            messagebox.showinfo("Error", "Please provide an integer greater than 3")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer")

def on_copy_button_click():
    global result_label

    password = result_label.cget("text").replace("Generated Password: ", "")
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard")
    else:
        messagebox.showwarning("Warning", "No password to copy")

def main():
    global root, entry, result_label, copy_button

    # Create the main application window
    root = tk.Tk()
    root.title("Password Generator")

    # Create and place the widgets
    tk.Label(root, text="Enter length of password:").pack(pady=10)
    entry = tk.Entry(root)
    entry.pack(pady=5)

    generate_button = tk.Button(root, text="Generate Password", command=show_output)
    generate_button.pack(pady=10)

    result_label = tk.Label(root, text="", font=("Helvetica", 12), wraplength=400)
    result_label.pack(pady=10)

    copy_button = tk.Button(root, text="Copy to Clipboard", command=on_copy_button_click)

    root.mainloop()

if __name__ == "__main__":
    main()
