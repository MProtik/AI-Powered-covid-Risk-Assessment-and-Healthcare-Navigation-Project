import tkinter as tk
from tkinter import ttk

class ScrollableForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scrollable Form")
        self.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        # Create a Canvas widget
        self.canvas = tk.Canvas(self)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add a Scrollbar to the Canvas
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=scrollbar.set)

        # Create a Frame inside the Canvas
        self.frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        # Populate the Frame with sample entry widgets
        for i in range(20):
            label = ttk.Label(self.frame, text=f"Field {i+1}")
            label.grid(row=i, column=0, padx=5, pady=5)
            entry = ttk.Entry(self.frame)
            entry.grid(row=i, column=1, padx=5, pady=5)

        # Update the scroll region
        self.frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        # Add a button to retrieve form data
        btn_submit = ttk.Button(self.frame, text="Submit", command=self.submit_form)
        btn_submit.grid(row=21, column=0, columnspan=2, pady=10)

    def submit_form(self):
        data = []
        for widget in self.frame.winfo_children():
            if isinstance(widget, ttk.Entry):
                data.append(widget.get())
        print("Form Data:", data)

if __name__ == "__main__":
    app = ScrollableForm()
    app.mainloop()
