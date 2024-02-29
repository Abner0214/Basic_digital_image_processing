import tkinter as tk
import PIL
from PIL import Image,ImageTk





# Haruki reset!
def reset_img():
    # *fileName = entry.get()
    # *global ORIGNAL_open_img
    # *ORIGNAL_open_img = Image.open(fileName)
    global fileName
    global NOW_img
    global ORIGNAL_open_img
    global ORIGNAL_img
    global PRESENT_img  # current image in the window
    ORIGNAL_open_img = Image.open(fileName)
    ORIGNAL_img = ImageTk.PhotoImage(ORIGNAL_open_img)
    NOW_img = ORIGNAL_open_img
    image = PIL.Image.open(fileName)
    wid, hei = image.size
    PRESENT_img = tk.Label(window, image = ORIGNAL_img, width = wid, height = hei)
    PRESENT_img.image = ORIGNAL_img
    PRESENT_img.grid(row = 2, column = 0)

    global Dynamic_Island
    Dynamic_Island.config(text = "Reset! The image is back to the way when it was just opened!", bg = "hot pink", font = ("Arial", 14), width = 70, height = 1)
    window.update_idletasks()




##################################  window  ##################################

window = tk.Tk()
window.title("Image File Operations")
Dynamic_Island = tk.Label(window, text = "Simple graphic user interface of PIL.", bg = "yellow", font = ("Arial", 16), width = 70, height = 2)
