import math
from math import cos, radians , degrees , acos,sqrt
import tkinter as tk
from tkinter import filedialog
import PIL
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import os
import sheep
import shineWu

def open_watermark_img():
    Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    window.update_idletasks()
    global WATERMARK
    fileName = filedialog.askopenfilename()
    WATERMARK = Image.open(fileName)
    nameStr = fileName.split("/")
    Dynamic_Island.config(text = "You open this image: " + nameStr[-1] , bg = "AntiqueWhite1", font = ("Arial", 16), width = 80, height = 2)
    
    # NOW_img.show()
    WATERMARK.show()

    # fig,ax = plt.subplots()
    # ax.title.set_text("Watermark")
    # ax.imshow(WATERMARK, interpolation="none",cmap="gray",vmin=0,vmax=255)
    # fig.set_figheight(5)
    # fig.set_figwidth(5)
    # plt.show()

    window.update_idletasks()

    return WATERMARK

def open_black_img():
    Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    window.update_idletasks()
    global BLACK_img
    fileName = filedialog.askopenfilename()
    BLACK_img = Image.open(fileName)
    nameStr = fileName.split("/")
    Dynamic_Island.config(text = "Your image2: " + nameStr[-1] , bg = "AntiqueWhite1", font = ("Arial", 16), width = 80, height = 2)
    BLACK_img.show()

    # fig,ax = plt.subplots()
    # ax.title.set_text("Image2")
    # ax.imshow(BLACK_img, interpolation="none",cmap="gray",vmin=0,vmax=255)
    # fig.set_figheight(5)
    # fig.set_figwidth(5)
    # plt.show()
    # window.update_idletasks()

    return BLACK_img

def open_white_img():
    Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    window.update_idletasks()
    global WHITE_img
    fileName = filedialog.askopenfilename()
    WHITE_img = Image.open(fileName)
    nameStr = fileName.split("/")
    Dynamic_Island.config(text = "Your image1: " + nameStr[-1] , bg = "AntiqueWhite1", font = ("Arial", 16), width = 80, height = 2)
    WHITE_img.show()

    # fig,ax = plt.subplots()
    # ax.title.set_text("Image1")
    # ax.imshow(WHITE_img, interpolation="none",cmap="gray",vmin=0,vmax=255)
    # fig.set_figheight(5)
    # fig.set_figwidth(5)
    # plt.show()
    # window.update_idletasks()

    window.update_idletasks()

    return WHITE_img
# Haruki reset!
def reset_img():

    Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    global fileName
    window.update_idletasks()
 
    global NOW_img
    global ORIGNAL_open_img
    NOW_img = ORIGNAL_open_img
    NOW_img.show()
    
    # fig,ax = plt.subplots()
    # fig.canvas.manager.set_window_title('Current image')
    # ax.imshow(NOW_img, interpolation="none",cmap="gray",vmin=0,vmax=255)
    # fig.set_figheight(5)
    # fig.set_figwidth(5)
    # plt.show()


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

    fileName = filedialog.askopenfilename(title = "Select an image file",)
    ORIGNAL_open_img = Image.open(fileName)
    NOW_img = ORIGNAL_open_img.copy()
    ORIGNAL_img = ImageTk.PhotoImage(ORIGNAL_open_img)
    image = PIL.Image.open(fileName)
    nameStr = fileName.split("/")
    Dynamic_Island.config(text = "You open this image: " + nameStr[-1] , bg = "AntiqueWhite1", font = ("Arial", 16), width = 80, height = 2)
    NOW_img.show()
    
    # fig,ax = plt.subplots()
    # fig.canvas.manager.set_window_title('Current image')
    # ax.imshow(NOW_img, interpolation="none",cmap="gray",vmin=0,vmax=255)
    # fig.set_figheight(5)
    # fig.set_figwidth(5)
    # plt.show()

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

    fileName = filedialog.askopenfilename(title = "Select a .raw image file",)
    x = open(fileName,'rb')
    ORIGNAL_open_img = Image.frombytes("L", (512, 512), x.read(), 'raw')
    NOW_img = ORIGNAL_open_img
    ORIGNAL_img = ImageTk.PhotoImage(ORIGNAL_open_img)
    NOW_img.show()
    
    # fig,ax = plt.subplots()
    # fig.canvas.manager.set_window_title('Current image')
    # ax.imshow(NOW_img, interpolation="none",cmap="gray",vmin=0,vmax=255)
    # fig.set_figheight(5)
    # fig.set_figwidth(5)
    # plt.show()

    nameStr = fileName.split("/")
    Dynamic_Island.config(text = "You open this .raw file: " + nameStr[-1] , bg = "AntiqueWhite1", font = ("Arial", 16), width = 80, height = 2)
    window.update_idletasks()
    if not fileName:
        Dynamic_Island.config(text = "Fail to open this .raw file" , bg = "AntiqueWhite1", font = ("Arial", 16), width = 80, height = 2)
        window.update_idletasks()
        return
    
