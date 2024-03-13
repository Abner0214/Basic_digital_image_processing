import math
import tkinter
import numpy as np
import PIL
import scipy.fft
from PIL import Image, ImageEnhance, ImageFont, ImageTk
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.figure
import matplotlib.backends.backend_tkagg
import copy
import sys


#主程式
'''
傳入 img 轉成 r,g,b 三個 pixel arr
'''
def imgtoarr(img):
    img = img.convert('RGB')
    rr=[[0 for i in range(img.size[1])] for j in range(img.size[0])]
    gg=[[0 for i in range(img.size[1])] for j in range(img.size[0])]
    bb=[[0 for i in range(img.size[1])] for j in range(img.size[0])]
    for x in range (img.size[0]):
        for y in range (img.size[1]):
            r,g,b=img.getpixel((x,y))
            rr[x][y]=r
            gg[x][y]=g
            bb[x][y]=b
    cr=copy.deepcopy(rr)
    cg=copy.deepcopy(gg)
    cb=copy.deepcopy(bb)
    return cr,cg,cb

def arrtoimg(r,g,b,img):
    for x in range (len(r)):
        for y in range (len(r[0])):
            img.putpixel((x,y),(int(r[x][y]),int(g[x][y]),int(b[x][y])))
    return img
'''
副函式:
absrgbpixel,setrgbpixel

輸入:
rimg,gimg,bimg 分別為存 r,g,b 的陣列
(x,y) 選一個img上的pixel位置
rang 0~100 選擇相鄰pixel的相似度
setr,setg,setb 設定該區域轉換成的顏色
輸出:
rimg,gimg,bimg 為修改後img 陣列

描述:
選一pixel由該pixel延伸
將相鄰且相似的pixel
轉換成選擇的顏色

'''
def colorblocks(rimg,gimg,bimg,x,y,rang,setr=0,setg=0,setb=0,depth=0):

    
    ssety=sety=y
    ssetx=setx=x
    b=0
    # ssr=copy.deepcopy(rimg[setx][sety])
    # ssg=copy.deepcopy(gimg[setx][sety])
    # ssb=copy.deepcopy(bimg[setx][sety])
    ran=int(rang*255/100)
    ranc=ran +11
    #print("blocking ",a," times")
    #print("setx = ",setx,"sety = ",sety)
    #print("pixel: ",rimg[setx][sety]," ",gimg[setx][sety]," ",bimg[setx][sety])
    #mr,mg,mb=absrgbpixel(rimg,gimg,bimg,setx,sety,ssr,ssg,ssb,1)
    #print("mr = ",mr,"mg = ",mg,"mb = ",mb)
    #print("ssr = ",ssr,"ssg = ",ssg,"ssb = ",ssb)
    #print("ranc = ",ranc )    
    #print("setr","setg","setb",setr,setg,setb) 
    #colorblock(rimg,gimg,bimg,x,y,rang,setr,setg,setb,depth)
    rimg,gimg,bimg,ssetx,ssety=colorblock(rimg,gimg,bimg,setx,sety,rang,setr,setg,setb,depth)

    #ssetx=setx
    #ssety=sety
    
    # 4! arr 
    arr=[1,2,3,4,1,2,4,3,1,3,2,4,1,3,4,2,1,4,2,3,1,4,3,2,2,1,3,4,2,1,4,3,2,3,4,1,2,3,1,4,2,4,1,3,2,4,3,1,3,1,2,4,3,1,4,2,3,2,4,1,3,2,1,4,3,4,1,2,3,4,2,1,4,1,2,3,4,1,3,2,4,2,3,1,4,2,1,3,4,3,2,1,4,2,1,2]
    for b in range (120*4*3*2*4): 
        #print("b = ",b)
        dd = 90
        # right
        if(arr[b%dd]==1):
            while (  setx!=len(rimg)-1 and rimg[setx][sety]==setr and gimg[setx][sety]==setg and bimg[setx][sety]==setb):    
                setx=setx+1
                #print(len(rimg),len(gimg),len(bimg),setx,sety)
                #print(setx==len(rimg)-1)
                if(setx==len(rimg)-1):
                    break
                elif( rimg[setx][sety]!=setr or gimg[setx][sety]!=setg or bimg[setx][sety]!=setb):
                    #setx=setx-1
                    break
            mr,mg,mb=absrgbpixel(rimg,gimg,bimg,setx,sety,rimg[ssetx][ssety],gimg[ssetx][ssety],bimg[ssetx][ssety],1)
            #print("setx = ",setx," sety = ",sety )
            #print("pixel: ",rimg[setx][sety]," ",gimg[setx][sety]," ",bimg[setx][sety])
            #print("mmr = ",mr,"mmg = ",mg,"mmb = ",mb)
            #print("ranc = ",ranc )
            #print("setr = ",setr,"setg = ",setg,"setb = ",setb)
            ssety=sety
            ssetx=setx  
            #確認在範圍內
            if(mr<ranc and mg<ranc and mb<ranc and setx!=len(rimg)-1 and sety!=len(rimg[y])-1 and setx!=0 and sety!=0):
                #print("fright")
                rimg,gimg,bimg,ssetx,ssety=colorblock(rimg,gimg,bimg,setx,sety,rang,setr,setg,setb,depth)
            else:#使不出界
                setx=setx-1   
        
        # left  
        if(arr[b%dd]==2):   
            while ( rimg[setx][sety]==setr and gimg[setx][sety]==setg and bimg[setx][sety]==setb):
                setx=setx-1        
                if(setx==0):    
                    break
                elif( rimg[setx][sety]!=setr or gimg[setx][sety]!=setg or bimg[setx][sety]!=setb):
                    #setx=setx+1
                    #print("setx=setx+1")
                    break
            mr,mg,mb=absrgbpixel(rimg,gimg,bimg,setx,sety,rimg[ssetx][ssety],gimg[ssetx][ssety],bimg[ssetx][ssety],1)
            #print("setx = ",setx," sety = ",sety )
            ssety=sety
            ssetx=setx
            #確認在範圍內
            if(mr<ranc and mg<ranc and mb<ranc and setx!=len(rimg)-1 and sety!=len(rimg[y])-1 and setx!=0 and sety!=0):
                #print("fleft")
                rimg,gimg,bimg,ssetx,ssety=colorblock(rimg,gimg,bimg,setx,sety,rang,setr,setg,setb,depth)
            else:#使不出界
                setx=setx+1

        # up 
        if(arr[b%dd]==3):
            while ( rimg[setx][sety]==setr and gimg[setx][sety]==setg and bimg[setx][sety]==setb):
                sety=sety-1 
                #print("up")       
                if(sety==0):break
                elif( rimg[setx][sety]!=setr or gimg[setx][sety]!=setg or bimg[setx][sety]!=setb):
                    #sety=sety+1
                    break
            mr,mg,mb=absrgbpixel(rimg,gimg,bimg,setx,sety,rimg[ssetx][ssety],gimg[ssetx][ssety],bimg[ssetx][ssety],1)
            #print("setx = ",setx," sety = ",sety )
            ssety=sety
            ssetx=setx
            #確認在範圍內
            if(mr<ranc and mg<ranc and mb<ranc and setx!=len(rimg)-1 and sety!=len(rimg[y])-1 and setx!=0 and sety!=0):
                rimg,gimg,bimg,ssetx,ssety=colorblock(rimg,gimg,bimg,setx,sety,rang,setr,setg,setb,depth)
            else:#使不出界
                sety=sety+1

        # down 
        if(arr[b%dd]==4):
            while (setx!=len(rimg)-1 and rimg[setx][sety]==setr and gimg[setx][sety]==setg and bimg[setx][sety]==setb):
                sety=sety+1        
                if(sety==len(rimg)-1):
                    break
                elif( rimg[setx][sety]!=setr or gimg[setx][sety]!=setg or bimg[setx][sety]!=setb):
                    #sety=sety-1
                    break
            mr,mg,mb=absrgbpixel(rimg,gimg,bimg,setx,sety,rimg[ssetx][ssety],gimg[ssetx][ssety],bimg[ssetx][ssety],1)
            #print("setx = ",setx," sety = ",sety )
            ssety=sety
            ssetx=setx
            #確認在範圍內
            if(mr<ranc and mg<ranc and mb<ranc and setx!=len(rimg)-1 and sety!=len(rimg[y])-1 and setx!=0 and sety!=0):            
                #print("down")
                rimg,gimg,bimg,ssetx,ssety=colorblock(rimg,gimg,bimg,setx,sety,rang,setr,setg,setb,depth)
            else:#使不出界
                sety=sety-1
       
    return rimg,gimg,bimg
