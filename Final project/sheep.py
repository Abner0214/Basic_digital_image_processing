from PIL import Image
import pygame
import os

def color_wheel():
    pygame.init()
    running = True
    screen = pygame.display.set_mode((550,500))
    pygame.display.set_caption("Select")

    color_wheel_img = pygame.image.load(os.path.join("Image samples/Color image/Color wheel/color_wheel.png")).convert()
    gray_lvl_img = pygame.image.load(os.path.join("Image samples/Color image/Color wheel/gray_level3.png")).convert()
    color_wheel_img = pygame.transform.scale(color_wheel_img,(500,500))
    gray_lvl_img = pygame.transform.scale(gray_lvl_img,(50,500))

    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)

    return_data = (0,0,0)
    rect = pygame.Rect(0,0,60,60)

    intensity_mask = pygame.Surface((500,500))
    intensity_mask.set_alpha(0)
    intensity_mask.fill((0,0,0))

    outline_rect = pygame.Rect(0,0,61,61)
    WHITE = (255,255,255)

    while running :
        mouse = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEWHEEL:
                brush_width+=event.y
                if(brush_width<1):
                    brush_width=1
                elif(brush_width>150):
                    brush_width=150
        
        pos = pygame.mouse.get_pos()
        if(mouse[0]):
            return_data = screen.get_at(pos)[0:3]
            if(pos[0]>=500):
                intensity_mask.set_alpha(255-return_data[0])
            
        
        screen.blit(color_wheel_img,(0,0))
        screen.blit(intensity_mask,(0,0))
        screen.blit(gray_lvl_img,(500,0))
        pygame.draw.rect(screen,WHITE,outline_rect)
        pygame.draw.rect(screen,return_data,rect)
        pygame.display.update()
    pygame.quit()
    return return_data


def lowpass_watermark(main_image, watermark_image_import,position):
    """
    Main_image: 基底, 出來的圖片會跟基底差不多
    watermark_image_import: 浮水印, 會印在基底bit palne 0 的位置,會強制轉為黑底白字圖片
    position: 須為一tuple() or list[], 浮水印放置的座標, 座標法採用矩陣座標(左上=(0,0))

    基底和浮水印都可接受灰階或彩色圖片
    基底給彩色圖, 輸出就是彩色圖, 灰階同理
    若圖片帶有透明度, 輸出的圖片透明度將與基底相同

    """
    x,y = position
    if(not isinstance(watermark_image_import.getpixel((0, 0)),int)):
        temp_watermark = Image.new("L", (watermark_image_import.size[0], watermark_image_import.size[1]))
        for i in range(watermark_image_import.size[0]):
            for j in range(watermark_image_import.size[1]):
                if(any(tuple(watermark_image_import.getpixel((i,j))))):
                    temp_watermark.putpixel((i,j),255)
        watermark_image = temp_watermark
    else:
        watermark_image = watermark_image_import



    if(isinstance(main_image.getpixel((0, 0)),int)):
        ret_img = Image.new("L", (main_image.size[0], main_image.size[1]))
        for i in range(main_image.size[0]):
            for j in range(main_image.size[1]):
                new_val = main_image.getpixel((i, j))
                if(new_val%2!=0):
                    new_val -= 1
                if(watermark_image.size[0]>i-x >0 and watermark_image.size[1]>j-y >0):
                    if(watermark_image.getpixel((i-x,j-y))):
                        new_val+=1
                ret_img.putpixel((i,j),new_val)
    else:
        if(len(main_image.getpixel((0, 0)))==3):
            ret_img = Image.new("RGB", (main_image.size[0], main_image.size[1]))
        else:
            ret_img = Image.new("RGBA", (main_image.size[0], main_image.size[1]))
        for i in range(main_image.size[0]):
            for j in range(main_image.size[1]):
                new_val = list(main_image.getpixel((i, j)))
                for k in range(3):
                    if(new_val[k]%2!=0):
                        new_val[k] -= 1
                    if(watermark_image.size[0]>i-x >0 and watermark_image.size[1]>j-y >0):
                        if(watermark_image.getpixel((i-x,j-y))):
                            new_val[k]+=1
                ret_img.putpixel((i,j),tuple(new_val))
    ret_img.show()
    return ret_img