# display image
def display_img():
    
    Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    window.update_idletasks()
    NOW_img.show()
    Dynamic_Island.config(text = "Display!", bg = "aquamarine", font = ("Arial", 16), width = 80, height = 1)
    window.update_idletasks()

def make_lowpass_watermark(NOW_img, WATERMARK):
    global put_WATERMARK
    put_WATERMARK = sheep.lowpass_watermark(NOW_img, WATERMARK, (0, 0))

# save image 
def save_img():

    Dynamic_Island.config(text = "Processing ...", bg = "green3", font = ("Arial", 14), width = 30, height = 1)
    window.update_idletasks()
    newName = entry_fileName.get()
    NOW_img.save(newName)
    Dynamic_Island.config(text = "The image has been saved! Please check your folder!", bg = "aquamarine", font = ("Arial", 16), width = 80, height = 2)

    window.update_idletasks()

def make_camouflage_img_generater(WHITE_img, BLACK_img):
    global NOW_img

    r1 = int(entry_img1_r.get())
    g1 = int(entry_img1_g.get())
    b1 = int(entry_img1_b.get())
    a1 = float(entry_img1_a.get())
    rgba_img1 = (r1, g1, b1, a1)

    r2 = int(entry_img2_r.get())
    g2 = int(entry_img2_g.get())
    b2 = int(entry_img2_b.get())
    a2 = float(entry_img2_a.get())
    rgba_img2 = (r2, g2, b2, a2)

    scale_x = int(entry_scale_x.get())
    scale_y = int(entry_scale_y.get())
    scale = (scale_x, scale_y)

    img1_x = int(entry_img1_x.get())
    img1_y = int(entry_img1_y.get())
    img2_x = int(entry_img1_x.get())
    img2_y = int(entry_img1_y.get())
    img1_position = (img1_x, img1_y)
    img2_position = (img2_x, img2_y)

    slic_x1 = int(entry_slice_x1.get())
    slic_y1 = int(entry_slice_y1.get())
    slic_x2 = int(entry_slice_x2.get())
    slic_y2 = int(entry_slice_y2.get())
    slic = ((slic_x1, slic_y1), (slic_x2, slic_y2))

    NOW_img = sheep.camouflage_img_generater(WHITE_img, BLACK_img, rgba_img1, rgba_img2, scale, img1_position, img2_position, slic)
    NOW_img.show()
    # fig,ax = plt.subplots()
    # fig.canvas.manager.set_window_title('Current image')
    # ax.imshow(NOW_img, interpolation="none",cmap="gray",vmin=0,vmax=255)
    # fig.set_figheight(5)
    # fig.set_figwidth(5)
    # plt.show()
    # window.update_idletasks()

def make_color_block(setr=0, setg=0, setb=0, depth=0):
    global NOW_img
    rimg, gimg, bimg = shineWu.imgtoarr(NOW_img)
    x = int(entry_x.get())
    y = int(entry_y.get())
    rang = float(entry_range.get())
    setr, setg, setb = sheep.color_wheel()
    r, g, b = shineWu.colorblocks(rimg, gimg, bimg ,x, y, rang, setr, setg, setb, depth)
    NOW_img = shineWu.arrtoimg(r, g, b, NOW_img)
    NOW_img.show()
    
    # fig,ax = plt.subplots()
    # fig.canvas.manager.set_window_title('Current image')
    # ax.imshow(NOW_img, interpolation="none",cmap="gray",vmin=0,vmax=255)
    # fig.set_figheight(5)
    # fig.set_figwidth(5)
    # plt.show()

def using_draw_watermark():
    global WATERMARK
    WATERMARK = sheep.draw_watermark(500, 500, 5)

def fill_img1_RGB():

    global r1, g1, b1
    r, g, b = sheep.color_wheel()
    r1.set(r)
    g1.set(g)
    b1.set(b)

