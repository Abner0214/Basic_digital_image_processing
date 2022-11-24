import PIL
import tkinter
from tkinter import filedialog
from PIL import Image,ImageTk,ImageEnhance,ImageOps
import os
import math
from  matplotlib import pyplot

my_window = tkinter.Tk()
my_window.title('B103040051 dip hw2')
my_window.geometry("1200x700+50+20")


ori_img_import = Image.open(os.path.join(r'c:\Users\User\OneDrive\桌面\數位影像處理\hw2\B103040003_HW2\elaine.512.tiff'))
ori_img = ImageTk.PhotoImage(ori_img_import)
now_img = ori_img_import


#照片
photo_panel = tkinter.Label(my_window,image = ori_img,height=300,width=300)
photo_panel.image = ori_img

#文字
#   上排訊息
message_up_text_var = tkinter.StringVar()
message_up_text_var.set('Welcome to the best image app in the world!')
message_up = tkinter.Label(my_window,textvariable= message_up_text_var)
#   亮度ab
label_title = tkinter.Label(my_window,text = 'Birghtness Enhance')
label_a = tkinter.Label(my_window,text = 'a :')
label_b = tkinter.Label(my_window,text = 'b :')
#   rot
label_rot_title = tkinter.Label(my_window,text = 'Rotation')
label_rot = tkinter.Label(my_window,text = 'deg :')
#   size
label_resize_title = tkinter.Label(my_window,text = 'Resize')
label_resize = tkinter.Label(my_window,text = 'persent :')
#   gray lvl
label_gray_up  = tkinter.Label(my_window,text = 'UpperBound :')
label_gray_low = tkinter.Label(my_window,text = 'LowerBound :')
label_gray_title = tkinter.Label(my_window,text = 'Gray Level Slicing')
label_gray_preserve = tkinter.Label(my_window,text = 'Preserve :')
#   save
label_save_title = tkinter.Label(my_window,text = 'Save File')
label_save_name = tkinter.Label(my_window,text = 'Name : ')
label_save_type = tkinter.Label(my_window,text = 'Type : ')
#   bit plane
label_bit_title = tkinter.Label(my_window,text = 'Bit Plane Slicing')
label_bit_bit = tkinter.Label(my_window,text = 'Bit: ')
#   show histogram
label_his_title = tkinter.Label(my_window,text = 'Histogram')
label_his_show = tkinter.Label(my_window,text = 'Show Histogram :')
label_his_equal = tkinter.Label(my_window,text = 'HIST Equalization :')
#   filter
label_filter_title= tkinter.Label(my_window,text = 'Filter')
label_filter_degree= tkinter.Label(my_window,text = 'degree/k:')

#亮度調整：函式
def brightness_lin(fun_a,fun_b):
    message_up_text_var.set('processing...')
    global now_img
    new_img = Image.new("L", (now_img.size[0], now_img.size[1]))
    for i in range(now_img.size[0]):
        for j in range(now_img.size[1]):
            val = now_img.getpixel((i, j))#x,y
            val = fun_a*val + fun_b
            if(val>255):
                val = 255
            val = int(val)
            new_img.putpixel((i, j), val)
    now_img = new_img
    new_img = ImageTk.PhotoImage(new_img)
    photo_panel.configure(image=new_img)
    photo_panel.image = new_img
    my_window.update_idletasks()
    message_up_text_var.set('[linear] Done!')
    
def brightness_exp(fun_a,fun_b):
    message_up_text_var.set('processing...')
    global now_img
    new_img = Image.new("L", (now_img.size[0], now_img.size[1]))
    for i in range(now_img.size[0]):
        for j in range(now_img.size[1]):
            val = now_img.getpixel((i, j))#x,y
#            print(val)
            if(fun_a*val>6 or fun_b>6):
                val = 255
            else:
                val = math.exp(fun_a*val + fun_b)
                if(val>255):
                    val = 255
            val = int(val)
            new_img.putpixel((i, j), val)
#    print("hello")
    now_img = new_img
    new_img = ImageTk.PhotoImage(new_img)
    photo_panel.configure(image=new_img)
    photo_panel.image = new_img
    my_window.update_idletasks()
    message_up_text_var.set('[exponential] Done!')