#pixel值和定值

def absrgbpixel(r,g,b,x2,y2,rvalue,gvalue,bvalue,absolute):#9項 #absolute>0 取正 =0 取正負 <0取負
    #if(x2!=255):
        #print("in absrgbpixel")
        #print("x2 = ",x2,"y2 = ",y2)
        #print("r[x2][y2]=",r[x2][y2],"g[x2][y2]=",g[x2][y2],"b[x2][y2]=",b[x2][y2])
        #print("rvalue = ",rvalue,"gvalue = ",gvalue,"bvalue = ",bvalue,"\n")
    mr=int(r[x2][y2]-rvalue)
    mg=int(g[x2][y2]-gvalue)
    mb=int(b[x2][y2]-bvalue)
    if(int(absolute)>0):
        if(mr<0):mr=mr*(-1)
        if(mg<0):mg=mg*(-1)
        if(mb<0):mb=mb*(-1)
    elif(absolute<0):
        if(mr>0):mr=mr*(-1)
        if(mg>0):mg=mg*(-1)
        if(mb>0):mb=mb*(-1)
    return mr,mg,mb
#比較兩pixel值
def cmprgbpixel(r,g,b,x1,y1,x2,y2,absolute):#8項 #absolute>0 取正 =0 取正負 <0取負
    #print("x1=",x1,"y1=",y1,"x2=",x2,"y2=",y2 )
    #print("r[x2][y2]=",r[x2][y2],"r[x1][y1]=",r[x1][y1])
    #print("absolute = ",absolute)
    mr=r[x2][y2]-r[x1][y1]
    mg=g[x2][y2]-g[x1][y1]
    mb=b[x2][y2]-b[x1][y1]
    if(absolute>0):
        if(mr<0):mr=mr*(-1)
        if(mg<0):mg=mg*(-1)
        if(mb<0):mb=mb*(-1)
    elif(absolute<0):
        if(mr>0):mr=mr*(-1)
        if(mg>0):mg=mg*(-1)
        if(mb>0):mb=mb*(-1)
    return mr,mg,mb
        