def fill_img2_RGB():

    global r2, g2, b2
    r, g, b = sheep.color_wheel()
    r2.set(r)
    g2.set(g)
    b2.set(b)

def use_rgb_comp():
    global NOW_img
    NOW_img = sheep.negative(NOW_img)
    NOW_img.show()

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
            H = math.degrees(acos((r-g/2-b/2)/sqrt(r**2+g**2+b**2-g*b-r*g-r*b)))
        except:
            H = 0
    else:
        try:
            H = 360 - math.degrees(acos((r-g/2-b/2)/sqrt(r**2+g**2+b**2-g*b-r*g-r*b)))
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

def use_rgb_smooth():
    global NOW_img
    
    degree = int(entry_degree.get())
    split_img = Image.Image.split(NOW_img)
    smoothing_img = Image.new("RGB", (NOW_img.size[0], NOW_img.size[1]))
    for i in range(NOW_img.size[0]):
        for j in range(NOW_img.size[1]):
            R_sum = 0
            G_sum = 0
            B_sum = 0
            pixel_count = 0
            for k in range(degree*degree):
                row = i + k / degree - degree/2
                col = j + k % degree - degree/2
                if(row < 0  or  col < 0  or  row >= NOW_img.size[0]  or  col >= NOW_img.size[1]):
                    continue
                R_sum += split_img[0].getpixel((row,col))
                G_sum += split_img[1].getpixel((row,col))
                B_sum += split_img[2].getpixel((row,col))
                pixel_count += 1
            if (pixel_count == 0):
                pixel_count = 1
            smoothing_img.putpixel((i, j), (round(R_sum/pixel_count), round(G_sum/pixel_count), round(B_sum/pixel_count)))
    NOW_img = smoothing_img
    NOW_img.show()
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
    fig.set_figwidth(12)
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
    NOW_img.show()
    new_img = ImageTk.PhotoImage(new_img)
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
    NOW_img.show()
    new_img = ImageTk.PhotoImage(new_img)
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
    NOW_img.show()
    new_img = ImageTk.PhotoImage(new_img)
    Dynamic_Island.config(text = "Blue component image", bg = "blue", font = ("Arial", 14), width = 80, height = 2)
    window.update_idletasks()

###############################################  on the window  ###############################################

window = tk.Tk()


window.title("<< Final Project >>")
Dynamic_Island = tk.Label(window, text = "Please open an image first", bg = "gold", font = ("Arial", 16), width = 80, height = 2)

                    ######  Define  ######
        ### ========================
lbl___0_ = tk.Label(window, text = "==============================")
lbl___1_ = tk.Label(window, text = "==============================")
lbl___2_ = tk.Label(window, text = "==============================")
lbl___3_ = tk.Label(window, text = "==============================")
lbl___4_ = tk.Label(window, text = "==============================")
lbl___5_ = tk.Label(window, text = "==============================")
lbl___6_ = tk.Label(window, text = "==============================")
        ### open / save / dispaly   ### open .raw file  ### Haruki reset!
# Label
# Entry
# Button
btn_open = tk.Button(window, text = "Open", command = open_img)
btn_raw = tk.Button(window, text = "Open .raw", command = open_raw)
btn_reset = tk.Button(window, text = "Reset", command = reset_img)
btn_display = tk.Button(window, text = "Display", command = display_img)
entry_fileName = tk.Entry(window, width = 15)
btn_save = tk.Button(window, text = "Save", command = save_img)
        ### Watermark
# Label
lbl_watermark = tk.Label(window, text = "Add a watermark : ")
# Button
NOW_img = Image.open(os.path.join("Image samples\Color image\Lenna_512_color.tif"))
WATERMARK = Image.open(os.path.join("Image samples\Color image\Color wheel\color_wheel.png"))
put_WATERMARK = Image.open(os.path.join("Image samples\Color image\Color wheel\color_wheel.png"))
btn_cho_watermark = tk.Button(window, text = "Choice", command = open_watermark_img)
btn_draw_watermark = tk.Button(window, text = "Draw", command = using_draw_watermark)
btn_watermark = tk.Button(window, text = "Add", command = lambda: make_lowpass_watermark(NOW_img, WATERMARK))
btn_slice = tk.Button(window, text = "Check", command = lambda: sheep.bit_plane_slic(put_WATERMARK, 0))
        ### Black and white overlay
