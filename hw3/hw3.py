import os
import math
from math import cos, radians , degrees , acos,sqrt
import tkinter as tk
from tkinter import filedialog
import PIL
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import numpy


def update_display_canvas(photo_image):
    canvas.create_image(0, 0, anchor='nw', image=photo_image)
    canvas.config(scrollregion=canvas.bbox('all'))

def showProcessing():
    Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    window.update_idletasks()

# open image
def open_img():
    
    showProcessing()
    
    global filePath
    global NOW_img
    global ORIGNAL_open_img
    global ORIGNAL_PhotoImage
    
    filePath = filedialog.askopenfilename()
    ORIGNAL_open_img = Image.open(filePath)
    NOW_img = ORIGNAL_open_img.copy()
    ORIGNAL_PhotoImage = ImageTk.PhotoImage(ORIGNAL_open_img)
    
    update_display_canvas(ORIGNAL_PhotoImage)
    
    nameStr = filePath.split("/")
    Dynamic_Island.config(text = "You open this image: " + nameStr[-1] , bg = "AntiqueWhite1", font = ("Arial", 16), width = 80, height = 2)
    window.update_idletasks()

# open .raw image file
def open_raw():

    showProcessing()

    global filePath
    global NOW_img
    global ORIGNAL_open_img
    global ORIGNAL_PhotoImage
    global lbl_PRESENT_img  # current image in the window
    filePath = filedialog.askopenfilename(initialdir = "/", title = "Select a .raw image file",)
    x = open(filePath,'rb')
    ORIGNAL_open_img = Image.frombytes("L", (512, 512), x.read(), 'raw')
    NOW_img = ORIGNAL_open_img.copy()
    ORIGNAL_PhotoImage = ImageTk.PhotoImage(ORIGNAL_open_img)
    
    update_display_canvas(ORIGNAL_PhotoImage)

    nameStr = filePath.split("/")
    Dynamic_Island.config(text = "You open this .raw image file: " + nameStr[-1] , bg = "AntiqueWhite1", font = ("Arial", 16), width = 80, height = 2)
    window.update_idletasks()

    if not filePath:
        Dynamic_Island.config(text = "Fail to open this .raw image file" , bg = "AntiqueWhite1", font = ("Arial", 16), width = 80, height = 2)
        window.update_idletasks()
        return

# Haruki reset!
def reset_img():

    showProcessing()

    global filePath
    global NOW_img
    global ORIGNAL_open_img
    global ORIGNAL_PhotoImage

    NOW_img = ORIGNAL_open_img

    photo_image = ImageTk.PhotoImage(NOW_img)
    update_display_canvas(photo_image)

    nameStr = filePath.split("/")
    Dynamic_Island.config(text = f"{nameStr[-1]} resetd! It looks like opened just now!", bg = "hot pink", font = ("Arial", 14), width = 60, height = 2)
    window.update_idletasks()

# save image 
def save_img():

    showProcessing()

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
    
    showProcessing()

    NOW_img.show()
    Dynamic_Island.config(text = "Display!", bg = "green4", font = ("Arial", 16), width = 80, height = 1)
    window.update_idletasks()

# Adjust contrast/brightness of images by linearly
def lin_adj(a, b):
    global NOW_img
    new_img = NOW_img
    for i in range(NOW_img.size[0]):
        for j in range(NOW_img.size[1]):
            X = NOW_img.getpixel((i, j))  # x, y
            X = int(X * a + b)
            if X > 255:
                X = 255
            new_img.putpixel((i, j), X)
    
    NOW_img = new_img

    photo_image = ImageTk.PhotoImage(NOW_img)
    update_display_canvas(photo_image)
    #X = 1
    #global NOW_img
    #new_img = ImageEnhance.Brightness(NOW_img).enhance(a * X + b)
    #NOW_img = new_img
    #new_img = ImageTk.PhotoImage(new_img)
    #lbl_PRESENT_img.configure(image = new_img)
    #lbl_PRESENT_img.image = new_img
    global Dynamic_Island
    Dynamic_Island.config(text = "Linearly adjust!", bg = "gold", font = ("Arial", 14), width = 45, height = 2)
    window.update_idletasks()
    