def setrgbpixel(r,g,b,sr,sg,sb,x,y):
    
    r[x][y]=copy.deepcopy(sr)
    g[x][y]=copy.deepcopy(sg)
    b[x][y]=copy.deepcopy(sb)

    return r,g,b



#抓區塊
sys.setrecursionlimit(20000)



def colorblock(rimg,gimg,bimg,x,y,rang,setr=0,setg=0,setb=0,depth=0):#10項
    #print("in colorblock")
    #print("depth = ",depth)
    rg=rimg[x][y]
    depth=depth+1
    if(depth>2000):
     #   print("x = ",x,"y = ",y)
        return rimg,gimg,bimg,x,y
    #print("x = ",x,"y = ",y)
    ran=int(rang*255/100)
    sr=copy.deepcopy(rimg[x][y])
    sg=copy.deepcopy(gimg[x][y])
    sb=copy.deepcopy(bimg[x][y])
    #print("setr = ",setr)
    rimg,gimg,bimg=setrgbpixel(rimg,gimg,bimg,setr,setg,setb,x,y)   #設定該格顏色   
    a=0 
 
    if(x==0 or y==0 or x==len(rimg)-1 or y==len(rimg[0])-1):
        #print("edge return")
        ssetx=x
        ssety=y
        #print("x = ",x,"y = ",y)
        return rimg,gimg,bimg,ssetx,ssety
    if( rimg[x+1][y]!=setr or  gimg[x+1][y]!=setg or bimg[x+1][y]!=setb):
        mr,mg,mb=absrgbpixel(rimg,gimg,bimg,x+1,y,sr,sg,sb,1)
        #print("mr = ",mr,"mg = ",mg,"mb = ",mb)
        #print("ran = ",ran )
        if(mr<ran and mg<ran and mb<ran):#right
         #   print("right")
            rimg,gimg,bimg,xxx,yyy=colorblock(rimg,gimg,bimg,x+1,y,rang,setr,setg,setb,depth)
    if( rimg[x-1][y]!=setr or  gimg[x-1][y]!=setg or bimg[x-1][y]!=setb):      
        mr,mg,mb=absrgbpixel(rimg,gimg,bimg,x-1,y,sr,sg,sb,1)
        #print("mr = ",mr,"mg = ",mg,"mb = ",mb)
        if(mr<ran and mg<ran and mb<ran  ):#left
       #     print("left")
            rimg,gimg,bimg,xxx,yyy=colorblock(rimg,gimg,bimg,x-1,y,rang,setr,setg,setb,depth)
    if( rimg[x][y+1]!=setr or  gimg[x][y+1]!=setg or bimg[x][y+1]!=setb):      
        mr,mg,mb=absrgbpixel(rimg,gimg,bimg,x,y+1,sr,sg,sb,1)
        #print("mr = ",mr,"mg = ",mg,"mb = ",mb)
        if(mr<ran and mg<ran and mb<ran):#up
      #      print("up")
            rimg,gimg,bimg,xxx,yyy=colorblock(rimg,gimg,bimg,x,y+1,rang,setr,setg,setb,depth)
    if( rimg[x][y-1]!=setr or  gimg[x][y-1]!=setg or bimg[x][y-1]!=setb):      
        mr,mg,mb=absrgbpixel(rimg,gimg,bimg,x,y-1,sr,sg,sb,1)
        #print("mr = ",mr,"mg = ",mg,"mb = ",mb)
        if(mr<ran and mg<ran and mb<ran):#dowm
     #       print("down")
            rimg,gimg,bimg,xxx,yyy=colorblock(rimg,gimg,bimg,x,y-1,rang,setr,setg,setb,depth)
    #print("last return")
    #print("x = ",x,"y = ",y)
    return rimg,gimg,bimg,x,y

