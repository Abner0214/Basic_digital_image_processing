import math
from math import cos, radians , degrees , acos,sqrt
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import numpy


global current_photo_image
def update_display_canvas(photo_image):
    global current_photo_image
    current_photo_image = photo_image  # Store the reference globally
    canvas.create_image(0, 0, anchor='nw', image=current_photo_image)
    canvas.config(scrollregion=canvas.bbox('all'))

def showProcessing():
    Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 2)
    window.update_idletasks()

# open image
def open_img():
    
    showProcessing()
    
    global File_path
    global ORIGNAL_open_img
    global ORIGNAL_open_img_copy
    global ORIGNAL_PhotoImage
    
    File_path = filedialog.askopenfilename(title = "Select an image file",)
    ORIGNAL_open_img = Image.open(File_path)
    ORIGNAL_open_img_copy = ORIGNAL_open_img.copy()
    ORIGNAL_PhotoImage = ImageTk.PhotoImage(ORIGNAL_open_img)
    
    update_display_canvas(ORIGNAL_PhotoImage)
    
    nameStr = File_path.split("/")
    Dynamic_Island.config(text = "You open this image: " + nameStr[-1] , bg = "AntiqueWhite1", font = ("Arial", 16), width = 80, height = 2)
    window.update_idletasks()

# open .raw image file
def open_raw():

    showProcessing()

    global File_path
    global ORIGNAL_open_img_copy
    global ORIGNAL_open_img
    global ORIGNAL_PhotoImage
    
    File_path = filedialog.askopenfilename(title = "Select a .raw image file",)
    x = open(File_path,'rb')
    ORIGNAL_open_img = Image.frombytes("L", (512, 512), x.read(), 'raw')
    ORIGNAL_open_img_copy = ORIGNAL_open_img.copy()
    ORIGNAL_PhotoImage = ImageTk.PhotoImage(ORIGNAL_open_img)
    
    update_display_canvas(ORIGNAL_PhotoImage)

    nameStr = File_path.split("/")
    Dynamic_Island.config(text = "You open this .raw image file: " + nameStr[-1] , bg = "AntiqueWhite1", font = ("Arial", 16), width = 80, height = 2)
    window.update_idletasks()

    if not File_path:
        Dynamic_Island.config(text = "Fail to open this .raw image file" , bg = "AntiqueWhite1", font = ("Arial", 16), width = 80, height = 2)
        window.update_idletasks()
        return

# Haruki reset!
def reset_img():

    showProcessing()
    global ORIGNAL_open_img
    global ORIGNAL_open_img_copy
    global ORIGNAL_PhotoImage

    ORIGNAL_open_img_copy = ORIGNAL_open_img.copy()
    update_display_canvas(ORIGNAL_PhotoImage)

    global File_path
    nameStr = File_path.split("/")
    Dynamic_Island.config(text = f"{nameStr[-1]} resetd! It looks like just opened !", bg = "hot pink", font = ("Arial", 14), width = 60, height = 2)
    window.update_idletasks()

# save image 
def save_img():
    # Get the file name from the entry widget
    file_name = entry_fileName.get()

    # Check if the file name is not empty
    if file_name:
        ORIGNAL_open_img_copy.save(file_name)
    else:
        print("Please enter a file name.")

    Dynamic_Island.config(text = f"{file_name} has been saved! Please check your folder!", bg = "aquamarine", font = ("Arial", 16), width = 80, height = 2)
    window.update_idletasks() 
    
# display image
def display_img():
    
    showProcessing()

    global ORIGNAL_open_img_copy
    ORIGNAL_open_img_copy.show()

    Dynamic_Island.config(text = "Display!", bg = "darkorchid2", font = ("Arial", 16), width = 80, height = 2)
    window.update_idletasks()

# Adjust contrast/brightness of images by linearly
def lin_adj(a, b):
    global ORIGNAL_open_img_copy
    for i in range(ORIGNAL_open_img_copy.size[0]):
        for j in range(ORIGNAL_open_img_copy.size[1]):
            X = ORIGNAL_open_img_copy.getpixel((i, j))  # x, y
            X = int(X * a + b)
            if X > 255:
                X = 255
            ORIGNAL_open_img_copy.putpixel((i, j), X)

    photo_image = ImageTk.PhotoImage(ORIGNAL_open_img_copy)
    update_display_canvas(photo_image)
    #X = 1
    #global ORIGNAL_open_img_copy
    #new_img = ImageEnhance.Brightness(ORIGNAL_open_img_copy).enhance(a * X + b)

    global Dynamic_Island
    Dynamic_Island.config(text = "Linearly adjust!", bg = "gold", font = ("Arial", 14), width = 45, height = 2)
    window.update_idletasks()
    
# Adjust contrast/brightness of images by exponentially
def exp_adj(a, b):
    global ORIGNAL_open_img_copy
    for i in range(ORIGNAL_open_img_copy.size[0]):
        for j in range(ORIGNAL_open_img_copy.size[1]):
            X = ORIGNAL_open_img_copy.getpixel((i, j))  # x, y
            X = int(math.exp(X * a + b))
            if X > 255:
                X = 255
            ORIGNAL_open_img_copy.putpixel((i, j), X)

    photo_image = ImageTk.PhotoImage(ORIGNAL_open_img_copy)
    update_display_canvas(photo_image)
    #X = 1
    #global ORIGNAL_open_img_copy
    #new_img = ImageEnhance.Brightness(ORIGNAL_open_img_copy).enhance(math.exp(a * X + b))

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

    global ORIGNAL_open_img_copy
    for i in range(ORIGNAL_open_img_copy.size[0]):
        for j in range(ORIGNAL_open_img_copy.size[1]):
            X = ORIGNAL_open_img_copy.getpixel((i, j))  # x, y
            X = int(math.log(X * a + b))
            if X > 255:
                X = 255
            ORIGNAL_open_img_copy.putpixel((i, j), X)

    photo_image = ImageTk.PhotoImage(ORIGNAL_open_img_copy)
    update_display_canvas(photo_image)
    #X = 1
    #global ORIGNAL_open_img_copy
    #new_img = ImageEnhance.Brightness(ORIGNAL_open_img_copy).enhance(math.log(a * X + b))

    Dynamic_Island.config(text = "Logarithmically adjust!", bg = "firebrick", font = ("Arial", 14), width = 40, height = 2)
    window.update_idletasks()
    
