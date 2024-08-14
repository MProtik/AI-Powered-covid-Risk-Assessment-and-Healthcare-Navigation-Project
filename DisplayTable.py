import tkinter as tk
from tkinter import ttk

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Table of Information")
        self.root.geometry("600x400")

        # Sample data
        self.data = [
            ("John Doe", "1234567890", "john@example.com"),
            ("Jane Smith", "0987654321", "jane@example.com"),
            ("Emily Johnson", "1122334455", "emily@example.com"),
            ("Michael Brown", "2233445566", "michael@example.com")
        ]

        # Create Treeview
        self.tree = ttk.Treeview(self.root, columns=("Name", "Phone", "Email"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Phone", text="Phone Number")
        self.tree.heading("Email", text="Email Address")

        self.tree.column("Name", anchor=tk.CENTER, width=200)
        self.tree.column("Phone", anchor=tk.CENTER, width=150)
        self.tree.column("Email", anchor=tk.CENTER, width=250)

        self.tree.pack(pady=20)

        # Insert data into Treeview
        for row in self.data:
            self.tree.insert("", tk.END, values=row)

        # Create a button to show selected item
        self.show_button = tk.Button(self.root, text="Show Selected", command=self.show_selected)
        self.show_button.pack(pady=10)

        # Create a label to display the selected item
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=10)

    def show_selected(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            values = item['values']
            self.result_label.config(text=f"Selected: Name={values[0]}, Phone={values[1]}, Email={values[2]}")
        else:
            self.result_label.config(text="No item selected")

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
