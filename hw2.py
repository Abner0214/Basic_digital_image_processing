import math
import tkinter as tk
from tkinter import filedialog
import os
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
    
# open image
def open_img():
    
    global fileName
    global NOW_img
    global ORIGNAL_open_img
    global ORIGNAL_img
    global PRESENT_img  # current image in the window
    fileName = filedialog.askopenfilename()
    ORIGNAL_open_img = Image.open(fileName)
    ORIGNAL_img = ImageTk.PhotoImage(ORIGNAL_open_img)
    NOW_img = ORIGNAL_open_img
    image = PIL.Image.open(fileName)
    wid, hei = image.size
    PRESENT_img = tk.Label(window, image = ORIGNAL_img, width = wid, height = hei)
    PRESENT_img.image = ORIGNAL_img
    PRESENT_img.grid(row = 2, column = 0)
        
    global Dynamic_Island
    Dynamic_Island.config(text = "You open this image!", bg = "AntiqueWhite1", font = ("Arial", 16), width = 30, height = 2)
    window.update_idletasks()

# save image 
def save_img():
    global Dynamic_Island
    newName = entry.get()
    if newName[-3:] == ".tif":
        NOW_img.save(newName, "tiff")
        Dynamic_Island.config(text = "The image has been saved in the TIF format! Please check your folder!", bg = "aquamarine", font = ("Arial", 16), width = 70, height = 2)
    else:
        NOW_img.save(newName, "JPEG")
        Dynamic_Island.config(text = "The image has been saved in the JPG format! Please check your folder!", bg = "aquamarine", font = ("Arial", 16), width = 70, height = 2)

    
    window.update_idletasks()   
    
# display image
def display_img():
    
    global Dynamic_Island
    Dynamic_Island.config(text = "Display!", bg = "green3", font = ("Arial", 16), width = 30, height = 1)
    window.update_idletasks()
    
    NOW_img.show()
    
    
# Adjust contrast/brightness of images by linearly
def lin_adj(a, b):
    global NOW_img
    new_img = ORIGNAL_open_img
    for i in range(NOW_img.size[0]):
        for j in range(NOW_img.size[1]):
            X = NOW_img.getpixel((i, j))  # x, y
            X = int(X * a + b)
            if X > 255:
                X = 255
            new_img.putpixel((i, j), X)
    NOW_img = new_img
    new_img = ImageTk.PhotoImage(new_img)
    PRESENT_img.configure(image = new_img)
    PRESENT_img.image = new_img
    global Dynamic_Island
    Dynamic_Island.config(text = "Linearly adjust!", bg = "gold", font = ("Arial", 14), width = 45, height = 2)
    window.update_idletasks()
    
# Adjust contrast/brightness of images by exponentially
def exp_adj(a, b):
    global NOW_img
    new_img = ORIGNAL_open_img
    for i in range(NOW_img.size[0]):
        for j in range(NOW_img.size[1]):
            X = NOW_img.getpixel((i, j))  # x, y
            X = int(math.exp(X * a + b))
            if X > 255:
                X = 255
            new_img.putpixel((i, j), X)
    NOW_img = new_img
    new_img = ImageTk.PhotoImage(new_img)
    PRESENT_img.configure(image = new_img)
    PRESENT_img.image = new_img
    global Dynamic_Island
    Dynamic_Island.config(text = "Exponentially adjust!", bg = "SeaGreen", font = ("Arial", 14), width = 30, height = 2)
    window.update_idletasks()
    
# Adjust contrast/brightness of images by logarithmically
def log_adj(a, b):
    if (b <= 1):
        global Dynamic_Island
        Dynamic_Island.config(text = "[ERROR]: b msut > 1", bg = "red3", font = ("Arial", 16), width = 20, height = 3)
        window.update_idletasks()
        print("[ERROR]: b msut > 1")
        return

    global NOW_img
    new_img = ORIGNAL_open_img
    for i in range(NOW_img.size[0]):
        for j in range(NOW_img.size[1]):
            X = NOW_img.getpixel((i, j))  # x, y
            X = int(math.log(X * a + b))
            if X > 255:
                X = 255
            new_img.putpixel((i, j), X)
    NOW_img = new_img
    new_img = ImageTk.PhotoImage(new_img)
    PRESENT_img.configure(image = new_img)
    PRESENT_img.image = new_img
    Dynamic_Island.config(text = "Logarithmically adjust!", bg = "firebrick", font = ("Arial", 14), width = 40, height = 2)
    window.update_idletasks()
    