print(sys.getrecursionlimit())

# window = tkinter.Tk()
# window.title('find edge')
# window.geometry("1400x1000")
# im1=Image.open('something.jpg')
# im1 = im1.convert('RGB')
# im1=im1.resize((512, 512))
# im2=Image.open('something.jpg')
# im2 = im2.convert('RGB')
# im2=im2.resize((512, 512))
# rr=[[0 for i in range(im1.size[0])] for j in range(im1.size[1])]
# gg=[[0 for i in range(im1.size[0])] for j in range(im1.size[1])]
# bb=[[0 for i in range(im1.size[0])] for j in range(im1.size[1])]
# for x in range (im1.size[0]):
#     for y in range (im1.size[1]):
#        r,g,b=im1.getpixel((x,y))
#        rr[x][y]=r
#        gg[x][y]=g
#        bb[x][y]=b
# cr=copy.deepcopy(rr)
# cg=copy.deepcopy(gg)
# cb=copy.deepcopy(bb)
# depth=0

# #執行主函式
# colorblocks(cr,cg,cb,450,400,5,0,0,0,depth)

# #print

# '''
# x=255
# y=112
# print("around ",x," , ",y," : ",)
# if(-1<x+1 and x+1<len(cg)):
#     print("x+1 ",int(cr[x+1][y]),int(cg[x+1][y]),int(cb[x+1][y]))
# if(-1<x-1 and x-1<len(cg)):
#     print("x-1 ",int(cr[x-1][y]),int(cg[x-1][y]),int(cb[x-1][y]))
# if(-1<y+1 and y+1<len(cg[0])):
#     print("y+1 ",int( cr[x][y+1]),int(cg[x][y+1]),int(cb[x][y+1]))
# if(-1<y-1 and y-1<len(cg[0])):
#     print("y-1 ",int(cr[x][y-1]),int(cg[x][y-1]),int(cb[x][y-1]))
# x=254
# y=114
# print("around ",x," , ",y," : ",)
# if(-1<x+1 and x+1<len(cg)):
#     print("x+1 ",int(cr[x+1][y]),int(cg[x+1][y]),int(cb[x+1][y]))
# if(-1<x-1 and x-1<len(cg)):
#     print("x-1 ",int(cr[x-1][y]),int(cg[x-1][y]),int(cb[x-1][y]))
# if(-1<y+1 and y+1<len(cg[0])):
#     print("y+1 ",int( cr[x][y+1]),int(cg[x][y+1]),int(cb[x][y+1]))
# if(-1<y-1 and y-1<len(cg[0])):
#     print("y-1 ",int(cr[x][y-1]),int(cg[x][y-1]),int(cb[x][y-1]))
# x=236
# y=113
# print("around ",x," , ",y," : ",)
# if(-1<x+1 and x+1<len(cg)):
#     print("x+1 ",int(cr[x+1][y]),int(cg[x+1][y]),int(cb[x+1][y]))
# if(-1<x-1 and x-1<len(cg)):
#     print("x-1 ",int(cr[x-1][y]),int(cg[x-1][y]),int(cb[x-1][y]))
# if(-1<y+1 and y+1<len(cg[0])):
#     print("y+1 ",int( cr[x][y+1]),int(cg[x][y+1]),int(cb[x][y+1]))
# if(-1<y-1 and y-1<len(cg[0])):
#     print("y-1 ",int(cr[x][y-1]),int(cg[x][y-1]),int(cb[x][y-1]))
# x=237
# y=111
# print("around ",x," , ",y," : ",)
# if(-1<x+1 and x+1<len(cg)):
#     print("x+1 ",int(cr[x+1][y]),int(cg[x+1][y]),int(cb[x+1][y]))
# if(-1<x-1 and x-1<len(cg)):
#     print("x-1 ",int(cr[x-1][y]),int(cg[x-1][y]),int(cb[x-1][y]))
# if(-1<y+1 and y+1<len(cg[0])):
#     print("y+1 ",int( cr[x][y+1]),int(cg[x][y+1]),int(cb[x][y+1]))
# if(-1<y-1 and y-1<len(cg[0])):
#     print("y-1 ",int(cr[x][y-1]),int(cg[x][y-1]),int(cb[x][y-1]))
# print("sss")
# '''
# for x in range (im1.size[0]):
#     for y in range (im1.size[1]):
#         r,g,b=im1.getpixel((x,y))
#         im2.putpixel((x,y),(int(cr[x][y]),int(cg[x][y]),int(cb[x][y])))


# ptoim1=ImageTk.PhotoImage(im1)
# imL1=tkinter.Label(window,image=ptoim1)
# imL1.grid(row=2,column=1 )
# ptoim2=ImageTk.PhotoImage(im2)
# imL2=tkinter.Label(window,image=ptoim2)
# imL2.grid(row=2,column=2 )
# window.mainloop()