def bit_plane_slic(now_img,plane,rgb=[1,1,1]):
    """
    bit plane slicing
    now_img: 輸入圖片, 可接受灰階或彩色圖, 輸出會是同樣類型, 若圖片有透明度, 其透明度會被消除
    plane: slice第幾bit
    rgb: 為一tuple or list, 為0 or 1, 長度為3, rgb模式的Rgb係數
    """
    rgb = list(rgb)
    while(len(rgb)<3):
        rgb.append(1)
    for i in range(3):
        if rgb[i] >1:
            rgb[i] = 1
        elif rgb[i] <1:
            rgb[i] = 0

    if(isinstance(now_img.getpixel((0, 0)),int)):
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
    else:
        new_img = Image.new("RGB", (now_img.size[0], now_img.size[1]))

        for i in range(now_img.size[0]):
            for j in range(now_img.size[1]):
                temp = plane
                val = list(now_img.getpixel((i, j)))#x,y
                for k in range(3):
                    while(temp>0):
                        val[k]//=2
                        temp-=1
                    if(val[k]%2==1):
                        val[k] = 255*rgb[k]
                    else:
                        val[k] = 0
                new_img.putpixel((i, j), tuple(val))
    new_img.show()
    return new_img

class brush(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(0,0,5,5)
        x = Image.new("RGB",(5,5),color=(255,255,255))
        mode = x.mode
        size = tuple(x.size)
        data = x.tobytes()
        self.image = pygame.image.fromstring(data, size, mode)
    def update(self,scale,x,y,mouse_but):
        self.rect = pygame.Rect(0,0,scale,scale)
        self.image = pygame.transform.scale(self.image,(scale,scale))
        if(mouse_but[0]):
            self.image.fill((0,255,0))
        elif(mouse_but[2]):
            self.image.fill((255,0,0))
        else:
            self.image.fill((255,255,255))
        self.rect.center = (x,y)
        self.image.set_alpha(170)

brush_obj = brush()
brush_group = pygame.sprite.Group()
brush_group.add(brush_obj)
# 300, 100, 5
def draw_watermark(Width,Height,brush):
    pygame.init()
    running = True
    screen = pygame.display.set_mode((Width,Height))
    pygame.display.set_caption("Draw your watermark!")

    pygame.mouse.set_visible(False)

    ret_watermark = Image.new("RGB",(Width,Height))
    mode = ret_watermark.mode
    size = tuple(ret_watermark.size)
    data = ret_watermark.tobytes()

    brush_width = brush

    while running :
        mouse = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEWHEEL:
                brush_width+=event.y
                if(brush_width<1):
                    brush_width=1
                elif(brush_width>150):
                    brush_width=150
        
        pos = pygame.mouse.get_pos()
        if(mouse[0]):
            for i in range(pos[0]-brush_width//2 , pos[0]+brush_width//2+1):
                for j in range(pos[1]-brush_width//2,pos[1]+brush_width//2+1):
                    if(size[0]>i>=0 and size[1]>j>=0):
                        ret_watermark.putpixel((i,j),(255,255,255))
        elif(mouse[2]):
            for i in range(pos[0]-brush_width//2 , pos[0]+brush_width//2+1):
                for j in range(pos[1]-brush_width//2,pos[1]+brush_width//2+1):
                    if(size[0]>i>=0 and size[1]>j>=0):
                        ret_watermark.putpixel((i,j),0)
        
        
        data = ret_watermark.tobytes()
        screen.blit(pygame.image.fromstring(data, size, mode),(0,0))
        brush_obj.update(brush_width,pos[0],pos[1],mouse)
        brush_group.draw(screen)
        pygame.display.update()
    pygame.quit()
    return ret_watermark

def rgb2i(R,G,B):
    r = R / 255
    g = G / 255
    b = B / 255

    cmax = max(r,g,b)
    cmin = min(r,g,b)
    delta = cmax- cmin
    
    I = (cmax+cmin)/2
    I = (R+G+B)/3
    I = int(I)
    return (I)

def create_trans(im1_inp,rgba = (0,0,0,0.2),slice = -1):
    r,g,b,a = rgba
    """
    create a transparent due to their gray level
    im1_inp: 目標
    rgba: 顏色參數, 全部填滿對應顏色, 將灰階值乘以對應透明度
    slice: 分割為一個list or tuple包著2個list or tuple代表對應的
    """
    if(slice == -1):
        im1_png = Image.new("RGBA", (im1_inp.size[0], im1_inp.size[1]))
        if(isinstance(im1_inp.getpixel((0, 0)),int)): 
            for i in range(im1_inp.size[0]):
                for j in range(im1_inp.size[1]):
                    val = im1_inp.getpixel((i, j))
                    im1_png.putpixel((i, j), (r,g,b,int(val*a)))
        else:
            for i in range(im1_inp.size[0]):
                for j in range(im1_inp.size[1]):
                    val = im1_inp.getpixel((i, j))
                    val_2 = rgb2i(val[0],val[1],val[2])
                    im1_png.putpixel((i, j), (r,g,b,int(val_2*a)))
    elif(len(slice)>=2 and slice[0][0]<=slice[1][0] and slice[0][1]<=slice[1][1]):#乖乖

        im1_png = Image.new("RGBA", (im1_inp.size[0], im1_inp.size[1]))
        if(isinstance(im1_inp.getpixel((0, 0)),int)): 
            for i in range(slice[0][0],slice[1][0]):
                for j in range(slice[0][1],slice[1][1]):

                    val = im1_inp.getpixel((i, j))
                    im1_png.putpixel((i, j), (r,g,b,int(val*a)))
        else:
            for i in range(slice[0][0],slice[1][0]):
                for j in range(slice[0][1],slice[1][1]):

                    val = im1_inp.getpixel((i, j))
                    val_2 = rgb2i(val[0],val[1],val[2])
                    im1_png.putpixel((i, j), (r,g,b,int(val_2*a)))
    else:
        print("[ERROR] occured when creating transparent image: invalid slice input")

    return im1_png

def negative(im1_inp):
    """
    改負片, 可接受彩色與灰階, 輸出對應
    """
    im1_png = Image.new("RGB", (im1_inp.size[0], im1_inp.size[1]))
    if(isinstance(im1_inp.getpixel((0, 0)),int)): 
        for i in range(im1_inp.size[0]):
            for j in range(im1_inp.size[1]):
                val = im1_inp.getpixel((i, j))
                im1_png.putpixel((i, j), (255-val,255-val,255-val))
    else:
        for i in range(im1_inp.size[0]):
            for j in range(im1_inp.size[1]):
                val = im1_inp.getpixel((i, j))
                im1_png.putpixel((i, j), (255-val[0],255-val[1],255-val[2]))
    return im1_png

def merge(img1,img2,rgbaa,rgbab):
    """
    將兩張透明圖片合併
    give 2 image return the merged transparent image
    """
    print("Setting transparent(0/3)")
    im1_png = negative(img1)
    print("Setting transparent(1/3)")
    im1_png = create_trans(im1_png,rgba=rgbaa)
    print("img1 transparent done")
    print("Setting transparent(2/3)")


    im2_png = create_trans(img2,rgba=rgbab)
    print("img2 transparent done")
    print("Setting transparent(3/3)")

    print("Applying alpha composite from im1 to im2...")
    blend = alpha_composite(im1_png,im2_png)
    print("Applyed alpha composite")
    return blend


def alpha_composite(imga,imgb):
    ret_img = Image.new("RGBA", (imga.size[0], imga.size[1]))
    for i in range(imga.size[0]):
        for j in range(imga.size[1]):
            if(imgb.size[0]>i and imgb.size[1]>j):
                va = imga.getpixel((i,j))
                vb = imgb.getpixel((i,j))

                aa = va[3]/255
                ab = vb[3]/255
                temp = ab*(1-aa)
                alp = aa + temp
                if(alp==0):
                    v = (0,0,0,0)
                else:
                    v = (int((aa*va[0]+temp*vb[0])/(alp)),int((aa*va[1]+temp*vb[1])/(alp)),int((aa*va[2]+temp*vb[2])/(alp)), int(alp*255))
            else:
                v = imga.getpixel((i,j))
            ret_img.putpixel((i,j),v)
    return ret_img



def camouflage_img_generater(img1,img2,rgba_img1=(0,0,0,0.2),rgba_img2 = (255,255,255,0.8),scale = -1,img1_position=(0,0),img2_position=(0,0),slice = -1):
    """
    generate an image that will display different image in front of different background
    img1: 偽裝, an image, image1 that will display in front of background(default white)
    img2: 真相, an image, image1 that will display in front of background(generally black)
    scale: 大小, default -1, input(x,y), the generated image size(default -1, which will become img1's scale)
    img1/2_position: 放置位置, default(0,0), input (x,y), the position that put on screen(矩陣座標)
    rgba_img1/2: 填充背景顏色與透明參數, input(0~255,0~255,0~255,0~1), the background and the proportion (r,g,b,alpha)

    slice: default -1, input((x1,y1),(x2,y2)), create camouflage_img in sapific range
    """
    """
    流程:
     創建一張總圖大小之圖片, 並將偽裝貼至其之上(需考慮位置), 我們稱這張圖為基底
     做出基底的透明圖(分割)-> 黑隱圖
     做出真相的透明圖片(分割) -> 白隱圖
     將其合併, 需考慮總圖大小與白隱圖貼上之位置, 還有切割
    """
    if((isinstance(rgba_img1,tuple) or isinstance(rgba_img1,list)) and len(rgba_img1)==4):
        if(rgba_img1[3]>1 or rgba_img1[3]<0):
            rgba_img1 = (0,0,0,0.2)
        for i in range(3):
            if(rgba_img1[i]>255 or rgba_img1[i]<0):
                rgba_img1 = (0,0,0,0.2)
    else:
        rgba_img1 = (0,0,0,0.2)
    if((isinstance(rgba_img2,tuple) or isinstance(rgba_img2,list)) and len(rgba_img2)==4):
        if(rgba_img2[3]>1 or rgba_img2[3]<0):
            rgba_img2 = (255,255,255,0.8)
        for i in range(3):
            if(rgba_img2[i]>255 or rgba_img2[i]<0):
                rgba_img2 = (255,255,255,0.8)
    else:
        rgba_img2 = (255,255,255,0.8)
    if((not (isinstance(img1_position,tuple) or isinstance(img1_position,list)) and len(img1_position)==2)):
        img1_position=(0,0)
    if((not (isinstance(img2_position,tuple) or isinstance(img2_position,list)) and len(img2_position)==2)):
        img2_position=(0,0)

    print("Initializing...")
    if(isinstance(scale,int)):
        ret_imagea = Image.new("RGBA", (img1.size[0], img1.size[1]))
        ret_imageb = Image.new("RGBA", (img1.size[0], img1.size[1]))
    else:
      if(len(scale)==2 and scale[0]>0 and scale[1]>0):
        ret_imagea = Image.new("RGBA", (scale[0], scale[1]))
        ret_imageb = Image.new("RGBA", (scale[0], scale[1]))
      else:
        print("invalid scale, return to default")
        ret_imagea = Image.new("RGBA", (img1.size[0], img1.size[1]))
        ret_imageb = Image.new("RGBA", (img1.size[0], img1.size[1]))
    print("Resizing image(1/4)...")
    print("Resizing image(2/4)...")
    x1,y1 = img1_position
    x2,y2 = img2_position

    #process_1a
    for i in range(ret_imagea.size[0]):
        for j in range(ret_imagea.size[1]):
            if(img1.size[0]>i>=x1 and img1.size[1]>j>=y1):
                ret_imagea.putpixel((i,j),img1.getpixel((i-x1,j-y1)))
    print("Resizing image(3/4)...")
    #process_1b
    for i in range(ret_imageb.size[0]):
        for j in range(ret_imageb.size[1]):
            if(img2.size[0]>i>=x2 and img2.size[1]>j>=y2):
                ret_imageb.putpixel((i,j),img2.getpixel((i-x2,j-y2)))
    print("Resizing image(4/4)...")

    print("Merging image...(0/1)")
    ret_image_1 = merge(ret_imagea,ret_imageb,rgbaa=rgba_img1,rgbab=rgba_img2)
    ret_image_2 = ret_image_1.copy()
    print("Merged(1/1)")

    print("Slicing...(0/1)")
    if(((isinstance(slice,tuple)) or isinstance(slice,list)) and len(slice)>=2 and len(slice[0])>=2 and len(slice[0])>=2):
        if(slice[0][0]<0 and slice[1][0]<0 and slice[0][1]<0 and slice[1][1]<0):
            pass
        else:
            for i in range(ret_image_1.size[0]):
                for j in range(ret_image_1.size[1]):
                    if(slice[0][0]<=i<=slice[1][0] and slice[0][1]<=j<=slice[1][1]):
                        ret_image_2.putpixel((i,j),ret_image_1.getpixel((i,j)))
                    else:
                        ret_image_2.putpixel((i,j),ret_imagea.getpixel((i,j)))
    print("Sliced(1/1)")
    print("[camouflage_img_generater] Done!!!")
    return ret_image_2
    #process_2
    # bacic_trans = negative(img1)
    # bacic_trans = create_trans(bacic_trans,rgba_img1)


"""
main test
"""
# im1=Image.open("liu_good.jpg")
# im2=Image.open("liu_bad.jpg")


# # blend = camouflage_img_generater(im1,im2,scale=(800,1000),img1_position=(-100,-100),img2_position=(100,100),rgba_img1=(255,0,0,0.2),slice=((100,100),(700,1300)))
# # blend = merge(im1,im2)
# blend = camouflage_img_generater(im1,im2)
# blend.show()
# # blend.save("liu.png")