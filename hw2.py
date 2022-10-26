import os
import math
import tkinter as tk
from tkinter import filedialog
import PIL
from PIL import Image,ImageTk
import matplotlib.pyplot as plt


# Haruki reset!
def reset_img():

    Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    window.update_idletasks()
    # *fileName = entry.get()
    # *global ORIGNAL_open_img
    # *ORIGNAL_open_img = Image.open(fileName)
    global fileName
    global NOW_img
    global ORIGNAL_open_img
    global ORIGNAL_img
    global lbl_PRESENT_img  # current image in the window

    #ORIGNAL_open_img = Image.open(fileName)

    wid = 512
    hei = 512
    
    if (fileName[-4:] != ".raw"):
        image = PIL.Image.open(fileName)
        wid, hei = image.size
    
    NOW_img = ORIGNAL_open_img
    lbl_PRESENT_img = tk.Label(window, image = ORIGNAL_img, width = wid, height = hei)
    lbl_PRESENT_img.image = ORIGNAL_img
    lbl_PRESENT_img.grid(row = 2, column = 0)

    Dynamic_Island.config(text = "Reset! The image is back to the way when it was just opened!", bg = "hot pink", font = ("Arial", 14), width = 60, height = 2)
    window.update_idletasks()
    
# open image
def open_img():
    
    Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    window.update_idletasks()
    global fileName
    global NOW_img
    global ORIGNAL_open_img
    global ORIGNAL_img
    global lbl_PRESENT_img  # current image in the window
    fileName = filedialog.askopenfilename()
    ORIGNAL_open_img = Image.open(fileName)
    NOW_img = ORIGNAL_open_img
    ORIGNAL_img = ImageTk.PhotoImage(ORIGNAL_open_img)
    image = PIL.Image.open(fileName)
    wid, hei = image.size
    lbl_PRESENT_img = tk.Label(window, image = ORIGNAL_img, width = wid, height = hei)
    lbl_PRESENT_img.image = ORIGNAL_img
    lbl_PRESENT_img.grid(row = 2, column = 0)
    
    nameStr = fileName.split("/")

    Dynamic_Island.config(text = "You open this image: " + nameStr[-1] , bg = "AntiqueWhite1", font = ("Arial", 16), width = 80, height = 2)
    window.update_idletasks()

    return image

# open .raw file
def open_raw():

    Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    window.update_idletasks()
    global fileName
    global NOW_img
    global ORIGNAL_open_img
    global ORIGNAL_img
    global lbl_PRESENT_img  # current image in the window
    fileName = filedialog.askopenfilename(initialdir = "/", title = "Select a .raw file",)
    x = open(fileName,'rb')
    ORIGNAL_open_img = Image.frombytes("L", (512, 512), x.read(), 'raw')
    NOW_img = ORIGNAL_open_img
    ORIGNAL_img = ImageTk.PhotoImage(ORIGNAL_open_img)
    #image = PIL.Image.open(fileName)
    #wid, hei = image.size
    lbl_PRESENT_img = tk.Label(window, image = ORIGNAL_img, width = 512, height = 512)
    lbl_PRESENT_img.image = ORIGNAL_img
    lbl_PRESENT_img.grid(row = 2, column = 0)

    nameStr = fileName.split("/")
    
    Dynamic_Island.config(text = "You open this .raw file: " + nameStr[-1] , bg = "AntiqueWhite1", font = ("Arial", 16), width = 80, height = 2)
    window.update_idletasks()
    if not fileName:
        Dynamic_Island.config(text = "Fail to open this .raw file" , bg = "AntiqueWhite1", font = ("Arial", 16), width = 80, height = 2)
        window.update_idletasks()
        return

