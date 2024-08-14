import tkinter as tk
from tkinterweb import HtmlFrame

# Create the main Tkinter window
root = tk.Tk()
root.title("Map with Markers")

# Create an HtmlFrame widget
frame = HtmlFrame(root, horizontal_scrollbar="auto")

# Use the correct absolute path to the HTML file
html_file_path = "file:///Users/protik/Desktop/Work File/Class Work/Information System lab/map.html"
frame.load_website(html_file_path)

# Pack the frame into the window
frame.pack(fill="both", expand=True)

# Start the Tkinter main loop
root.mainloop()
