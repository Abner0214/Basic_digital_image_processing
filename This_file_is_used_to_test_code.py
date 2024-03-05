import tkinter as tk
from tkinter import ttk

# Create the main application window
window = tk.Tk()
window.title("Application with Scrollbar")

# Configure the grid layout of the window to fill the available space
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Create a canvas and a vertical scrollbar attached to the window
canvas = tk.Canvas(window)
scrollbar = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

# Place the canvas and scrollbar in the window using grid
canvas.grid(row=0, column=0, sticky='nsew')
scrollbar.grid(row=0, column=1, sticky='ns')

# Create a frame that will be inside the canvas (content area)
content_frame = tk.Frame(canvas)

# Place the content_frame inside the canvas
canvas.create_window((0, 0), window=content_frame, anchor="nw")

# Function to update the scrollregion
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

content_frame.bind("<Configure>", on_frame_configure)

# Example of adding widgets into the content_frame
# Replace this part with your widget creation code (e.g., btn_open.grid, lbl_save_display.grid, etc.)
for i in range(50):
    ttk.Button(content_frame, text=f"Button {i}").grid(row=i, column=0, sticky='ew')

# Run the main application loop
window.mainloop()
