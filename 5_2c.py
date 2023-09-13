
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

led1 = LED(10)
led2 = LED(11)
led3 = LED(12)
win = Tk()
win.title("toggle")
buttonFont = tkinter.font.Font(family = 'Calibri', size = 12)

def led1Toggle():
    if led1.is_lit:
        led1.off()
        button1["text"] = "ON"
    else:
        led1.on()
        button1["text"] = "OFF"

def led2Toggle():
    if led2.is_lit:
        led2.off()
        button2["text"] = "ON"
    else:
        led2.on()
        button2["text"] = "OFF"
       
def led3Toggle():
    if led3.is_lit:
        led3.off()
        button3["text"] = "ON"
    else:
        led3.on()
        button3["text"] = "OFF"

button1 = Button(win, text ='ON', font = buttonFont, command = led1Toggle, bg = 'red', height = 1, width = 24)
button1.grid(row =0, column=1)

button2 = Button(win, text ='ON', font = buttonFont, command = led2Toggle, bg = 'green', height = 1, width = 24)
button2.grid(row =1, column=1)

button3 = Button(win, text ='ON', font = buttonFont, command = led3Toggle, bg = 'blue', height = 1, width = 24)
button3.grid(row =2, column=1)