# save image 
def save_img():

    Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    window.update_idletasks()
    newName = entry_fileName.get()
    if newName[-3:] == ".tif":
        NOW_img.save(newName, "tiff")
        Dynamic_Island.config(text = "The image has been saved in the TIF format! Please check your folder!", bg = "aquamarine", font = ("Arial", 16), width = 80, height = 2)
    else:
        NOW_img.save(newName, "JPEG")
        Dynamic_Island.config(text = "The image has been saved in the JPG format! Please check your folder!", bg = "aquamarine", font = ("Arial", 16), width = 80, height = 2)

    window.update_idletasks()   
    
# display image
def display_img():
    
    Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    window.update_idletasks()
    Dynamic_Island.config(text = "Display!", bg = "green4", font = ("Arial", 16), width = 80, height = 1)
    window.update_idletasks()
    NOW_img.show()
       
# Display the histogram of images
def display_htg():

    Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    window.update_idletasks()    
    img = NOW_img
    pixels = []
    for x in range(256):
        pixels.append(x)
    width, height = img.size
    counts = [0] * 256
    for x in range(width):
        for y in range(height):
            counts[img.getpixel((x,y))] += 1
    # plot histogram
    plt.bar(pixels,counts)
    Dynamic_Island.config(text = "Display the histogram of images!", bg = "green4", font = ("Arial", 16), width = 80, height = 1)
    window.update_idletasks()
    plt.show()

# Histogram equlization
def auto_level():
    
    Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    window.update_idletasks()
    max_gray_lv = 256
    all_lv = [0] * 256
    temp = [0] * 256
    global NOW_img
    new_img = ORIGNAL_open_img
    for i in range(NOW_img.size[0]):
        for j in range(NOW_img.size[1]):
            X = NOW_img.getpixel((i, j))
            if (X > max_gray_lv):
                max_gray_lv = X
            all_lv[X] += 1 / (NOW_img.size[0] * NOW_img.size[1])
            temp[X] = all_lv[X]
    
    for i in range(1, 255):
        for j in range(0, i-1):
            all_lv[i] += temp[j]

    for i in range(NOW_img.size[0]):
        for j in range(NOW_img.size[1]):
            X = NOW_img.getpixel((i, j))
            new_img.putpixel((i, j), int(all_lv[X] * max_gray_lv))

    NOW_img = new_img
    new_img = ImageTk.PhotoImage(new_img)
    lbl_PRESENT_img.configure(image = new_img)
    lbl_PRESENT_img.image = new_img

    Dynamic_Island.config(text = "Histogram equlization!", bg = "gold", font = ("Arial", 14), width = 80, height = 2)
    window.update_idletasks()

# Bit-Plane images
def bit_plane():

    plane = int(entry_bit_plane.get())

    Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    window.update_idletasks()
    global NOW_img
    new_img = Image.new("L", (NOW_img.size[0], NOW_img.size[1]))
    for i in range(NOW_img.size[0]):
        for j in range(NOW_img.size[1]):
            temp = plane
            val = NOW_img.getpixel((i, j))#x,y
            while(temp>0):
                val//=2
                temp-=1
            if(val%2==1):
                val = 255
            else:
                val = 0
            new_img.putpixel((i, j), val)
    NOW_img = new_img
    new_img = ImageTk.PhotoImage(new_img)
    lbl_PRESENT_img.configure(image = new_img)
    lbl_PRESENT_img.image = new_img

    Dynamic_Island.config(text = "Display bit-plane: " + str(plane), bg = "gold", font = ("Arial", 14), width = 80, height = 2)
    window.update_idletasks()

# smoothing / sharpening
def smoothing():
  
    degree = int(entry_degree.get())
    Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    window.update_idletasks()

    global NOW_img
    new_img = Image.new("L", (NOW_img.size[0], NOW_img.size[1]))
    for i in range(NOW_img.size[0]):
        for j in range(NOW_img.size[1]):
            pixel_sum = 0
            pixel_count = 0
            for k in range(degree*degree):
                row = i + k / degree - degree/2
                col = j + k % degree - degree/2
                if(row < 0  or  col < 0  or  row >= NOW_img.size[0]  or  col >= NOW_img.size[1]):
                    continue
                pixel_sum += NOW_img.getpixel((row,col))
                pixel_count += 1
            if (pixel_count == 0):
                pixel_count = 1
            new_img.putpixel((i, j), round(pixel_sum / pixel_count))

    NOW_img = new_img
    new_img = ImageTk.PhotoImage(new_img)
    lbl_PRESENT_img.configure(image = new_img)
    lbl_PRESENT_img.image = new_img
    
    Dynamic_Island.config(text = "Smoothing!", bg = "gold", font = ("Arial", 14), width = 80, height = 2)
    window.update_idletasks()

