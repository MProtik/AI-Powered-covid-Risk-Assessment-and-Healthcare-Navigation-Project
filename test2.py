import tkinter as tk
from tkinter import ttk

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Display Cell Information")
        self.root.geometry("400x200")
        
        self.data = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']
        
        # Create a Listbox to display the list of items
        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(pady=10)
        
        for item in self.data:
            self.listbox.insert(tk.END, item)
        
        # Create a button to show the selected item
        self.show_button = tk.Button(self.root, text="Show Selected", command=self.show_selected)
        self.show_button.pack(pady=10)
        
        # Create a label to display the selected item
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=10)
        
    def show_selected(self):
        # Get the selected item
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_item = self.listbox.get(selected_index)
            # Display the selected item in the label
            self.result_label.config(text=f"Selected Item: {selected_item}")
        else:
            self.result_label.config(text="No item selected")

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
