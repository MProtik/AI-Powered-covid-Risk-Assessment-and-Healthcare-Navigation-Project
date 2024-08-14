import tkinter as tk
#from tkinter import ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create the main window
root = tk.Tk()
root.title("Matplotlib in Tkinter")
root.geometry("1600x800")

# Create a figure
fig, ax = plt.subplots()

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plot data
ax.plot(x, y)
ax.set_title("Sample Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

# Embed the figure in the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Start the Tkinter event loop
root.mainloop()
