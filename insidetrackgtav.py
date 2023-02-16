import csv

import pyautogui as pyg
import time as t
import mouse as m
import keyboard
from PIL import ImageGrab
from PIL import Image
from pytesseract import pytesseract
import pandas as pd
import cv2 as cv
#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract
pyg.keyDown("alt")
pyg.press("tab")
pyg.keyUp("alt")
a=0
max=30
l=0
def check(ar):
    for i in range(len(ar)):
        try:
            if ar[i][0]=="W":
                ar[i]=17
        except:
            continue
    for i in range(len(ar)):
        try:
            if ar[i][0]=="A":
                ar[i]=4
        except:
            continue
    for i in range(len(ar)):
        try:
            if ar[i][0]=="T":
                ar[i]=7
        except:
            continue
    for i in range(len(ar)):
        try:
            if ar[i]=="2ga":
                ar[i]=29
        except:
            continue
    for i in range(len(ar)):
        try:
            if ar[i][0]=="/":
                ar.pop(i)
        except:
            pass
    return ar
while keyboard.is_pressed("esc")==False:
    a = 0
    max = 30
    l = 0
    ff = open("data.csv", "a")
    f=csv.writer(ff)
    pb=(1279,917)
    pyg.moveTo(pb)
    t.sleep(0.5)
    m.press()
    t.sleep(1)
    m.release()
    b = 349
    c = 383
    t.sleep(0.7)
    for i in range(5):

        ss_region = (182,b,253,c)
        ss_img = ImageGrab.grab(ss_region)
        ss_img.save(f"{i + 1}.jpg")
        b=b+120
        c=c+122
    ss_region = (182,932,253,990)
    ss_img = ImageGrab.grab(ss_region)
    ss_img.save(f"{6}.jpg")


    arr=[]
    for k in range(1,7):
        #Define path to image
        path_to_image = f'{k}.jpg'
        #Open image with PIL
        img = Image.open(path_to_image)
        #Extract text from image
        text = pytesseract.image_to_string(img)
        print(text)
        text=text.split("/")
        try:
            arr.append(int(text[0]))
        except:
            arr.append(text[0])


    arr=check(arr)
    ar=str(tuple(arr))
    df = pd.read_csv("data.csv")
    if ar in df.Odds.tolist():
        print("isme")
        pos = int(df.loc[df['Times'] == df['Times'].max(), 'Win pos'].iloc[0])
        tt=int(df.loc[df['Times'] == df['Times'].max(), 'Win pos'].iloc[0].index())
        print(pos)
    else:
        for i in range(len(arr)):
            try:
                if arr[i][0] == "E":
                    pos = i
                    break
            except:
                if arr[i] == max:
                    if i < pos:

                        pos = i
                elif arr[i] < max:
                    l = max
                    max = arr[i]
                    pos = i
    dic={
        0:(182,352),
        1:(182,472),
        2:(182,593),
        3:(182,688),
        4:(182,808),
        5:(182,928)
    }
    pyg.moveTo(dic.get(pos))
    m.press()
    t.sleep(0.5)
    m.release()
    ssr=(1382,391,1510,431)
    ss_img = ImageGrab.grab(ssr)
    ss_img.save("bal.jpg")
    path_to_image = "bal.jpg"
    img = Image.open(path_to_image)
    bal = int(pytesseract.image_to_string(img))
    print(pos)
    pyg.moveTo(1521,513)
    """if bal<400000:
        for i in range(10):
            t.sleep(1)
            pyg.keyDown("alt")
            pyg.press("tab")
            pyg.keyUp("alt")
            pyg.keyDown("alt")
            pyg.press("f4")
            pyg.keyUp("alt")
            t.sleep(0.8)
            pyg.press("enter")"""
    if bal<25000:
            m.press()
            t.sleep(2)
            m.release()
    elif bal>50000:
            m.press()
            t.sleep(8)
            m.release()
    else:
            m.press()
            t.sleep(4)
            m.release()
    pyg.moveTo(1235,771)
    m.press()
    t.sleep(1)
    m.release()

    t.sleep(41)
    ssr = (731, 800, 818, 856)
    ss = ImageGrab.grab(ssr)
    ss.save("winodd.jpg")

    path_to_image = "winodd.jpg"
    img = Image.open(path_to_image)
    text = pytesseract.image_to_string(img)
    text=text.split("/")
    text=check(text)
    try:
        if ar in df.Odds.tolist():
            if pos==arr.index(text[0]):
                df.loc[tt,'Times']=+1
            else:
                a=[ar,arr.index(text[0]),1]
        else:
            a = [ar, arr.index(text[0]), 1]
    except:
        a = [ar,None, 1]
    f.writerow(a)
    ff.close()
    m.press("right")
    t.sleep(1)
    m.release("right")

    print(a)
    #print(pyg.position())



