import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tkinter Message Box Example")
root.geometry("300x200")

def show_info():
    messagebox.showinfo("Information", "This is an information message.")

def show_warning():
    messagebox.showwarning("Warning", "This is a warning message.")

def show_error():
    messagebox.showerror("Error", "This is an error message.")

def ask_question():
    response = messagebox.askquestion("Question", "Do you like Tkinter?")
    print("Response:", response)

def ask_ok_cancel():
    response = messagebox.askokcancel("Confirmation", "Do you want to proceed?")
    print("Response:", response)

def ask_yes_no():
    response = messagebox.askyesno("Confirmation", "Do you like Python?")
    print("Response:", response)

btn_info = tk.Button(root, text="Show Info", command=show_info)
btn_info.pack(pady=10)

btn_warning = tk.Button(root, text="Show Warning", command=show_warning)
btn_warning.pack(pady=10)

btn_error = tk.Button(root, text="Show Error", command=show_error)
btn_error.pack(pady=10)

btn_question = tk.Button(root, text="Ask Question", command=ask_question)
btn_question.pack(pady=10)

btn_ok_cancel = tk.Button(root, text="Ask Ok/Cancel", command=ask_ok_cancel)
btn_ok_cancel.pack(pady=10)

btn_yes_no = tk.Button(root, text="Ask Yes/No", command=ask_yes_no)
btn_yes_no.pack(pady=10)

root.mainloop()