# Zoom in and shrink
def resize_img(perc):
    global NOW_img
    new_img = NOW_img.resize((NOW_img.size[0] * perc // 100, NOW_img.size[1] * perc // 100))
    NOW_img = new_img
    new_img = ImageTk.PhotoImage(new_img)
    PRESENT_img.configure(image = new_img)
    PRESENT_img.image = new_img
    global Dynamic_Island
    Dynamic_Island.config(text = "Resize " + str(perc) + " %", bg = "DarkOrange", font = ("Arial", 14), width = 30, height = 2)
    window.update_idletasks()

# Rotate 
def rotate_img(degrees):
    global NOW_img
    new_img = NOW_img.rotate(degrees, expand = "yes")
    NOW_img = new_img
    new_img = ImageTk.PhotoImage(new_img)
    PRESENT_img.configure(image = new_img)
    PRESENT_img.image = new_img
    global Dynamic_Island
    if degrees > 0 :
        Dynamic_Island.config(text = "Rotate +" + str(degrees) + "°", bg = "DarkSlateGray3", font = ("Arial", 14), width = 50, height = 2)
    else:
        Dynamic_Island.config(text = "Rotate " + str(degrees) + "°", bg = "DarkSlateGray2", font = ("Arial", 14), width = 50, height = 2)
    window.update_idletasks()
    
# Gray-level slicing
def gray_lvl_slc(lowerbound, upperbound, keep = True):
    global NOW_img
    new_img = Image.new("L", (NOW_img.size[0], NOW_img.size[1]))
    for i in range(NOW_img.size[0]):
        for j in range(NOW_img.size[1]):
            val = NOW_img.getpixel((i, j))  # x, y
            if (val >= lowerbound and val <= upperbound):
                val = 255
            elif(not keep):
                val = 0
            new_img.putpixel((i, j), val)
    NOW_img = new_img
    new_img = ImageTk.PhotoImage(new_img)
    PRESENT_img.configure(image = new_img)
    PRESENT_img.image = new_img
    global Dynamic_Island
    Dynamic_Island.config(text = "Gray-level slicing ", bg = "dim grey", font = ("Arial", 14), width = 60, height = 2)
    window.update_idletasks()

# if preserve 
def prs_change():
    global if_prs_btn
    global if_prs_text
    if_prs_btn = not if_prs_btn
    if (if_prs_btn):
        if_prs_text.set("Yes")
    else:
        if_prs_text.set("No")
    

#####################################  on the window  #####################################

window = tk.Tk()

window.title("GUI of PIL")
Dynamic_Island = tk.Label(window, text = "Simple graphic user interface of PIL.", bg = "yellow", font = ("Arial", 16), width = 70, height = 2)


                    ###  Define  ###
                               
        ## open/ save / dispaly
# Label
lbl_open = tk.Label(window, text = "First step  ========  ======   ====   ==   = > ",font = ("Arial", 12))
lbl_save_dispaly = tk.Label(window, text = "Please enter a file name to Save / Display this image \n(contain filename extenstion)",font = ("Arial", 10))
# Entry
entry = tk.Entry(window, width = 25)
# Button
btn_open = tk.Button(window, text = "Open a image", command = open_img)
btn_save = tk.Button(window, text = "Save image", command = save_img)
btn_display = tk.Button(window, text = "Display image", command = display_img)
    
        ## Adjust contrast / brightness of images
# Label
lbl_bri = tk.Label(window, text = "Adjust contrast / brightness")
lbl_a = tk.Label(window, text = "a :")
lbl_b = tk.Label(window, text = "b :")
# Entry
entry_a = tk.Entry(window, width = 8)
entry_b = tk.Entry(window, width = 8)
# Button
btn_lin = tk.Button(window, text = "Linear", command = lambda: lin_adj(float(entry_a.get()), float(entry_b.get())))
btn_exp = tk.Button(window, text = "Exp", command = lambda: exp_adj(float(entry_a.get()), float(entry_b.get())))
btn_log = tk.Button(window, text = "Log", command = lambda: log_adj(float(entry_a.get()), float(entry_b.get())))
    
        ## Zoom in and shrink
# Label
lbl_resize = tk.Label(window, text = "Resize the image ( ? %):")
# Entry
entry_resize = tk.Entry(window, width = 8)
# Button
btn_resize = tk.Button(window, text = "Resize", command  = lambda: resize_img(int(entry_resize.get())))

        ## Rotate  
# Label
lbl_rot = tk.Label(window, text = "Rotate the image (by degrees):")
# Entry
entry_rot = tk.Entry(window, width = 8)
# Button
btn_rot = tk.Button(window, text = "Rotate", command = lambda: rotate_img(int(entry_rot.get())))

        ## Gray-level slicing
if_prs_btn = True
if_prs_text = tk.StringVar()
if_prs_text.set("Yes")
# Label
lbl_slc = tk.Label(window, text = "Gray-level slicing")
lbl_lowerbound = tk.Label(window, text = "Lowbound:")
lbl_upperbound = tk.Label(window, text = "Upperbound:")
lbl_prs = tk.Label(window, text = "Preserve ?")
# Entry
entry_lowerbound = tk.Entry(window, width = 8)
entry_upperbound = tk.Entry(window, width = 8)
# Button
btn_slc = tk.Button(window, text = "Slice!", command = lambda: gray_lvl_slc(int(entry_lowerbound.get()), int(entry_upperbound.get()), if_prs_btn))
btn_if_prs = tk.Button(window, textvariable = if_prs_text, command = prs_change)


        ## Haruki reset!
btn_reset = tk.Button(window, text = "Reset the image", command = reset_img)



                    ###  composition  ###
# Heading
Dynamic_Island.grid(row = 0, column = 0, columnspan = 15, rowspan = 1)
# Open / Save / Dispaly
lbl_open.grid(row = 1, column = 0)
btn_open.grid(row = 1, column = 1)
lbl_save_dispaly.grid(row = 3, column = 0)
entry.grid(row = 4, column = 0)
btn_save.grid(row = 4, column = 1)
btn_display.grid(row = 4, column = 2)                                     
# Adjust contrast / brightness of images
lbl_bri.grid(row = 6, column = 0)
lbl_a.grid(row = 6, column = 1)
entry_a.grid(row = 6, column = 2)
lbl_b.grid(row = 6, column = 3)
entry_b.grid(row = 6, column = 4)
btn_lin.grid(row = 6, column = 5)
btn_exp.grid(row = 6, column = 6)
btn_log.grid(row = 6, column = 7)
# Zoom in and shrink
lbl_resize.grid(row = 7, column = 0)
entry_resize.grid(row = 7, column = 1)
btn_resize.grid(row = 7, column = 2)
# Rotate
lbl_rot.grid(row = 8, column = 0)
entry_rot.grid(row = 8, column = 1)
btn_rot.grid(row = 8, column = 2)
# Gray-level slicing
lbl_slc.grid(row = 9, column = 0)
lbl_lowerbound.grid(row = 9, column = 1)
entry_lowerbound.grid(row = 9, column = 2)
lbl_upperbound.grid(row = 9, column = 3)
entry_upperbound.grid(row = 9, column = 4)
lbl_prs.grid(row = 9, column = 5)
btn_if_prs.grid(row = 9, column = 6)
btn_slc.grid(row = 9, column = 7)

# Haruki reset!
btn_reset.grid(row = 15, column = 0)

window.mainloop()