# Zoom in and shrink
def resize_img(perc):

    showProcessing()

    global ORIGNAL_open_img_copy
    new_img = ORIGNAL_open_img_copy.resize((ORIGNAL_open_img_copy.size[0] * perc // 100, ORIGNAL_open_img_copy.size[1] * perc // 100))
    ORIGNAL_open_img_copy = new_img
    photo_image = ImageTk.PhotoImage(new_img)
    update_display_canvas(photo_image)

    global Dynamic_Island
    Dynamic_Island.config(text = "Resize " + str(perc) + " %", bg = "DarkOrange", font = ("Arial", 14), width = 30, height = 2)
    window.update_idletasks()

# Rotate 
def rotate_img(degrees):

    showProcessing()

    global ORIGNAL_open_img_copy
    new_img = ORIGNAL_open_img_copy.rotate(degrees, expand = "yes")
    ORIGNAL_open_img_copy = new_img
    photo_image = ImageTk.PhotoImage(new_img)
    update_display_canvas(photo_image)

    global Dynamic_Island
    if degrees > 0 :
        Dynamic_Island.config(text = "Rotate +" + str(degrees) + "°", bg = "DarkSlateGray3", font = ("Arial", 14), width = 50, height = 2)
    else:
        Dynamic_Island.config(text = "Rotate " + str(degrees) + "°", bg = "DarkSlateGray2", font = ("Arial", 14), width = 50, height = 2)
    window.update_idletasks()
    
# Gray-level slicing
def gray_lvl_slc(lowerbound, upperbound, keep = True):
    global ORIGNAL_open_img_copy
    new_img = Image.new("L", (ORIGNAL_open_img_copy.size[0], ORIGNAL_open_img_copy.size[1]))
    for i in range(ORIGNAL_open_img_copy.size[0]):
        for j in range(ORIGNAL_open_img_copy.size[1]):
            val = ORIGNAL_open_img_copy.getpixel((i, j))  # x, y
            if (val >= lowerbound and val <= upperbound):
                val = 255
            elif(not keep):
                val = 0
            new_img.putpixel((i, j), val)

    ORIGNAL_open_img_copy = new_img
    photo_image = ImageTk.PhotoImage(new_img)
    update_display_canvas(photo_image)

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
     
# Display the histogram of images
def display_htg():

    showProcessing()

    img = ORIGNAL_open_img_copy
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
    Dynamic_Island.config(text = "Display the histogram of images!", bg = "green4", font = ("Arial", 16), width = 80, height = 2)
    window.update_idletasks()
    plt.show()

# Histogram equlization
def auto_level():
    
    showProcessing()

    max_gray_lv = 256
    all_lv = [0] * 256
    temp = [0] * 256
    global ORIGNAL_open_img_copy
    new_img = Image.new("L", (ORIGNAL_open_img_copy.size[0], ORIGNAL_open_img_copy.size[1]))
    for i in range(ORIGNAL_open_img_copy.size[0]):
        for j in range(ORIGNAL_open_img_copy.size[1]):
            X = ORIGNAL_open_img_copy.getpixel((i, j))
            if (X > max_gray_lv):
                max_gray_lv = X
            all_lv[X] += 1 / (ORIGNAL_open_img_copy.size[0] * ORIGNAL_open_img_copy.size[1])
            temp[X] = all_lv[X]
    
    for i in range(1, 255):
        for j in range(0, i-1):
            all_lv[i] += temp[j]

    for i in range(ORIGNAL_open_img_copy.size[0]):
        for j in range(ORIGNAL_open_img_copy.size[1]):
            X = ORIGNAL_open_img_copy.getpixel((i, j))
            new_img.putpixel((i, j), int(all_lv[X] * max_gray_lv))
    
    ORIGNAL_open_img_copy = new_img
    photo_image = ImageTk.PhotoImage(new_img)
    update_display_canvas(photo_image)

    Dynamic_Island.config(text = "Histogram equlization!", bg = "gold", font = ("Arial", 14), width = 80, height = 2)
    window.update_idletasks()

# Bit-Plane images
def bit_plane():

    plane = int(entry_bit_plane.get())

    showProcessing()

    global ORIGNAL_open_img_copy
    new_img = Image.new("L", (ORIGNAL_open_img_copy.size[0], ORIGNAL_open_img_copy.size[1]))
    for i in range(ORIGNAL_open_img_copy.size[0]):
        for j in range(ORIGNAL_open_img_copy.size[1]):
            temp = plane
            val = ORIGNAL_open_img_copy.getpixel((i, j))#x,y
            while(temp>0):
                val//=2
                temp-=1
            if(val%2==1):
                val = 255
            else:
                val = 0
            new_img.putpixel((i, j), val)
    
    ORIGNAL_open_img_copy = new_img
    photo_image = ImageTk.PhotoImage(new_img)
    update_display_canvas(photo_image)

    Dynamic_Island.config(text = "Bit-plane: " + str(plane), bg = "gold", font = ("Arial", 14), width = 80, height = 2)
    window.update_idletasks()

# smoothing
def smoothing():
  
    showProcessing()

    degree = int(entry_degree.get())
    global ORIGNAL_open_img_copy
    new_img = Image.new("L", (ORIGNAL_open_img_copy.size[0], ORIGNAL_open_img_copy.size[1]))
    for i in range(ORIGNAL_open_img_copy.size[0]):
        for j in range(ORIGNAL_open_img_copy.size[1]):
            pixel_sum = 0
            pixel_count = 0
            for k in range(degree*degree):
                row = i + k / degree - degree/2
                col = j + k % degree - degree/2
                if(row < 0  or  col < 0  or  row >= ORIGNAL_open_img_copy.size[0]  or  col >= ORIGNAL_open_img_copy.size[1]):
                    continue
                pixel_sum += ORIGNAL_open_img_copy.getpixel((row,col))
                pixel_count += 1
            if (pixel_count == 0):
                pixel_count = 1
            new_img.putpixel((i, j), round(pixel_sum / pixel_count))

    ORIGNAL_open_img_copy = new_img
    photo_image = ImageTk.PhotoImage(new_img)
    update_display_canvas(photo_image)
    
    Dynamic_Island.config(text = "Smoothing!", bg = "gold", font = ("Arial", 14), width = 80, height = 2)
    window.update_idletasks()

# sharpening
def sharpening():

    k = int(entry_degree.get())
    showProcessing()
    if(k < 0):
        print("[Error]: k must >= 0")
        Dynamic_Island.config(text = "[Error]:k must >= 0", bg = "DarkSlateGray3", font = ("Arial", 14), width = 70, height = 2)
        return
    showProcessing()
    global ORIGNAL_open_img_copy
    temp_img = ORIGNAL_open_img_copy.copy()
    
    smoothing()#now ORIGNAL_open_img_copy is being average filtered
    new_img = Image.new("L", (ORIGNAL_open_img_copy.size[0], ORIGNAL_open_img_copy.size[1]))
    for i in range(ORIGNAL_open_img_copy.size[0]):
        for j in range(ORIGNAL_open_img_copy.size[1]):
            new_img.putpixel((i, j),(k+1)*int(temp_img.getpixel((i,j))) - int(k*ORIGNAL_open_img_copy.getpixel((i,j))))

    ORIGNAL_open_img_copy = new_img
    photo_image = ImageTk.PhotoImage(new_img)
    update_display_canvas(photo_image)

    Dynamic_Island.config(text = "Sharpening!", bg = "DarkSlateGray3", font = ("Arial", 14), width = 80, height = 2)
    window.update_idletasks()

# median smoothing
def median():

    showProcessing()
    degree = int(entry_degree.get())
    global ORIGNAL_open_img_copy
    new_img = Image.new("L", (ORIGNAL_open_img_copy.size[0], ORIGNAL_open_img_copy.size[1]))
    for i in range(ORIGNAL_open_img_copy.size[0]):
        for j in range(ORIGNAL_open_img_copy.size[1]):
            all_pixel = []
            for k in range(degree * degree):
                row = i + int(k / degree) - int(degree / 2)
                col = j + int(k % degree) - int(degree / 2)
                if(row < 0 or col < 0 or row >= ORIGNAL_open_img_copy.size[0] or col >= ORIGNAL_open_img_copy.size[1]):
                    continue
                all_pixel.append(ORIGNAL_open_img_copy.getpixel((row, col)))
            all_pixel.sort()
            new_img.putpixel((i, j), all_pixel[int(len(all_pixel) / 2)])
            del all_pixel
    
    ORIGNAL_open_img_copy = new_img
    photo_image = ImageTk.PhotoImage(new_img)
    update_display_canvas(photo_image)

    Dynamic_Island.config(text = "Median filter!", bg = "DarkSlateGray3", font = ("Arial", 14), width = 80, height = 2)
    window.update_idletasks()

# Laplacian mask
def Laplacian():
    
    showProcessing()

    global ORIGNAL_open_img_copy
    new_img = Image.new("L", (ORIGNAL_open_img_copy.size[0], ORIGNAL_open_img_copy.size[1]))
    for i in range(ORIGNAL_open_img_copy.size[0]):
        for j in range(ORIGNAL_open_img_copy.size[1]):
            sum_pixel = 0
            for k in range(9):
                row = i + int(k / 3) - int(3 / 2)
                col = j + int(k % 3) - int(3 / 2)
                if(row < 0  or  col < 0  or  row >= ORIGNAL_open_img_copy.size[0]  or  col >= ORIGNAL_open_img_copy.size[1]):
                    continue
                elif(k==4):
                    sum_pixel -= ORIGNAL_open_img_copy.getpixel((row,col))*8
                else:
                    sum_pixel += ORIGNAL_open_img_copy.getpixel((row,col))
            new_img.putpixel((i, j), ORIGNAL_open_img_copy.getpixel((i,j))-(sum_pixel))
            
    ORIGNAL_open_img_copy = new_img
    photo_image = ImageTk.PhotoImage(new_img)
    update_display_canvas(photo_image)

    Dynamic_Island.config(text = "Wearing Laplacian mask!", bg = "DarkSlateGray3", font = ("Arial", 14), width = 80, height = 2)
    window.update_idletasks()

# log |F(u,v)|
# magnitude-only image
# phase-only image
def log_mag_pha_img():
    
    showProcessing()

    global ORIGNAL_open_img_copy
    a = []
    for i in range(ORIGNAL_open_img_copy.size[0]):
        temp = []
        for j in range(ORIGNAL_open_img_copy.size[1]):
            temp.append(ORIGNAL_open_img_copy.getpixel((i, j)))
        a.append(temp)
        del temp
    b = numpy.array(a)
    freq = numpy.fft.fft2(b)
    freq = numpy.fft.fftshift(freq)
    phase = freq
    freq = numpy.abs(freq)
    freq = freq + 0.000000001
    mag = freq
    mag = mag + 0.000000001
    phase = phase/(mag)
    freq = numpy.log(freq)
    freq = freq * 20    
    mag = numpy.fft.ifftshift(mag)
    mag = numpy.fft.ifft2(mag)
    phase = numpy.fft.ifftshift(phase)
    phase = numpy.fft.ifft2(phase)
    
    phase = numpy.log((phase))
    phase *= 20
    mag = numpy.log(mag)
    mag = mag * 20
    
    phase = numpy.real(phase)
    mag = numpy.real(mag)
    
    mag = numpy.transpose(mag)
    phase = numpy.transpose(phase)
    freq = numpy.transpose(freq)
    fig,ax = plt.subplots(2,2)
    
    ax[0, 0].title.set_text("Histogram of images")
    ax[0, 0].hist(freq.ravel(),bins = 100)
    ax[0, 1].title.set_text("Spectrum image of log |F(u,v)|")
    ax[0, 1].imshow(freq, interpolation="none", cmap="gray", vmin=0, vmax=255)
    ax[1, 0].title.set_text("Magnitude-only image")
    ax[1, 0].imshow(mag, interpolation="none", cmap="gray", vmin=0, vmax=255)
    ax[1, 1].title.set_text("phase-only image")
    ax[1, 1].imshow(phase, interpolation="none", cmap="gray")

    Dynamic_Island.config(text = "Display the spectrum image of log |F(u,v)|, magnitude-only image ,and phase-only image", bg = "DarkSlateGray2", font = ("Arial", 14), width = 80, height = 2)
    window.update_idletasks()

    fig.set_figheight(8)
    fig.set_figwidth(8)
    
    plt.show()

# Multiplying the image by (-1)^(x+y)
# Computing the DFT
# Taking the complex conjugate of the transform
# Computing the inverse DFT
# Multiplying the real part of the result by (-1)^(x+y)
def step1_5():

    showProcessing()

    global ORIGNAL_open_img_copy
    a = []
    for i in range(ORIGNAL_open_img_copy.size[0]):
        temp = []
        for j in range(ORIGNAL_open_img_copy.size[1]):
            if((i+j)%2==0):
                temp.append(ORIGNAL_open_img_copy.getpixel((i, j)))
            else:
                temp.append(ORIGNAL_open_img_copy.getpixel((i, j))*-1)
        a.append(temp)
        del temp
    step1 = numpy.array(a)
    
    step2 = numpy.fft.fft2(step1)
    step2 = numpy.fft.fftshift(step2)
    step3 = numpy.conjugate(step2)
    step4 = numpy.fft.ifftshift(step3)
    step4 = numpy.fft.ifft2(step4)
    
    step5 = step4
    for i in range(ORIGNAL_open_img_copy.size[0]):
        for j in range(ORIGNAL_open_img_copy.size[1]):
            if((i+j)%2==1):
                step5[i][j]*=-1
    
    fig,ax = plt.subplots(2,3)
    
    step1 = numpy.transpose(step1)
    step2 = numpy.transpose(numpy.log(numpy.abs(step2))*20)
    step3 = numpy.transpose(numpy.log(numpy.abs(step3))*20)
    step4 = numpy.transpose(numpy.log(numpy.abs(step4))*20)
    step5 = numpy.transpose(numpy.real(step5))
    ax[0, 0].title.set_text("Original image")
    ax[0, 0].imshow(ORIGNAL_open_img_copy, interpolation="none",cmap="gray",vmin=0,vmax=255)
    ax[0, 1].title.set_text("Step. (1): Multiplying the image by (-1)^(x+y)")
    ax[0, 1].imshow(step1, interpolation="none",cmap="gray",vmin=0,vmax=255)
    ax[0, 2].title.set_text("Step. (2): Computing the DFT")
    ax[0, 2].imshow(step2, interpolation="none",cmap="gray",vmin=0,vmax=255)
    ax[1, 0].title.set_text("Step. (3): Taking the complex conjugate of the transform")
    ax[1, 0].imshow(step3, interpolation="none",cmap="gray",vmin=0,vmax=255)
    ax[1, 1].title.set_text("Step. (4): Computing the inverse DFT")
    ax[1, 1].imshow(step4, interpolation="none",cmap="gray",vmin=0,vmax=255)
    ax[1, 2].title.set_text("Step. (5): Multiplying the real part of the result by (-1)^(x+y)")
    ax[1, 2].imshow(step5, interpolation="none",cmap="gray",vmin=0,vmax=255)

    Dynamic_Island.config(text = "Display DFT processing", bg = "ghost white", font = ("Arial", 14), width = 80, height = 2)
    window.update_idletasks()
    #fig.canvas.set_window_title("Problem. 3")

    fig.set_figheight(8)
    fig.set_figwidth(16)
    plt.show()
            
# Red component image
def red_img():

    showProcessing()

    global ORIGNAL_open_img_copy
    split_img = Image.Image.split(ORIGNAL_open_img_copy)
    new_img = Image.new("RGB", (ORIGNAL_open_img_copy.size[0], ORIGNAL_open_img_copy.size[1]))
    for i in range(ORIGNAL_open_img_copy.size[0]):
        for j in range(ORIGNAL_open_img_copy.size[1]):
            r = split_img[0].getpixel((i, j))
            new_img.putpixel((i, j), (r, 0, 0))
            
    ORIGNAL_open_img_copy = new_img
    photo_image = ImageTk.PhotoImage(new_img)
    update_display_canvas(photo_image)

    Dynamic_Island.config(text = "Red component image", bg = "red", font = ("Arial", 14), width = 80, height = 2)
    window.update_idletasks()

# Green component image
def green_img():

    showProcessing()

    global ORIGNAL_open_img_copy
    split_img = Image.Image.split(ORIGNAL_open_img_copy)
    new_img = Image.new("RGB", (ORIGNAL_open_img_copy.size[0], ORIGNAL_open_img_copy.size[1]))
    for i in range(ORIGNAL_open_img_copy.size[0]):
        for j in range(ORIGNAL_open_img_copy.size[1]):
            g = split_img[1].getpixel((i, j))
            new_img.putpixel((i, j), (0, g, 0))
            
    ORIGNAL_open_img_copy = new_img
    photo_image = ImageTk.PhotoImage(new_img)
    update_display_canvas(photo_image)

    Dynamic_Island.config(text = "Green component image", bg = "green2", font = ("Arial", 14), width = 80, height = 2)
    window.update_idletasks()

# Blue component image
def blue_img():

    showProcessing()

    global ORIGNAL_open_img_copy
    split_img = Image.Image.split(ORIGNAL_open_img_copy)
    new_img = Image.new("RGB", (ORIGNAL_open_img_copy.size[0], ORIGNAL_open_img_copy.size[1]))
    for i in range(ORIGNAL_open_img_copy.size[0]):
        for j in range(ORIGNAL_open_img_copy.size[1]):
            b = split_img[2].getpixel((i, j))
            new_img.putpixel((i, j), (0, 0, b))
            
    ORIGNAL_open_img_copy = new_img
    photo_image = ImageTk.PhotoImage(new_img)
    update_display_canvas(photo_image)
    
    Dynamic_Island.config(text = "Blue component image", bg = "blue", font = ("Arial", 14), width = 80, height = 2)
    window.update_idletasks()

# RGB to HSI
def rgb_to_hsi(R ,G, B):
    
    r = R
    g = G
    b = B

    I = (R+G+B)/3
    
    if I > 0:
        S  = 1 - min([r, g, b]) / I
    else:
        S = 0
    if g>=b:
        try:
            H=degrees(acos((r-g/2-b/2)/sqrt(r**2+g**2+b**2-g*b-r*g-r*b)))
        except:
            H = 0
    else:
        try:
            H = 360 - degrees(acos((r-g/2-b/2)/sqrt(r**2+g**2+b**2-g*b-r*g-r*b)))
        except:
            H = 359

    return (H, S, I)

# HSI to RGB
def hsi_to_rgb(h, s, i):

    if h == 0:
        r = i + 2*i*s
        g = i - i*s
        b = i - i*s
    elif 0 < h < 120 :
        b = i * (1 - s)
        r = i * (1 + (s * cos(radians(h)) / cos(radians(60) - radians(h))))
        g = i * 3 - (r + b)
    elif h == 120:
        r = i - i*s
        g = i + 2*i*s
        b = i- i*s
    elif 120 < h <= 240:
        h -= 120
        r = i * (1 - s)
        g = i * (1 + (s * cos(radians(h)) / cos(radians(60) - radians(h))))
        b = 3 * i - (r + g)
    elif h==240:
        r = i - i*s
        g = i - i*s
        b = i + 2*i*s
    else:
        h -= 240
        g = i * (1 - s)
        b = i * (1 + (s * cos(radians(h)) / cos(radians(60) - radians(h))))
        r = i * 3 - (g + b)
    # print(r,g,b)

    return [i if 0 <= i <=255 else 255 for i in [r, g, b]]        

# RGB to Hue, saturation, Intenstity subplot
def rgb_to_h_s_i_subplot():

    showProcessing()

    global ORIGNAL_open_img_copy
    split_img = Image.Image.split(ORIGNAL_open_img_copy)
    h_img = Image.new("L", (ORIGNAL_open_img_copy.size[0], ORIGNAL_open_img_copy.size[1]))
    s_img = Image.new("L", (ORIGNAL_open_img_copy.size[0], ORIGNAL_open_img_copy.size[1]))
    i_img = Image.new("L", (ORIGNAL_open_img_copy.size[0], ORIGNAL_open_img_copy.size[1]))
    for i in range(ORIGNAL_open_img_copy.size[0]):
        for j in range(ORIGNAL_open_img_copy.size[1]):
            R = split_img[0].getpixel((i, j))
            G = split_img[1].getpixel((i, j))
            B = split_img[2].getpixel((i, j))
            H, S, I = rgb_to_hsi(R, G, B)
            h_img.putpixel((i, j), round(H/360*255))
            s_img.putpixel((i, j), round(S*255))
            i_img.putpixel((i, j), round(I))

    fig,ax = plt.subplots(1,4)
    
    ax[0].title.set_text("Original image")
    ax[0].imshow(ORIGNAL_open_img_copy, interpolation="none",cmap="gray",vmin=0,vmax=255)
    ax[1].title.set_text("Hue")
    ax[1].imshow(h_img, interpolation="none",cmap="gray",vmin=0,vmax=255)
    ax[2].title.set_text("Saturation")
    ax[2].imshow(s_img, interpolation="none",cmap="gray",vmin=0,vmax=255)
    ax[3].title.set_text("Intensity")
    ax[3].imshow(i_img, interpolation="none",cmap="gray",vmin=0,vmax=255)

    Dynamic_Island.config(text = "RGB to HSI", bg = "ghost white", font = ("Arial", 14), width = 80, height = 2)
    window.update_idletasks()
    #fig.canvas.set_window_title("Problem. 3")

    fig.set_figheight(4)
    fig.set_figwidth(12)
    plt.show()

# RGB complements to enhance the detail
def rgb_complements():

    showProcessing()

    global ORIGNAL_open_img_copy
    split_img = Image.Image.split(ORIGNAL_open_img_copy)
    new_img = Image.new("RGB", (ORIGNAL_open_img_copy.size[0], ORIGNAL_open_img_copy.size[1]))
    for i in range(ORIGNAL_open_img_copy.size[0]):
        for j in range(ORIGNAL_open_img_copy.size[1]):
            r = split_img[0].getpixel((i, j))
            g = split_img[1].getpixel((i, j))
            b = split_img[2].getpixel((i, j))
            new_img.putpixel((i, j), (255 - r, 255 - g, 255 - b))
            
    ORIGNAL_open_img_copy = new_img
    photo_image = ImageTk.PhotoImage(new_img)
    update_display_canvas(photo_image)
    
    Dynamic_Island.config(text = "RGB model color complements", bg = "ghost white", font = ("Arial", 14), width = 80, height = 2)
    window.update_idletasks()

def rgb_hsi_sharping():

    showProcessing()

    degree = 5

    global ORIGNAL_open_img_copy
    split_img = Image.Image.split(ORIGNAL_open_img_copy)
    smoothing_img = Image.new("RGB", (ORIGNAL_open_img_copy.size[0], ORIGNAL_open_img_copy.size[1]))
    I_smoothing_img = Image.new("RGB", (ORIGNAL_open_img_copy.size[0], ORIGNAL_open_img_copy.size[1]))
    # smoothing
    for i in range(ORIGNAL_open_img_copy.size[0]):
        for j in range(ORIGNAL_open_img_copy.size[1]):
            R_sum = 0
            G_sum = 0
            B_sum = 0
            I_sum = 0
            pixel_count = 0
            for k in range(degree*degree):
                row = i + k / degree - degree/2
                col = j + k % degree - degree/2
                if(row < 0  or  col < 0  or  row >= ORIGNAL_open_img_copy.size[0]  or  col >= ORIGNAL_open_img_copy.size[1]):
                    continue
                R_sum += split_img[0].getpixel((row,col))
                G_sum += split_img[1].getpixel((row,col))
                B_sum += split_img[2].getpixel((row,col))
                h, s, I = rgb_to_hsi(split_img[0].getpixel((row,col)), split_img[1].getpixel((row,col)), split_img[2].getpixel((row,col)))
                I_sum += I
                pixel_count += 1
            if (pixel_count == 0):
                pixel_count = 1
            smoothing_img.putpixel((i, j), (round(R_sum/pixel_count), round(G_sum/pixel_count), round(B_sum/pixel_count)))
            r, g, b = hsi_to_rgb(h, s, round(I/pixel_count))
            I_smoothing_img.putpixel((i, j), (round(r), round(g), round(b)))
    
    # RGB Laplacian # HSI Laplacian
    RGB_Lap_img = Image.new("RGB", (ORIGNAL_open_img_copy.size[0], ORIGNAL_open_img_copy.size[1]))
    HSI_Lap_img = Image.new("RGB", (ORIGNAL_open_img_copy.size[0], ORIGNAL_open_img_copy.size[1]))
    split_smoothing_img = Image.Image.split(smoothing_img)
    split_I_smoothing_img = Image.Image.split(smoothing_img)
    for i in range(ORIGNAL_open_img_copy.size[0]):
        for j in range(ORIGNAL_open_img_copy.size[1]):
            r_sum = 0
            g_sum = 0
            b_sum = 0
            
            h_sum = 0
            s_sum = 0
            i_sum = 0
            for k in range(9):
                row = i + int(k / 3) - int(3 / 2)
                col = j + int(k % 3) - int(3 / 2)
                if(row < 0  or  col < 0  or  row >= ORIGNAL_open_img_copy.size[0]  or  col >= ORIGNAL_open_img_copy.size[1]):
                    continue
                elif(k==4):
                    r_sum -= split_smoothing_img[0].getpixel((row,col))*8
                    g_sum -= split_smoothing_img[1].getpixel((row,col))*8
                    b_sum -= split_smoothing_img[2].getpixel((row,col))*8

                    h, s, I = rgb_to_hsi(split_I_smoothing_img[0].getpixel((row,col)), split_I_smoothing_img[1].getpixel((row,col)), split_I_smoothing_img[2].getpixel((row,col)))
                    
                    i_sum -= I*8
                else:
                    r_sum += split_smoothing_img[0].getpixel((row,col))
                    g_sum += split_smoothing_img[1].getpixel((row,col))
                    b_sum += split_smoothing_img[2].getpixel((row,col))

                    h, s, I = rgb_to_hsi(split_I_smoothing_img[0].getpixel((row,col)), split_I_smoothing_img[1].getpixel((row,col)), split_I_smoothing_img[2].getpixel((row,col)))
                    
                    i_sum += I

            r = split_smoothing_img[0].getpixel((i, j))
            g = split_smoothing_img[1].getpixel((i, j))
            b = split_smoothing_img[2].getpixel((i, j))
            h,s,I = rgb_to_hsi(r,g,b)

            RGB_Lap_img.putpixel((i, j), (r - (r_sum), g - (g_sum), b - (b_sum)))
            r, g, b = hsi_to_rgb(h, s, I-i_sum)
            # r=g=b = I-i_sum
            # print(I-i_sum,i_sum)
            HSI_Lap_img.putpixel((i, j), (round(r), round(g), round(b)))
    
    fig, ax = plt.subplots(1,3)
    
    ax[0].title.set_text("Original image")
    ax[0].imshow(ORIGNAL_open_img_copy, interpolation="none",cmap="gray",vmin=0,vmax=255)
    ax[1].title.set_text("RGB Laplacian")
    ax[1].imshow(RGB_Lap_img, interpolation="none",cmap="gray",vmin=0,vmax=255)
    ax[2].title.set_text("HSI Laplacian")
    ax[2].imshow(HSI_Lap_img, interpolation="none",cmap="gray",vmin=0,vmax=255)

    Dynamic_Island.config(text = "RGB Laplacian and HSI Laplacian", bg = "ghost white", font = ("Arial", 14), width = 80, height = 2)
    window.update_idletasks()
    #fig.canvas.set_window_title("Problem. 3")

    fig.set_figheight(4)
    fig.set_figwidth(10)
    plt.show()

# Segmenting the feathers
def seg_fea_mask():
    
    showProcessing()

    global ORIGNAL_open_img_copy
    split_img = Image.Image.split(ORIGNAL_open_img_copy)
    feathers_img = Image.new("RGB", (ORIGNAL_open_img_copy.size[0], ORIGNAL_open_img_copy.size[1]))
    H_img = Image.new("L", (ORIGNAL_open_img_copy.size[0], ORIGNAL_open_img_copy.size[1]))
    S_img = Image.new("L", (ORIGNAL_open_img_copy.size[0], ORIGNAL_open_img_copy.size[1]))

    for i in range (ORIGNAL_open_img_copy.size[0]):
        for j in range (ORIGNAL_open_img_copy.size[1]):
            r = split_img[0].getpixel((i, j))
            g = split_img[1].getpixel((i, j))
            b = split_img[2].getpixel((i, j))
            H, S, I = rgb_to_hsi(r, g, b)
            H_img.putpixel((i, j), round(H/360*255))
            S_img.putpixel((i, j), round(S*255))
            if (325 > H > 250  and ORIGNAL_open_img_copy.size[0] * 0.1 < i < ORIGNAL_open_img_copy.size[0] * 0.6):
                feathers_img.putpixel((i, j), (r, g, b))
            else:
                feathers_img.putpixel((i, j), (0, 0, 0))

    fig, ax = plt.subplots(1,4)
    
    ax[0].title.set_text("Original image")
    ax[0].imshow(ORIGNAL_open_img_copy, interpolation="none",cmap="gray",vmin=0,vmax=255)
    ax[1].title.set_text("Hue")
    ax[1].imshow(H_img, interpolation="none",cmap="gray",vmin=0,vmax=255)
    ax[2].title.set_text("Saturation")
    ax[2].imshow(S_img, interpolation="none",cmap="gray",vmin=0,vmax=255)
    ax[3].title.set_text("Feathers")
    ax[3].imshow(feathers_img, interpolation="none",cmap="gray",vmin=0,vmax=255)

    Dynamic_Island.config(text = "RGB Laplacian and HSI Laplacian", bg = "ghost white", font = ("Arial", 14), width = 80, height = 2)
    window.update_idletasks()
    #fig.canvas.set_window_title("Problem. 3")

    fig.set_figheight(4)
    fig.set_figwidth(12)
    plt.show()


###############################################  on the window  ###############################################

window = tk.Tk()
window.title("Basic Digital Image Processing")

Dynamic_Island = tk.Label(window, text = "Please open an image file first!", bg = "gold", font = ("Arial", 16), width = 80, height = 2)

                    ######  Define component ######

        ### Canvas and scrollbars for displaying the current image

# Create a frame for the canvas and scrollbars
frame = ttk.Frame(window)
frame.grid(row=2, column=0, sticky='nw')

# Create a canvas within the frame
canvas = tk.Canvas(frame, bg='lightgrey', width=512, height=512)
canvas.grid(row=0, column=0, sticky='nw')

# Add scrollbars to the canvas
h_scroll = ttk.Scrollbar(frame, orient='horizontal', command=canvas.xview)
h_scroll.grid(row=1, column=0, sticky='ew')
v_scroll = ttk.Scrollbar(frame, orient='vertical', command=canvas.yview)
v_scroll.grid(row=0, column=1, sticky='ns')
canvas.configure(xscrollcommand=h_scroll.set, yscrollcommand=v_scroll.set)



        ### open / save / display
# Label
# lbl_open = ttk.Label(window, text = "First step  ========  OPEN   ====   ==   = > ",font = ("Arial", 12))
lbl_save_display = ttk.Label(window, text = "Please enter a file name to Save / Display the image (contain filename extenstion)",font = ("Arial", 10))
# Entry
entry_fileName = ttk.Entry(window, width = 20)
# Button
btn_open = ttk.Button(window, text = "Open an image", command = open_img)
btn_save = ttk.Button(window, text = "Save image", command = save_img)
btn_display = ttk.Button(window, text = "Keep above image in an indenpendent window", command = display_img)
        ### open .raw image file
btn_raw = ttk.Button(window, text = "Open a .raw image", command = open_raw)
        ### Haruki reset!
btn_reset = ttk.Button(window, text = "Reset image", command = reset_img)
        ### Display the histogram of images
lbl_eql = ttk.Label(window, text = "Histogram Equalization")
btn_htg = ttk.Button(window, text = "Display histogram", command = display_htg)
btn_htg_eql = ttk.Button(window, text = "Equalize", command = auto_level)

        ### Adjust contrast / brightness of images
# Label
lbl_bri = ttk.Label(window, text = "Adjust contrast / brightness (aX + b, exp(aX + b), ln(aX + b), b > 1)   |   a: [ integer ] b: [ > 1 ]")
# lbl_a = tk.Label(window, text = "a :")
# lbl_b = tk.Label(window, text = "b :")
# Entry
entry_a = ttk.Entry(window, width = 8)
entry_b = ttk.Entry(window, width = 8)
# Button
btn_lin = ttk.Button(window, text = "Linear", command = lambda: lin_adj(float(entry_a.get()), float(entry_b.get())))
btn_exp = ttk.Button(window, text = "Exp", command = lambda: exp_adj(float(entry_a.get()), float(entry_b.get())))
btn_log = ttk.Button(window, text = "Log", command = lambda: log_adj(float(entry_a.get()), float(entry_b.get())))
    
        ### Zoom in and shrink
# Label
lbl_resize = ttk.Label(window, text = "Resize the image (by percentage)   |   [ > 0 ]")
# Entry
entry_resize = ttk.Entry(window, width = 8)
# Button
btn_resize = ttk.Button(window, text = "Resize", command  = lambda: resize_img(int(entry_resize.get())))

        ### Rotate  
# Label
lbl_rot = ttk.Label(window, text = "Rotate the image (by degrees)   |   [ integer ]")
# Entry
entry_rot = ttk.Entry(window, width = 8)
# Button
btn_rot = ttk.Button(window, text = "Rotate", command = lambda: rotate_img(int(entry_rot.get())))

        ### Gray-level slicing
if_prs_btn = True
if_prs_text = tk.StringVar()
if_prs_text.set("Yes")
# Label
lbl_slc = ttk.Label(window, text = "Gray-level slicing   |   Lowbound: [ 0 - 255 ] Upperbound: [ 0 - 255 ]")
# lbl_lowerbound = ttk.Label(window, text = "Lowbound:")
# lbl_upperbound = ttk.Label(window, text = "Upperbound:")
lbl_prs = ttk.Label(window, text = "Preserve?")
# Entry
entry_lowerbound = ttk.Entry(window, width = 8)
entry_upperbound = ttk.Entry(window, width = 8)
# Button
btn_slc = ttk.Button(window, text = "Slice", command = lambda: gray_lvl_slc(int(entry_lowerbound.get()), int(entry_upperbound.get()), if_prs_btn))
btn_if_prs = ttk.Button(window, textvariable = if_prs_text, command = prs_change)

        ### Bit-plane image
# Label
lbl_bit_plane = ttk.Label(window, text = "Bit-plane image   |   [ 1 - 7 ]")
# Entry
entry_bit_plane = ttk.Entry(window, width = 8)
# Button
btn_bit_plane = ttk.Button(window, text = "Slice", command = bit_plane)

        ### [Spatial Filters] smoothing / sharpening / median filter / Laplacian mask
# Label
lbl_spt_flt = ttk.Label(window, text = "Spatial Filters (degree)   |   [ integer ]")
# Entry
entry_degree = ttk.Entry(window, width = 8)
# Button
btn_smt = ttk.Button(window, text = "Mean", command = smoothing)
btn_shp = ttk.Button(window, text = "Sharpening", command = sharpening)
btn_med = ttk.Button(window, text = "Median", command = median)
btn_lpl = ttk.Button(window, text = "Laplacian", command = Laplacian)

        ### log |F(u,v)|  &  Magnitude and Phase images
# Label
lbl_log_mag_pha_img = ttk.Label(window, text = "2D FFT processing")
# Button
btn_log_mag_pha_img = ttk.Button(window, text = "Do", command = log_mag_pha_img)

        ### 3. step. (1) - (5)
    ## Multiplying the image by (-1)^(x+y)
    ## Computing the DFT
    ## Taking the complex conjugate of the transform
    ## Computing the inverse DFT
    ## Multiplying the real part of the result by (-1)^(x+y)
# Label
lbl_step1_5 = ttk.Label(window, text = "DFT processing")
# Button
btn_step1_5 = ttk.Button(window, text = "Do", command = step1_5)

        ### 4. (b) - (f)
    ## Component image
# Label
lbl_com_img = ttk.Label(window, text = "Component image ")
# Button
btn_red_img = ttk.Button(window, text = "Red", command = red_img)
btn_green_img = ttk.Button(window, text = "Green", command = green_img)
btn_blue_img = ttk.Button(window, text = "Blue", command = blue_img)
    ## Convert RGB to HSI model ,and display its Hue, Saturation, and Intensity components as gray-level images respectively.
# Label
lbl_RGB_to_HSI = ttk.Label(window, text = "Convert RGB to HSI")
# Button
btn_RGB_to_HSI = ttk.Button(window, text = "Do", command = rgb_to_h_s_i_subplot)
    ## Do color complements by using RGB model
# Label
lbl_rgb_cpm = ttk.Label(window, text = "RGB color complementary image (To enhance the detail)")
# Button
btn_rgb_cpm = ttk.Button(window, text = "Do", command = rgb_complements)

    ## Sharping with the Laplacian to this image by using RGB and HSI models
# Label
lbl_rgb_hsi_sharping = ttk.Label(window, text = "Sharping with the Laplacian to this image by using RGB and HSI models")
# Button
btn_rgb_hsi_sharping = ttk.Button(window, text = "Do", command = rgb_hsi_sharping)
    ## segmenting the feathers
lbl_seg_fea = ttk.Label(window, text = "Segmenting the feathers of \"Lenna_512_color.tif\"")
# Button
btn_seg_fea = ttk.Button(window, text = "Do", command = seg_fea_mask)

# ======== Grayscale image ========
lbl_______grayscale_img = ttk.Label(window, text=" ######################  Grayscale image  ###################### ")
# ========== Color image ==========
lbl_______color_img = ttk.Label(window, text=" ######################  Color image  ###################### ")

                    ######  composition  ######
# Heading
Dynamic_Island.grid(row = 0, column = 0, columnspan = 15, rowspan = 1)
# Open image
btn_open.grid(row = 1, column = 1)
# Display image
btn_display.grid(row = 3, column = 0)  
#  Save image
lbl_save_display.grid(row = 4, column = 0)
entry_fileName.grid(row = 4, column = 1)
btn_save.grid(row = 4, column = 2)
# open .raw image file
btn_raw.grid(row = 1, column = 2)
# Haruki reset!
btn_reset.grid(row = 2, column = 1)
lbl_______grayscale_img.grid(row = 5, column = 0)                 
# Adjust contrast / brightness of images
lbl_bri.grid(row = 6, column = 0)
# lbl_a.grid(row = 6, column = 1)
entry_a.grid(row = 6, column = 1)
# lbl_b.grid(row = 6, column = 3)
entry_b.grid(row = 6, column = 2)
btn_lin.grid(row = 6, column = 3)
btn_exp.grid(row = 6, column = 4)
btn_log.grid(row = 6, column = 5)
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
# lbl_lowerbound.grid(row = 9, column = 1)
entry_lowerbound.grid(row = 9, column = 1)
# lbl_upperbound.grid(row = 9, column = 3)
entry_upperbound.grid(row = 9, column = 2)
lbl_prs.grid(row = 9, column = 3)
btn_if_prs.grid(row = 9, column = 4)
btn_slc.grid(row = 9, column = 5)                               
# Histogram equlization
# Display the histogram of images    
lbl_eql.grid(row = 10, column = 0)
btn_htg.grid(row = 10, column = 1)    
btn_htg_eql.grid(row = 10, column = 2)
# Bit-plane image
lbl_bit_plane.grid(row = 11, column = 0)
entry_bit_plane.grid(row = 11, column = 1)
btn_bit_plane.grid(row = 11, column = 2)
# Smoothing / Sharpening / Median / Laplacian
lbl_spt_flt.grid(row = 12, column = 0)
entry_degree.grid(row = 12, column = 1)
btn_smt.grid(row = 12, column = 2)
btn_shp.grid(row = 12, column = 3)
btn_med.grid(row = 12, column = 4)
btn_lpl.grid(row = 12, column = 5)
# 2D FFT log |F(u,v)|  &  Magnitude and Phase images
lbl_log_mag_pha_img.grid(row = 13, column = 0)
btn_log_mag_pha_img.grid(row = 13, column = 1)
# 3. DFT step. (1) - (5)
lbl_step1_5.grid(row = 15, column = 0)
btn_step1_5.grid(row = 15, column = 1)
lbl_______color_img.grid(row = 18, column = 0)
# 4. (b) - (f)
lbl_com_img.grid(row = 20, column = 0)
btn_red_img.grid(row = 20, column = 1)
btn_green_img.grid(row = 20, column = 2)
btn_blue_img.grid(row = 20, column = 3)

lbl_RGB_to_HSI.grid(row = 21, column = 0)
btn_RGB_to_HSI.grid(row = 21, column = 1)

lbl_rgb_cpm.grid(row = 22, column = 0)
btn_rgb_cpm.grid(row = 22, column = 1)

lbl_rgb_hsi_sharping.grid(row = 23, column = 0)
btn_rgb_hsi_sharping.grid(row = 23, column = 1)

lbl_seg_fea.grid(row = 24, column = 0)
btn_seg_fea.grid(row = 24, column = 1)

# After adding all widgets, update the scrollregion of the canvas
window.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

window.mainloop()