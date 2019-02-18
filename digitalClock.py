#!/usr/bin/python3
from tkinter import *
import tkinter as tk
import datetime
import math
import time as pytime

root = tk.Tk() 
root.title("Clock")

def close():
	root.destroy()

root.resizable(False, False)

canvas = Canvas(root, width = 400, height = 400, bg='#000000', highlightbackground="#332f28")

currentDT = datetime.datetime.now()
time = currentDT.strftime("%I:%M:%S %p")
hour = datetime.datetime.now().hour;
minute = datetime.datetime.now().minute;
second = datetime.datetime.now().second;
canvas.create_text(197,50, tag="timestamp",fill="#65FF00",font='Verdana 41 bold', text=time)

canvas.pack()

def update_label():
	currentDT = datetime.datetime.now()
	time = currentDT.strftime("%I:%M:%S %p")
	hour = datetime.datetime.now().hour;
	minute = datetime.datetime.now().minute;
	second = datetime.datetime.now().second;
	canvas.itemconfig("timestamp", text=time)
	root.after(1000, update_label)

w = 398 
h = 100 

ws = root.winfo_screenwidth() 
hs = root.winfo_screenheight() 

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))

update_label()

root.mainloop() 