def brightness_log(fun_a,fun_b):
    if(fun_b<=1):
        message_up_text_var.set("[Error]:b must > 1 !")
        print("[Error]:b must > 1 !")
        return
    message_up_text_var.set('processing...')
    global now_img
    new_img = Image.new("L", (now_img.size[0], now_img.size[1]))
    for i in range(now_img.size[0]):
        for j in range(now_img.size[1]):
            val = now_img.getpixel((i, j))#x,y
            val = math.log(fun_a*val + fun_b)
            if(val>255):
                val = 255
            val = int(val)
            new_img.putpixel((i, j), val)
    now_img = new_img
    new_img = ImageTk.PhotoImage(new_img)
    photo_panel.configure(image=new_img)
    photo_panel.image = new_img
    my_window.update_idletasks()
    message_up_text_var.set('[logarithmical] Done!')
    
def resize(perc, resample = Image.Resampling.BILINEAR):
    global now_img    
    new_img =  now_img.resize((now_img.size[0] * perc // 100, now_img.size[1] * perc // 100), resample)
    now_img=new_img
    new_img = ImageTk.PhotoImage(new_img)
    photo_panel.configure(image=new_img)
    photo_panel.image = new_img
    my_window.update_idletasks()
def my_rotate(degree):
    global now_img    
    new_img =  now_img.rotate(degree,Image.Resampling.BILINEAR)
    now_img=new_img
    new_img = ImageTk.PhotoImage(new_img)
    photo_panel.configure(image=new_img)
    photo_panel.image = new_img
    my_window.update_idletasks()
#show_iamge
def show_img():
    message_up_text_var.set("I can show you the image. Shining, shimmering, splendid")
    now_img.show()
def re_set():
    global now_img
    now_img = ori_img_import
    photo_panel.configure(image=ori_img)
    photo_panel.image = ori_img
    my_window.update_idletasks()
    message_up_text_var.set("Reseted, everything back to original")
def gray_lvl_slic(lowerbound,upperbound,keep = True):
    message_up_text_var.set('processing...')
    global now_img
    new_img = Image.new("L", (now_img.size[0], now_img.size[1]))
    count = 0
    size = now_img.size[0]*now_img.size[1]
    for i in range(now_img.size[0]):
        for j in range(now_img.size[1]):
            val = now_img.getpixel((i, j))#x,y
            if(val >= lowerbound and val <= upperbound):
                val = 255
                count+=1
            elif(not keep):
                val = 0
            new_img.putpixel((i, j), val)
    now_img = new_img
    new_img = ImageTk.PhotoImage(new_img)
    photo_panel.configure(image=new_img)
    photo_panel.image = new_img
    my_window.update_idletasks()
    if(count==0):
        message_up_text_var.set('Gray level slicing completed...who truned the lights off?')
    elif(count>=size):
        message_up_text_var.set('Gray level slicing compl...OH GoD!MY eYEs ! iT\'S AlL wHIiTe AND I AM BLINDED, HEEELP!!!')
    else:
        message_up_text_var.set('Gray level slicing completed,it looks nice')
def preserve_change():
    global buton_ret_if_preserve
    global preserve_var
    buton_ret_if_preserve = not buton_ret_if_preserve
    if(buton_ret_if_preserve):
        preserve_var.set('Yes')
    else:
        preserve_var.set("NO")
def file_type_change():
    global if_file_type_jpg
    global save_file_var
    if_file_type_jpg = not if_file_type_jpg
    if(if_file_type_jpg):
        save_file_var.set('png')
    else:
        save_file_var.set("tiff")
def save_file(name,type):
    if(name==""):
        message_up_text_var.set("[ERROR] NULL name, please type something")
        return
    now_img.save(name+"."+type,type)
    message_up_text_var.set("File saved succefully, can my gpa be succefully saved?")
def open_img():
        global filename,ori_img,now_img,ori_img_import
        filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Image","*.jpg*"),("Image","*.tif*"),("Image","*.JPEG*")))
#        if(filename!="*jpg" or filename!="*tif"):
#            message_up_text_var.set("[Error]:must jpg or JPEG or tif!")
#            return
        if not filename:
            message_up_text_var.set("[Error]:file path is empty!")
            return
        ori_img_import = Image.open(filename)
        ori_img = ImageTk.PhotoImage(ori_img_import)
        now_img = ori_img_import
        photo_panel.configure(image=ori_img)
        photo_panel.image = ori_img
        my_window.update_idletasks()
def bit_plane_slic(plane):
    message_up_text_var.set('processing...')
    global now_img
    new_img = Image.new("L", (now_img.size[0], now_img.size[1]))
    for i in range(now_img.size[0]):
        for j in range(now_img.size[1]):
            temp = plane
            val = now_img.getpixel((i, j))#x,y
            while(temp>0):
                val//=2
                temp-=1
            if(val%2==1):
                val = 255
            else:
                val = 0
            new_img.putpixel((i, j), val)
    now_img = new_img
    new_img = ImageTk.PhotoImage(new_img)
    photo_panel.configure(image=new_img)
    photo_panel.image = new_img
    my_window.update_idletasks()
def historgram():
    global now_img
    name = list(range(0,256))
    val = [0 for x in range(256)]
    for i in range(now_img.size[0]):
        for j in range(now_img.size[1]):
            val[now_img.getpixel((i, j))]+=1
    pyplot.bar(name,val,width=0.25)
    pyplot.title("Gray level")
    message_up_text_var.set("Histogram showed, it's too long too much...I mean data")
    pyplot.show()
def equal():
    message_up_text_var.set('processing...')
    global now_img
    val = [0 for x in range(256)]#store the numbers of gray level
    for i in range(now_img.size[0]):#couont the numbers
        for j in range(now_img.size[1]):
            val[now_img.getpixel((i, j))]+=1
    size = now_img.size[0]*now_img.size[1]
    appearate = [x/size for x in val]#store the rate of gray level
    sumrate = []#store the sum_rate of gary level and multipy 255 the round it, which presents what gray level the new image should be
    sumnow = 0
    for i in range(256):#count sum rate part
        sumnow+=appearate[i]
        sumrate.append(round(sumnow*255))
    new_img = Image.new("L", (now_img.size[0], now_img.size[1]))
    for i in range(now_img.size[0]):#put pixel
        for j in range(now_img.size[1]):
            val = now_img.getpixel((i, j))
            new_img.putpixel((i, j), sumrate[val])
    now_img = new_img
    new_img = ImageTk.PhotoImage(new_img)
    photo_panel.configure(image=new_img)
    photo_panel.image = new_img
    message_up_text_var.set('All pixel are created equal')
    my_window.update_idletasks() 
def smoothing(degree):
    """
    also equal average filtering
    """
    message_up_text_var.set('processing...')
    global now_img
    new_img = Image.new("L", (now_img.size[0], now_img.size[1]))
    for i in range(now_img.size[0]):
        for j in range(now_img.size[1]):
            sum_pixel = 0
            sum_num = 0
            for k in range(degree*degree):
                row = i + int(k/degree) - int(degree/2)
                col = j + int(k%degree) - int(degree/2)
                if(row<0 or col<0 or row>=now_img.size[0] or col>=now_img.size[1]):
                    continue
                sum_pixel+= now_img.getpixel((row,col))
                sum_num+=1
            new_img.putpixel((i, j), round(sum_pixel/sum_num))
    now_img = new_img
    new_img = ImageTk.PhotoImage(new_img)
    photo_panel.configure(image=new_img)
    photo_panel.image = new_img
    message_up_text_var.set('very smooth')
    my_window.update_idletasks()
def Laplacian(if_in_function=False):
    message_up_text_var.set('processing...')
    global now_img
    new_img = Image.new("L", (now_img.size[0], now_img.size[1]))
    for i in range(now_img.size[0]):
        for j in range(now_img.size[1]):
            sum_pixel = 0
            for k in range(9):
                row = i + int(k/3) - int(3/2)
                col = j + int(k%3) - int(3/2)
                if(row<0 or col<0 or row>=now_img.size[0] or col>=now_img.size[1]):
                    continue
                elif(k==4):
                    sum_pixel -= now_img.getpixel((row,col))*8
                else:
                    sum_pixel += now_img.getpixel((row,col))
                # print(sum_pixel,end=" ")
            # print()
            new_img.putpixel((i, j), now_img.getpixel((i,j))-(sum_pixel))
    now_img = new_img
    new_img = ImageTk.PhotoImage(new_img)
    message_up_text_var.set('Laplacian!!!')
    if(not if_in_function):
        photo_panel.configure(image=new_img)
        photo_panel.image = new_img
        my_window.update_idletasks()
def Unsharp_Masking(k=1):
    #先將照片另存，做一次average filter，用k帶進去算
    if(k<0):
        print("[Error]:k must >= 0")
        message_up_text_var.set("[Error]:k must >= 0")
        return
    message_up_text_var.set('processing...') 
    global now_img
    temp_img = now_img.copy()
    smoothing(3)#now now_img is being average filtered
    new_img = Image.new("L", (now_img.size[0], now_img.size[1]))
    for i in range(now_img.size[0]):
        for j in range(now_img.size[1]):
            new_img.putpixel((i, j),(k+1)*int(temp_img.getpixel((i,j))) - int(k*now_img.getpixel((i,j))))
    now_img = new_img
    new_img = ImageTk.PhotoImage(new_img)
    photo_panel.configure(image=new_img)
    photo_panel.image = new_img
    if(k == 1):
        message_up_text_var.set('unsharp masking(k=1)')
    elif(k>1):
        message_up_text_var.set('highboost filtering(k>1)')
    else:
        message_up_text_var.set('I do not know(k<1)')
    my_window.update_idletasks()
def open_raw():
        global filename,ori_img,now_img,ori_img_import
        filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a .raw File",)
        if not filename:
            message_up_text_var.set("[Error]:file path is empty!")
            return
        
        # print('hi')
        x = open(filename,'rb')
        
        ori_img_import = Image.frombytes("L", (512, 512), x.read(), 'raw')
        ori_img = ImageTk.PhotoImage(ori_img_import)
        now_img = ori_img_import
        photo_panel.configure(image=ori_img)
        photo_panel.image = ori_img
        my_window.update_idletasks()
    
    
def median_filter(degree):
    message_up_text_var.set('processing...')
    global now_img
    new_img = Image.new("L", (now_img.size[0], now_img.size[1]))
    for i in range(now_img.size[0]):
        for j in range(now_img.size[1]):
            all_pixel = []
            for k in range(degree*degree):
                row = i + int(k/degree) - int(degree/2)
                col = j + int(k%degree) - int(degree/2)
                if(row<0 or col<0 or row>=now_img.size[0] or col>=now_img.size[1]):
                    continue
                all_pixel.append(now_img.getpixel((row,col)))
            all_pixel.sort()
            new_img.putpixel((i, j), all_pixel[int(len(all_pixel)/2)])
            del all_pixel
    now_img = new_img
    new_img = ImageTk.PhotoImage(new_img)
    photo_panel.configure(image=new_img)
    photo_panel.image = new_img
    message_up_text_var.set('very median')
    my_window.update_idletasks()


#輸入
entry_a = tkinter.Entry(my_window, width = 8)
entry_b = tkinter.Entry(my_window, width = 8)
entry_size = tkinter.Entry(my_window,width=8)
entry_rot = tkinter.Entry(my_window,width=8)
entry_gray_up =tkinter.Entry(my_window,width=8)
entry_gray_lo =tkinter.Entry(my_window,width=8)
entry_file_name =tkinter.Entry(my_window,width=8)
entry_bit_bit =tkinter.Entry(my_window,width=8)
entry_filter_degree=tkinter.Entry(my_window,width=8)

#按鈕
#   brightness
button_bri_lin = tkinter.Button(my_window,text = 'linear',command = lambda: brightness_lin(float(entry_a.get()),float(entry_b.get())))
button_bri_exp = tkinter.Button(my_window,text = 'exp',command = lambda: brightness_exp(float(entry_a.get()),float(entry_b.get())))
button_bri_log = tkinter.Button(my_window,text = 'ln',command = lambda: brightness_log(float(entry_a.get()),float(entry_b.get())))
#   others
#--------show
button_show = tkinter.Button(my_window,text = 'Show Img',command = show_img)
#--------re_set
button_re_set = tkinter.Button(my_window,text = 'Re:set',command = re_set)
#   resize
button_resize = tkinter.Button(my_window,text = 'Do it',command = lambda:resize(int(entry_size.get())))
#   totation
button_rot = tkinter.Button(my_window,text = 'Do it',command = lambda:my_rotate(int(entry_rot.get())))
#   gray level slice
buton_ret_if_preserve = True
preserve_var = tkinter.StringVar()
preserve_var.set('Yes')
button_sice = tkinter.Button(my_window,text = 'Do it',command = lambda:gray_lvl_slic(int(entry_gray_lo.get()),int(entry_gray_up.get()),buton_ret_if_preserve))
button_sice_preserve = tkinter.Button(my_window,textvariable = preserve_var,command = preserve_change)
#   save
save_file_var = tkinter.StringVar()
save_file_var.set('png')
if_file_type_jpg = True
button_save_type = tkinter.Button(my_window,textvariable = save_file_var,command = file_type_change)
button_save = tkinter.Button(my_window,text = 'Do it',command = lambda:save_file(entry_file_name.get(),save_file_var.get()))
#   open
button_open = tkinter.Button(my_window,text = 'Open',command = open_img)
button_open_raw = tkinter.Button(my_window,text = 'Open_raw',command = open_raw)
#   bit plane
button_bit = tkinter.Button(my_window,text = 'Do it',command = lambda:bit_plane_slic(int(entry_bit_bit.get())))
#   histogram
button_histogram_show = tkinter.Button(my_window,text = 'Do it',command = historgram)
button_histogram_equal = tkinter.Button(my_window,text = 'Do it',command = equal)
#   filter
button_filter_smoothing = tkinter.Button(my_window,text = 'Smoothing',command = lambda:smoothing(int(entry_filter_degree.get())))
button_filter_sharpen = tkinter.Button(my_window,text = 'Sharpen',command = lambda:Unsharp_Masking(int(entry_filter_degree.get()))) 
button_filter_Laplacian = tkinter.Button(my_window,text = 'Laplacian',command = Laplacian)
button_filter_median = tkinter.Button(my_window,text = 'Median',command = lambda:median_filter(int(entry_filter_degree.get())))

#GUI
gui_row = 0
message_up.grid(row=0,column=0,columnspan=10)
photo_panel.grid(row=1,column=0)

#brightness
label_title.grid(row=2,column=0)
label_a.grid(row=2,column=1)
entry_a.grid(row=2,column=2)
label_b.grid(row=2,column=3)
entry_b.grid(row=2,column=4)
#label_dot.grid(row=1,column=0)
button_bri_lin.grid(row=2,column=7)
button_bri_exp.grid(row=2,column=8)
button_bri_log.grid(row=2,column=9)

#rotate
label_rot_title.grid(row=3,column=0)
label_rot.grid(row=3,column=1)
button_rot.grid(row=3,column=7)
entry_rot.grid(row=3,column=2)
#resize
label_resize_title.grid(row=4,column=0)
label_resize.grid(row=4,column=1)
entry_size.grid(row=4,column=2)
button_resize.grid(row=4,column=7)


#gray
label_gray_title.grid(row=5,column=0)
label_gray_low.grid(row=5,column=1)
entry_gray_lo.grid(row=5,column=2)
label_gray_up.grid(row=5,column=3)
entry_gray_up.grid(row=5,column=4)
label_gray_preserve.grid(row=5,column=5)
button_sice_preserve.grid(row=5,column=6)
button_sice.grid(row=5,column=7)
#bit plane
label_bit_title.grid(row=6,column=0)
label_bit_bit.grid(row=6,column=1)
entry_bit_bit.grid(row=6,column=2)
button_bit.grid(row=6,column=7)
gui_row=7
#   histogram
label_his_title.grid(row=gui_row,column=0)
label_his_show.grid(row=gui_row,column=4)
label_his_equal.grid(row=gui_row,column=6)
button_histogram_show.grid(row=gui_row,column=5)
button_histogram_equal.grid(row=gui_row,column=7)
gui_row+=1
#   filter
label_filter_title.grid(row=gui_row,column=0)
label_filter_degree.grid(row=gui_row,column=1)
entry_filter_degree.grid(row=gui_row,column=2)
button_filter_smoothing.grid(row=gui_row,column=3)
button_filter_sharpen.grid(row=gui_row,column=4)
button_filter_median.grid(row=gui_row,column=5)
button_filter_Laplacian.grid(row=gui_row,column=6)

gui_row+=1


#buttom button :)
#   save
label_save_title.grid(row=gui_row,column=0)
label_save_name.grid(row=gui_row,column=1)
entry_file_name.grid(row=gui_row,column = 2)
label_save_type.grid(row=gui_row,column=3)
button_save_type.grid(row=gui_row,column=4)
button_save.grid(row=gui_row,column=7)
#   others
button_show.grid(row=gui_row+1,column=10)
button_re_set.grid(row=gui_row+2,column = 10)
button_open.grid(row = gui_row+3,column = 10)
button_open_raw.grid(row = gui_row+3,column = 9)


my_window.mainloop()