def sharpening():

    k = int(entry_degree.get())
    Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    window.update_idletasks()
    if(k < 0):
        print("[Error]: k must >= 0")
        Dynamic_Island.config(text = "[Error]:k must >= 0", bg = "DarkSlateGray3", font = ("Arial", 14), width = 70, height = 2)
        return
    Dynamic_Island.config(text = "Processing ...", bg = "Green3", font = ("Arial", 14), width = 50, height = 2)
    window.update_idletasks()
    global NOW_img
    temp_img = NOW_img.copy()
    
    smoothing()#now now_img is being average filtered
    new_img = Image.new("L", (NOW_img.size[0], NOW_img.size[1]))
    for i in range(NOW_img.size[0]):
        for j in range(NOW_img.size[1]):
            new_img.putpixel((i, j),(k+1)*int(temp_img.getpixel((i,j))) - int(k*NOW_img.getpixel((i,j))))

    NOW_img = new_img
    new_img = ImageTk.PhotoImage(new_img)
    lbl_PRESENT_img.configure(image = new_img)
    lbl_PRESENT_img.image = new_img
    Dynamic_Island.config(text = "Sharpening!", bg = "DarkSlateGray3", font = ("Arial", 14), width = 80, height = 2)
    window.update_idletasks()

# median / Laplacian mask
def median():

    Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    window.update_idletasks()
    degree = int(entry_degree.get())
    global NOW_img
    new_img = Image.new("L", (NOW_img.size[0], NOW_img.size[1]))
    for i in range(NOW_img.size[0]):
        for j in range(NOW_img.size[1]):
            all_pixel = []
            for k in range(degree * degree):
                row = i + int(k / degree) - int(degree / 2)
                col = j + int(k % degree) - int(degree / 2)
                if(row < 0 or col < 0 or row >= NOW_img.size[0] or col >= NOW_img.size[1]):
                    continue
                all_pixel.append(NOW_img.getpixel((row, col)))
            all_pixel.sort()
            new_img.putpixel((i, j), all_pixel[int(len(all_pixel) / 2)])
            del all_pixel
    
    NOW_img = new_img
    new_img = ImageTk.PhotoImage(new_img)
    lbl_PRESENT_img.configure(image = new_img)
    lbl_PRESENT_img.image = new_img
    Dynamic_Island.config(text = "Median filter!", bg = "DarkSlateGray3", font = ("Arial", 14), width = 80, height = 2)
    window.update_idletasks()

def Laplacian():
    
    Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    window.update_idletasks()

    global NOW_img
    new_img = Image.new("L", (NOW_img.size[0], NOW_img.size[1]))
    for i in range(NOW_img.size[0]):
        for j in range(NOW_img.size[1]):
            sum_pixel = 0
            for k in range(9):
                row = i + int(k / 3) - int(3 / 2)
                col = j + int(k % 3) - int(3 / 2)
                if(row < 0  or  col < 0  or  row >= NOW_img.size[0]  or  col >= NOW_img.size[1]):
                    continue
                elif(k==4):
                    sum_pixel -= NOW_img.getpixel((row,col))*8
                else:
                    sum_pixel += NOW_img.getpixel((row,col))
            new_img.putpixel((i, j), NOW_img.getpixel((i,j))-(sum_pixel))
            
    NOW_img = new_img
    new_img = ImageTk.PhotoImage(new_img)
    lbl_PRESENT_img.configure(image = new_img)
    lbl_PRESENT_img.image = new_img
    Dynamic_Island.config(text = "Wearing Laplacian mask!", bg = "DarkSlateGray3", font = ("Arial", 14), width = 80, height = 2)
    window.update_idletasks()