# Label
lbl_overlay = tk.Label(window, text = "Overlay two images: ")
lbl_img1_rgba = tk.Label(window, text = "Image1 [ R ] [ G ] [ B ] [ A ] : ")
lbl_img2_rgba = tk.Label(window, text = "Image2 [ R ] [ G ] [ B ] [ A ] : ")
lbl_scale = tk.Label(window, text = "Image size to use [ x ] x [ y ] : ")
lbl_img1_position = tk.Label(window, text = "Image1 position ([ x ], [ y ]) : ")
lbl_img2_position = tk.Label(window, text = "Image2 position ([ x ], [ y ]) : ")
lbl_slice = tk.Label(window, text = "Overlay from ([ x1 ], [ y1 ]) to ([ x2 ], [ y2 ]) : ")
# Entry
global r1, g1, b1
r1 = tk.IntVar()
g1 = tk.IntVar()
b1 = tk.IntVar()
r1.set(0)
g1.set(0)
b1.set(0)
entry_img1_r = tk.Entry(window, width = 5, textvariable = r1)
entry_img1_g = tk.Entry(window, width = 5, textvariable = g1)
entry_img1_b = tk.Entry(window, width = 5, textvariable = b1)
entry_img1_a = tk.Entry(window, width = 5)

global r2, g2, b2
r2 = tk.IntVar()
g2 = tk.IntVar()
b2 = tk.IntVar()
r2.set(0)
g2.set(0)
b2.set(0)
entry_img2_r = tk.Entry(window, width = 5, textvariable = r2)
entry_img2_g = tk.Entry(window, width = 5, textvariable = g2)
entry_img2_b = tk.Entry(window, width = 5, textvariable = b2)
entry_img2_a = tk.Entry(window, width = 5)

entry_scale_x = tk.Entry(window, width = 5)
entry_scale_y = tk.Entry(window, width = 5)

entry_img1_x = tk.Entry(window, width = 5)
entry_img1_y = tk.Entry(window, width = 5)
entry_img2_x = tk.Entry(window, width = 5)
entry_img2_y = tk.Entry(window, width = 5)

entry_slice_x1 = tk.Entry(window, width = 5)
entry_slice_y1 = tk.Entry(window, width = 5)
entry_slice_x2 = tk.Entry(window, width = 5)
entry_slice_y2 = tk.Entry(window, width = 5)
# Button
WHITE_img = Image.open(os.path.join("Image samples\Color image\Color wheel\color_wheel.png"))
BLACK_img = Image.open(os.path.join("Image samples\Color image\Color wheel\color_wheel.png"))
btn_white_img = tk.Button(window, text = "Image1", command = open_white_img)
btn_black_img = tk.Button(window, text = "Image2", command = open_black_img)
btn_overlay_img = tk.Button(window, text = "Overlay", command = lambda: make_camouflage_img_generater(WHITE_img, BLACK_img))
btn_img1_rgb = tk.Button(window, text = "RGB color wheel", command = fill_img1_RGB)
btn_img2_rgb = tk.Button(window, text = "RGB color wheel", command = fill_img2_RGB)
        ### Color block
# Label
lbl_block = tk.Label(window, text = "Color block [ x ] [ y ] Difference: [  ]%: ")
# Entry
entry_x = tk.Entry(window, width = 5)
entry_y = tk.Entry(window, width = 5)
entry_range = tk.Entry(window, width = 5)
# Button
btn_block = tk.Button(window, text = "Color", command = make_color_block)
        ### RGB negative
lbl_n_rgb = tk.Label(window, text = "RGB complement : ")
btn_n_rgb = tk.Button(window, text = "Do", command = use_rgb_comp)
        ### RGB smoothing
lbl_rgb_smo = tk.Label(window, text = "RGB soothing [ degree ] : ")
entry_degree = tk.Entry(window, width = 5)
btn_rgb_smo = tk.Button(window, text = "Do", command = use_rgb_smooth)
    ## Convert RGB to HSI model ,and display its Hue, Saturation, and Intensity components as gray-level images respectively.
# Label
lbl_RGB_to_HSI = tk.Label(window, text = "Convert RGB to HSI :")
# Button
btn_RGB_to_HSI = tk.Button(window, text = "Do", command = rgb_to_h_s_i_subplot)
    ## Component image