# Adjust contrast/brightness of images by exponentially
def exp_adj(a, b):
    global NOW_img
    new_img = NOW_img
    for i in range(NOW_img.size[0]):
        for j in range(NOW_img.size[1]):
            X = NOW_img.getpixel((i, j))  # x, y
            X = int(math.exp(X * a + b))
            if X > 255:
                X = 255
            new_img.putpixel((i, j), X)
    
    NOW_img = new_img

    photo_image = ImageTk.PhotoImage(NOW_img)
    update_display_canvas(photo_image)
    #X = 1
    #global NOW_img
    #new_img = ImageEnhance.Brightness(NOW_img).enhance(math.exp(a * X + b))
    #NOW_img = new_img
    #new_img = ImageTk.PhotoImage(new_img)
    #lbl_PRESENT_img.configure(image = new_img)
    #lbl_PRESENT_img.image = new_img
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
    new_img = NOW_img
    for i in range(NOW_img.size[0]):
        for j in range(NOW_img.size[1]):
            X = NOW_img.getpixel((i, j))  # x, y
            X = int(math.log(X * a + b))
            if X > 255:
                X = 255
            new_img.putpixel((i, j), X)
    
    NOW_img = new_img

    photo_image = ImageTk.PhotoImage(NOW_img)
    update_display_canvas(photo_image)
    #X = 1
    #global NOW_img
    #new_img = ImageEnhance.Brightness(NOW_img).enhance(math.log(a * X + b))
    #NOW_img = new_img
    #new_img = ImageTk.PhotoImage(new_img)
    #lbl_PRESENT_img.configure(image = new_img)
    #lbl_PRESENT_img.image = new_img
    Dynamic_Island.config(text = "Logarithmically adjust!", bg = "firebrick", font = ("Arial", 14), width = 40, height = 2)
    window.update_idletasks()
    
