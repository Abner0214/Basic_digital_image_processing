import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

# Initialize the main window
window = tk.Tk()
window.title("Image Processing Application")

# Create a frame for the canvas and scrollbars
frame = tk.Frame(window)
frame.grid(row=2, column=0, sticky='nw')

# Create a canvas within the frame
canvas = tk.Canvas(frame, bg='lightgrey', width=512, height=512)  # Adjust canvas size as needed
canvas.grid(row=0, column=0, sticky='nw')

# Add scrollbars to the canvas
h_scroll = tk.Scrollbar(frame, orient='horizontal', command=canvas.xview)
h_scroll.grid(row=1, column=0, sticky='ew')
v_scroll = tk.Scrollbar(frame, orient='vertical', command=canvas.yview)
v_scroll.grid(row=0, column=1, sticky='ns')
canvas.configure(xscrollcommand=h_scroll.set, yscrollcommand=v_scroll.set)

# Function to update the image on the canvas
def update_image(image_path):
    global photo_image  # Keep a reference to avoid garbage collection
    image = Image.open(image_path)
    photo_image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor='nw', image=photo_image)
    canvas.config(scrollregion=canvas.bbox('all'))

# Example usage
update_image(os.path.join("Image samples\color wheel\gray_level3.png"))  # Replace with the path to your image

window.mainloop()