# Label
lbl_com_img = tk.Label(window, text = "Component image :")
# Button
btn_red_img = tk.Button(window, text = "Red", command = red_img)
btn_green_img = tk.Button(window, text = "Green", command = green_img)
btn_blue_img = tk.Button(window, text = "Blue", command = blue_img)

                    ######  composition  ######
### Heading
Dynamic_Island.grid(row = 0, column = 0, columnspan = 100, rowspan = 1)
### [Open]  [Open .raw]  [Reset]  [Dispaly]
btn_open.grid(row = 1, column = 0)
btn_raw.grid(row = 1, column = 1)
btn_reset.grid(row = 1, column = 2)
btn_display.grid(row = 1, column = 3)
entry_fileName.grid(row = 1, column = 4)
btn_save.grid(row = 1, column = 5)
### Watermark
lbl___0_.grid(row = 2, column = 0)
lbl_watermark.grid(row = 3, column = 0)
btn_cho_watermark.grid(row = 3, column = 1)
btn_draw_watermark.grid(row = 3, column = 2)
btn_watermark.grid(row = 3, column = 3)
btn_slice.grid(row = 3, column = 4)
### Black and white overlay
lbl___1_.grid(row = 4, column = 0)
lbl_overlay.grid(row = 5, column = 0)
btn_white_img.grid(row = 5, column = 1)
btn_black_img.grid(row = 5, column = 2)
btn_overlay_img.grid(row = 5, column = 3)

lbl_img1_rgba.grid(row = 7, column = 0)
entry_img1_r.grid(row = 7, column = 1)
entry_img1_g.grid(row = 7, column = 2)
entry_img1_b.grid(row = 7, column = 3)
btn_img1_rgb.grid(row = 7, column = 4)
entry_img1_a.grid(row = 7, column = 5)

lbl_img2_rgba.grid(row = 9, column = 0)
entry_img2_r.grid(row = 9, column = 1)
entry_img2_g.grid(row = 9, column = 2)
entry_img2_b.grid(row = 9, column = 3)
btn_img2_rgb.grid(row = 9, column = 4)
entry_img2_a.grid(row = 9, column = 5)

lbl_scale.grid(row = 11, column = 0)
entry_scale_x.grid(row = 11, column = 1)
entry_scale_y.grid(row = 11, column = 2)

lbl_img1_position.grid(row = 13, column = 0)
entry_img1_x.grid(row = 13, column = 1)
entry_img1_y.grid(row = 13, column = 2)

lbl_img2_position.grid(row = 15, column = 0)
entry_img2_x.grid(row = 15, column = 1)
entry_img2_y.grid(row = 15, column = 2)

lbl_slice.grid(row = 17, column = 0)
entry_slice_x1.grid(row = 17, column = 1)
entry_slice_y1.grid(row = 17, column = 2)
entry_slice_x2.grid(row = 17, column = 3)
entry_slice_y2.grid(row = 17, column = 4)
### Color block
lbl___2_.grid(row = 18, column = 0)
lbl_block.grid(row = 19, column = 0)
entry_x.grid(row = 19, column = 1)
entry_y.grid(row = 19, column = 2)
entry_range.grid(row = 19, column = 3)
btn_block.grid(row = 19, column = 4)
### RGB smoothing
lbl___4_.grid(row = 20, column = 0)
lbl_rgb_smo.grid(row = 21, column = 0)
entry_degree.grid(row = 21, column = 1)
btn_rgb_smo.grid(row = 21, column = 2)
### RGB negative
lbl___3_.grid(row = 22, column = 0)
lbl_n_rgb.grid(row = 23, column = 0)
btn_n_rgb.grid(row = 23, column = 1)
### Convert RGB to HSI model ,and display its Hue, Saturation, and Intensity components as gray-level images respectively.
lbl___5_.grid(row = 24, column = 0)
lbl_RGB_to_HSI.grid(row = 25, column = 0)
btn_RGB_to_HSI.grid(row = 25, column = 1)
### Convert RGB to HSI model ,and display its Hue, Saturation, and Intensity components as gray-level images respectively.
lbl___6_.grid(row = 26, column = 0)
lbl_com_img.grid(row = 27, column = 0)
btn_red_img.grid(row = 27, column = 1)
btn_green_img.grid(row = 27, column = 2)
btn_blue_img.grid(row = 27, column = 3)

window.geometry("900x600")
window.mainloop()