# Zoom in and shrink
def resize_img(perc):

    showProcessing()

    global NOW_img
    new_img = NOW_img.resize((NOW_img.size[0] * perc // 100, NOW_img.size[1] * perc // 100))
    NOW_img = new_img
    new_img = ImageTk.PhotoImage(new_img)

    update_display_canvas(new_img)

    global Dynamic_Island
    Dynamic_Island.config(text = "Resize " + str(perc) + " %", bg = "DarkOrange", font = ("Arial", 14), width = 30, height = 2)
    window.update_idletasks()

# Rotate 
def rotate_img(degrees):
    global NOW_img
    new_img = NOW_img.rotate(degrees, expand = "yes")
    NOW_img = new_img
    new_img = ImageTk.PhotoImage(new_img)
    lbl_PRESENT_img.configure(image = new_img)
    lbl_PRESENT_img.image = new_img
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
    lbl_PRESENT_img.configure(image = new_img)
    lbl_PRESENT_img.image = new_img
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
    new_img = Image.new("L", (NOW_img.size[0], NOW_img.size[1]))
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

# smoothing
def smoothing():
  
    Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    window.update_idletasks()
    degree = int(entry_degree.get())
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

# sharpening
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

# median smoothing
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

# Laplacian mask
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

# log |F(u,v)|
# magnitude-only image
# phase-only image
def log_mag_pha_img():
    
    Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    window.update_idletasks()

    global NOW_img
    a = []
    for i in range(NOW_img.size[0]):
        temp = []
        for j in range(NOW_img.size[1]):
            temp.append(NOW_img.getpixel((i, j)))
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
    Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    window.update_idletasks()
    global NOW_img
    a = []
    for i in range(NOW_img.size[0]):
        temp = []
        for j in range(NOW_img.size[1]):
            if((i+j)%2==0):
                temp.append(NOW_img.getpixel((i, j)))
            else:
                temp.append(NOW_img.getpixel((i, j))*-1)
        a.append(temp)
        del temp
    step1 = numpy.array(a)
    
    step2 = numpy.fft.fft2(step1)
    step2 = numpy.fft.fftshift(step2)
    step3 = numpy.conjugate(step2)
    step4 = numpy.fft.ifftshift(step3)
    step4 = numpy.fft.ifft2(step4)
    
    step5 = step4
    for i in range(NOW_img.size[0]):
        for j in range(NOW_img.size[1]):
            if((i+j)%2==1):
                step5[i][j]*=-1
    
    fig,ax = plt.subplots(2,3)
    
    step1 = numpy.transpose(step1)
    step2 = numpy.transpose(numpy.log(numpy.abs(step2))*20)
    step3 = numpy.transpose(numpy.log(numpy.abs(step3))*20)
    step4 = numpy.transpose(numpy.log(numpy.abs(step4))*20)
    step5 = numpy.transpose(numpy.real(step5))
    ax[0, 0].title.set_text("Original image")
    ax[0, 0].imshow(NOW_img, interpolation="none",cmap="gray",vmin=0,vmax=255)
    ax[0, 1].title.set_text("Step. (1)")
    ax[0, 1].imshow(step1, interpolation="none",cmap="gray",vmin=0,vmax=255)
    ax[0, 2].title.set_text("Step. (2)")
    ax[0, 2].imshow(step2, interpolation="none",cmap="gray",vmin=0,vmax=255)
    ax[1, 0].title.set_text("Step. (3)")
    ax[1, 0].imshow(step3, interpolation="none",cmap="gray",vmin=0,vmax=255)
    ax[1, 1].title.set_text("Step. (4)")
    ax[1, 1].imshow(step4, interpolation="none",cmap="gray",vmin=0,vmax=255)
    ax[1, 2].title.set_text("Step. (5)")
    ax[1, 2].imshow(step5, interpolation="none",cmap="gray",vmin=0,vmax=255)

    Dynamic_Island.config(text = "Display Problem. 3 step.(1) - (5)", bg = "ghost white", font = ("Arial", 14), width = 80, height = 2)
    window.update_idletasks()
    #fig.canvas.set_window_title("Problem. 3")

    fig.set_figheight(8)
    fig.set_figwidth(8)
    plt.show()
            
# Red component image
def red_img():
    Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    window.update_idletasks()
    global NOW_img

    split_img = Image.Image.split(NOW_img)
    new_img = Image.new("RGB", (NOW_img.size[0], NOW_img.size[1]))
    for i in range(NOW_img.size[0]):
        for j in range(NOW_img.size[1]):
            r = split_img[0].getpixel((i, j))
            new_img.putpixel((i, j), (r, 0, 0))
            
    NOW_img = new_img
    new_img = ImageTk.PhotoImage(new_img)
    lbl_PRESENT_img.configure(image = new_img)
    lbl_PRESENT_img.image = new_img
    Dynamic_Island.config(text = "Red component image", bg = "red", font = ("Arial", 14), width = 80, height = 2)
    window.update_idletasks()

# Green component image
def green_img():
    Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    window.update_idletasks()
    global NOW_img

    split_img = Image.Image.split(NOW_img)
    new_img = Image.new("RGB", (NOW_img.size[0], NOW_img.size[1]))
    for i in range(NOW_img.size[0]):
        for j in range(NOW_img.size[1]):
            g = split_img[1].getpixel((i, j))
            new_img.putpixel((i, j), (0, g, 0))
            
    NOW_img = new_img
    new_img = ImageTk.PhotoImage(new_img)
    lbl_PRESENT_img.configure(image = new_img)
    lbl_PRESENT_img.image = new_img
    Dynamic_Island.config(text = "Green component image", bg = "green2", font = ("Arial", 14), width = 80, height = 2)
    window.update_idletasks()

# Blue component image
def blue_img():
    Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    window.update_idletasks()
    global NOW_img

    split_img = Image.Image.split(NOW_img)
    new_img = Image.new("RGB", (NOW_img.size[0], NOW_img.size[1]))
    for i in range(NOW_img.size[0]):
        for j in range(NOW_img.size[1]):
            b = split_img[2].getpixel((i, j))
            new_img.putpixel((i, j), (0, 0, b))
            
    NOW_img = new_img
    new_img = ImageTk.PhotoImage(new_img)
    lbl_PRESENT_img.configure(image = new_img)
    lbl_PRESENT_img.image = new_img
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
    Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    window.update_idletasks()
    global NOW_img

    split_img = Image.Image.split(NOW_img)
    h_img = Image.new("L", (NOW_img.size[0], NOW_img.size[1]))
    s_img = Image.new("L", (NOW_img.size[0], NOW_img.size[1]))
    i_img = Image.new("L", (NOW_img.size[0], NOW_img.size[1]))
    for i in range(NOW_img.size[0]):
        for j in range(NOW_img.size[1]):
            R = split_img[0].getpixel((i, j))
            G = split_img[1].getpixel((i, j))
            B = split_img[2].getpixel((i, j))
            H, S, I = rgb_to_hsi(R, G, B)
            h_img.putpixel((i, j), round(H/360*255))
            s_img.putpixel((i, j), round(S*255))
            i_img.putpixel((i, j), round(I))

    fig,ax = plt.subplots(1,4)
    
    ax[0].title.set_text("Original image")
    ax[0].imshow(NOW_img, interpolation="none",cmap="gray",vmin=0,vmax=255)
    ax[1].title.set_text("Hue")
    ax[1].imshow(h_img, interpolation="none",cmap="gray",vmin=0,vmax=255)
    ax[2].title.set_text("Saturation")
    ax[2].imshow(s_img, interpolation="none",cmap="gray",vmin=0,vmax=255)
    ax[3].title.set_text("Intensity")
    ax[3].imshow(i_img, interpolation="none",cmap="gray",vmin=0,vmax=255)

    Dynamic_Island.config(text = "RGB to HSI", bg = "ghost white", font = ("Arial", 14), width = 80, height = 2)
    window.update_idletasks()
    #fig.canvas.set_window_title("Problem. 3")

    fig.set_figheight(8)
    fig.set_figwidth(8)
    plt.show()

# RGB complements to enhance the detail
def rgb_complements():
    Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    window.update_idletasks()
    global NOW_img
    
    split_img = Image.Image.split(NOW_img)
    new_img = Image.new("RGB", (NOW_img.size[0], NOW_img.size[1]))
    for i in range(NOW_img.size[0]):
        for j in range(NOW_img.size[1]):
            r = split_img[0].getpixel((i, j))
            g = split_img[1].getpixel((i, j))
            b = split_img[2].getpixel((i, j))
            new_img.putpixel((i, j), (255 - r, 255 - g, 255 - b))
            
    NOW_img = new_img
    new_img = ImageTk.PhotoImage(new_img)
    lbl_PRESENT_img.configure(image = new_img)
    lbl_PRESENT_img.image = new_img
    Dynamic_Island.config(text = "RGB model color complements", bg = "ghost white", font = ("Arial", 14), width = 80, height = 2)
    window.update_idletasks()

def rgb_hsi_sharping():
    Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    window.update_idletasks()
    global NOW_img

    degree = 5

    split_img = Image.Image.split(NOW_img)
    smoothing_img = Image.new("RGB", (NOW_img.size[0], NOW_img.size[1]))
    I_smoothing_img = Image.new("RGB", (NOW_img.size[0], NOW_img.size[1]))
    # smoothing
    for i in range(NOW_img.size[0]):
        for j in range(NOW_img.size[1]):
            R_sum = 0
            G_sum = 0
            B_sum = 0
            I_sum = 0
            pixel_count = 0
            for k in range(degree*degree):
                row = i + k / degree - degree/2
                col = j + k % degree - degree/2
                if(row < 0  or  col < 0  or  row >= NOW_img.size[0]  or  col >= NOW_img.size[1]):
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
    RGB_Lap_img = Image.new("RGB", (NOW_img.size[0], NOW_img.size[1]))
    HSI_Lap_img = Image.new("RGB", (NOW_img.size[0], NOW_img.size[1]))
    split_smoothing_img = Image.Image.split(smoothing_img)
    split_I_smoothing_img = Image.Image.split(smoothing_img)
    for i in range(NOW_img.size[0]):
        for j in range(NOW_img.size[1]):
            r_sum = 0
            g_sum = 0
            b_sum = 0
            
            h_sum = 0
            s_sum = 0
            i_sum = 0
            for k in range(9):
                row = i + int(k / 3) - int(3 / 2)
                col = j + int(k % 3) - int(3 / 2)
                if(row < 0  or  col < 0  or  row >= NOW_img.size[0]  or  col >= NOW_img.size[1]):
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
    ax[0].imshow(NOW_img, interpolation="none",cmap="gray",vmin=0,vmax=255)
    ax[1].title.set_text("RGB Laplacian")
    ax[1].imshow(RGB_Lap_img, interpolation="none",cmap="gray",vmin=0,vmax=255)
    ax[2].title.set_text("HSI Laplacian")
    ax[2].imshow(HSI_Lap_img, interpolation="none",cmap="gray",vmin=0,vmax=255)

    Dynamic_Island.config(text = "RGB Laplacian and HSI Laplacian", bg = "ghost white", font = ("Arial", 14), width = 80, height = 2)
    window.update_idletasks()
    #fig.canvas.set_window_title("Problem. 3")

    fig.set_figheight(8)
    fig.set_figwidth(8)
    plt.show()

# Segmenting the feathers
def seg_fea_mask():
    
    Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    window.update_idletasks()
    global NOW_img

    split_img = Image.Image.split(NOW_img)
    feathers_img = Image.new("RGB", (NOW_img.size[0], NOW_img.size[1]))
    H_img = Image.new("L", (NOW_img.size[0], NOW_img.size[1]))
    S_img = Image.new("L", (NOW_img.size[0], NOW_img.size[1]))

    for i in range (NOW_img.size[0]):
        for j in range (NOW_img.size[1]):
            r = split_img[0].getpixel((i, j))
            g = split_img[1].getpixel((i, j))
            b = split_img[2].getpixel((i, j))
            H, S, I = rgb_to_hsi(r, g, b)
            H_img.putpixel((i, j), round(H/360*255))
            S_img.putpixel((i, j), round(S*255))
            if (325 > H > 250  and NOW_img.size[0] * 0.1 < i < NOW_img.size[0] * 0.6):
                feathers_img.putpixel((i, j), (r, g, b))
            else:
                feathers_img.putpixel((i, j), (0, 0, 0))

    fig, ax = plt.subplots(1,4)
    
    ax[0].title.set_text("Original image")
    ax[0].imshow(NOW_img, interpolation="none",cmap="gray",vmin=0,vmax=255)
    ax[1].title.set_text("Hue")
    ax[1].imshow(H_img, interpolation="none",cmap="gray",vmin=0,vmax=255)
    ax[2].title.set_text("Saturation")
    ax[2].imshow(S_img, interpolation="none",cmap="gray",vmin=0,vmax=255)
    ax[3].title.set_text("Feathers")
    ax[3].imshow(feathers_img, interpolation="none",cmap="gray",vmin=0,vmax=255)

    Dynamic_Island.config(text = "RGB Laplacian and HSI Laplacian", bg = "ghost white", font = ("Arial", 14), width = 80, height = 2)
    window.update_idletasks()
    #fig.canvas.set_window_title("Problem. 3")

    fig.set_figheight(8)
    fig.set_figwidth(8)
    plt.show()


###############################################  on the window  ###############################################

window = tk.Tk()
window.title("Basic Digital Image Processing")
Dynamic_Island = tk.Label(window, text = "Please open an image file first", bg = "gold", font = ("Arial", 16), width = 80, height = 2)


                    ######  Define component ######

        ### Canvas and scrollbars for displaying the current image

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



        ### open / save / dispaly
# Label
lbl_open = tk.Label(window, text = "First step  ========  OPEN   ====   ==   = > ",font = ("Arial", 12))
lbl_save_dispaly = tk.Label(window, text = "Please enter a file name to Save / Display the image (contain filename extenstion)",font = ("Arial", 10))
# Entry
entry_fileName = tk.Entry(window, width = 25)
# Button
btn_open = tk.Button(window, text = "Open an image", command = open_img)
btn_save = tk.Button(window, text = "Save image", command = save_img)
btn_display = tk.Button(window, text = "Display image", command = display_img)
        ### open .raw image file
btn_raw = tk.Button(window, text = "Open a .raw image", command = open_raw)
        ### Haruki reset!
btn_reset = tk.Button(window, text = "Reset current image", command = reset_img)
        ### Display the histogram of images
lbl_eql = tk.Label(window, text = "Histogram Equlization")
btn_htg = tk.Button(window, text = "Histogram of current images", command = display_htg)
btn_htg_eql = tk.Button(window, text = "Equlization", command = auto_level)

        ### Adjust contrast / brightness of images
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
    
        ### Zoom in and shrink
# Label
lbl_resize = tk.Label(window, text = "Resize the image ( ? %):")
# Entry
entry_resize = tk.Entry(window, width = 8)
# Button
btn_resize = tk.Button(window, text = "Resize", command  = lambda: resize_img(int(entry_resize.get())))

        ### Rotate  
# Label
lbl_rot = tk.Label(window, text = "Rotate the image (by degrees) :")
# Entry
entry_rot = tk.Entry(window, width = 8)
# Button
btn_rot = tk.Button(window, text = "Rotate", command = lambda: rotate_img(int(entry_rot.get())))

        ### Gray-level slicing
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
btn_slc = tk.Button(window, text = "Slice", command = lambda: gray_lvl_slc(int(entry_lowerbound.get()), int(entry_upperbound.get()), if_prs_btn))
btn_if_prs = tk.Button(window, textvariable = if_prs_text, command = prs_change)

        ### Bit-plane image
# Label
lbl_bit_plane = tk.Label(window, text = "Bit-plane image ( Please enter a number (1 - 7) ):")
# Entry
entry_bit_plane = tk.Entry(window, width = 8)
# Button
btn_bit_plane = tk.Button(window, text = "Slice", command = bit_plane)

        ### [Spatial Filters] smoothing / sharpening / median filter / Laplacian mask
# Label
lbl_spt_flt = tk.Label(window, text = "Spatial Filters (degree) :")
# Entry
entry_degree = tk.Entry(window, width = 8)
# Button
btn_smt = tk.Button(window, text = "Arithmetic mean smoothing", command = smoothing)
btn_shp = tk.Button(window, text = "Sharpening", command = sharpening)
btn_med = tk.Button(window, text = "Median", command = median)
btn_lpl = tk.Button(window, text = "Laplacian", command = Laplacian)

        ### log |F(u,v)|  &  Magnitude and Phase images
# Label
lbl_log_mag_pha_img = tk.Label(window, text = "2D FFT:")
# Button
btn_log_mag_pha_img = tk.Button(window, text = "do", command = log_mag_pha_img)

        ### 3. step. (1) - (5)
    ## Multiplying the image by (-1)^(x+y)
    ## Computing the DFT
    ## Taking the complex conjugate of the transform
    ## Computing the inverse DFT
    ## Multiplying the real part of the result by (-1)^(x+y)
# Label
lbl_step1_5 = tk.Label(window, text = "(DFT) Step.(1) - (5) :")
# Button
btn_step1_5 = tk.Button(window, text = "do", command = step1_5)

        ### 4. (b) - (f)
    ## Component image
# Label
lbl_com_img = tk.Label(window, text = "Component image :")
# Button
btn_red_img = tk.Button(window, text = "Red", command = red_img)
btn_green_img = tk.Button(window, text = "Green", command = green_img)
btn_blue_img = tk.Button(window, text = "Blue", command = blue_img)
    ## Convert RGB to HSI model ,and display its Hue, Saturation, and Intensity components as gray-level images respectively.
# Label
lbl_RGB_to_HSI = tk.Label(window, text = "Convert RGB to HSI :")
# Button
btn_RGB_to_HSI = tk.Button(window, text = "do", command = rgb_to_h_s_i_subplot)
    ## Do color complements by using RGB model
# Label
lbl_rgb_cpm = tk.Label(window, text = "RGB color complements (Enhance the detail) :")
# Button
btn_rgb_cpm = tk.Button(window, text = "do", command = rgb_complements)

    ## Sharping with the Laplacian to this image by using RGB and HSI models
# Label
lbl_rgb_hsi_sharping = tk.Label(window, text = "Sharping with the Laplacian to this image by using RGB and HSI models :")
# Button
btn_rgb_hsi_sharping = tk.Button(window, text = "do ", command = rgb_hsi_sharping)
    ## segmenting the feathers
lbl_seg_fea = tk.Label(window, text = "Segmenting the feathers")
# Button
btn_seg_fea = tk.Button(window, text = "do", command = seg_fea_mask)

                    ######  composition  ######
# Heading
Dynamic_Island.grid(row = 0, column = 0, columnspan = 15, rowspan = 1)
# Open / Save / Dispaly
lbl_open.grid(row = 1, column = 0)
btn_open.grid(row = 1, column = 1)
lbl_save_dispaly.grid(row = 3, column = 0)
entry_fileName.grid(row = 4, column = 0)
btn_save.grid(row = 4, column = 1)
btn_display.grid(row = 4, column = 2)
# open .raw image file
btn_raw.grid(row = 1, column = 2)
# Haruki reset!
btn_reset.grid(row = 2, column = 1)
# Display the histogram of images
btn_htg.grid(row = 2, column = 2)                                     
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
# Histogram equlization
lbl_eql.grid(row = 10, column = 0)
btn_htg_eql.grid(row = 10, column = 1)
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
# log |F(u,v)|  &  Magnitude and Phase images
lbl_log_mag_pha_img.grid(row = 13, column = 0)
btn_log_mag_pha_img.grid(row = 13, column = 1)
# 3. step. (1) - (5)
lbl_step1_5.grid(row = 15, column = 0)
btn_step1_5.grid(row = 15, column = 1)
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


window.mainloop()