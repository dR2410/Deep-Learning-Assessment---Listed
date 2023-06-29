# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 16:00:37 2023

@author: Rahul
"""
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
from transformers import pipeline


my_w = tk.Tk()
my_w.geometry("400x400")  # Size of the window 
my_w.title('AI/ML')
my_font1=('times', 18, 'bold')
l1 = tk.Label(my_w,text='Caption Generator',width=30,font=my_font1)  
l1.grid(row=1,column=1)
b1 = tk.Button(my_w, text='Upload File', 
   width=20,command = lambda:upload_file())
b1.grid(row=2,column=1) 



def upload_file():
    global img
    f_types = [('png Files', '*.png'),('jpg files','*jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img=Image.open(filename)
    img_resized=img.resize((300,200)) # new width & height
    img=ImageTk.PhotoImage(img_resized)
    b2 =tk.Button(my_w,image=img) # using Button 
    b2.grid(row=3,column=1)
    
    
    image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")
    res = image_to_text(filename)
    textbox = Entry(my_w, bg="white", width=50, borderwidth=1)
    textbox.insert(0, res)
    textbox.grid(row=4, column=1)
my_w.mainloop() 