#####################################  on the window  #####################################

window = tk.Tk()

window.title("GUI of PIL")
Dynamic_Island = tk.Label(window, text = "A simple graphic user interface of PIL.", bg = "yellow", font = ("Arial", 16), width = 80, height = 2)

                    ###  Define  ###
                          
        ## open / save / dispaly
# Label
lbl_open = tk.Label(window, text = "First step  ========  OPEN   ====   ==   = > ",font = ("Arial", 12))
lbl_save_dispaly = tk.Label(window, text = "Please enter a file name to Save / Display the image (contain filename extenstion)",font = ("Arial", 10))
# Entry
entry_fileName = tk.Entry(window, width = 25)
# Button
btn_open = tk.Button(window, text = "Open a image", command = open_img)
btn_save = tk.Button(window, text = "Save image", command = save_img)
btn_display = tk.Button(window, text = "Display image", command = display_img)
        ## open .raw file
btn_raw = tk.Button(window, text = "Open .raw file", command = open_raw)
        ## Haruki reset!
btn_reset = tk.Button(window, text = "Reset current image", command = reset_img)
        ## Display the histogram of images
lbl_eql = tk.Label(window, text = "Histogram Equlization")
btn_htg = tk.Button(window, text = "Histogram of current images", command = display_htg)
btn_htg_eql = tk.Button(window, text = "Equlization", command = auto_level)
        ## Bit-plane image
# Label
lbl_bit_plane = tk.Label(window, text = "Bit-plane image ( Please enter a number (1 - 7) ):")
# Entry
entry_bit_plane = tk.Entry(window, width = 8)
# Button
btn_bit_plane = tk.Button(window, text = "Slice", command = bit_plane)
        ## [Spatial Filters] smoothing / sharpening / median filter / Laplacian mask
# Label
lbl_spt_flt = tk.Label(window, text = "Spatial Filters")
# Entry
entry_degree = tk.Entry(window, width = 8)
# Button
btn_smt = tk.Button(window, text = "Smoothing", command = smoothing)
btn_shp = tk.Button(window, text = "Sharpening", command = sharpening)
btn_med = tk.Button(window, text = "Median", command = median)
btn_lpl = tk.Button(window, text = "Laplacian", command = Laplacian)


                    ###  composition  ###
## Heading
Dynamic_Island.grid(row = 0, column = 0, columnspan = 15, rowspan = 1)
## Open / Save / Dispaly
lbl_open.grid(row = 1, column = 0)
btn_open.grid(row = 1, column = 1)
lbl_save_dispaly.grid(row = 3, column = 0)
entry_fileName.grid(row = 4, column = 0)
btn_save.grid(row = 4, column = 1)
btn_display.grid(row = 4, column = 2)
## open .raw file
btn_raw.grid(row = 1, column = 2)
## Haruki reset!
btn_reset.grid(row = 2, column = 1)                               
## Display the histogram of images
btn_htg.grid(row = 2, column = 2)
lbl_eql.grid(row = 5, column = 0)
btn_htg_eql.grid(row = 5, column = 1)
## Bit-plane image
lbl_bit_plane.grid(row = 6, column = 0)
entry_bit_plane.grid(row = 6, column = 1)
btn_bit_plane.grid(row = 6, column = 2)
## Smoothing / Sharpening / Median / Laplacian
lbl_spt_flt.grid(row = 7, column = 0)
entry_degree.grid(row = 7, column = 1)
btn_smt.grid(row = 7, column = 2)
btn_shp.grid(row = 7, column = 3)
btn_med.grid(row = 7, column = 4)
btn_lpl.grid(row = 7, column = 5)


window.mainloop()