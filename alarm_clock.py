#import libraries needed

import tkinter as tk
from tkinter import *
import datetime as dt
import time
import winsound as ws

#define the function for creating alarm

def clock(alarm):
    while True:
        time.sleep(1)
        actualTime = dt.datetime.now()
        currentTime = actualTime.strftime("%H : %M : %S")
        currentDate = actualTime.strftime("%d / %m / %y")
        message = "Current Time is : "+ str(currentTime)
        print(message)

        if currentTime == alarm:
            ws.PlaySound("sound.wav" , ws.SND_ASYNC)
            break

#define the function for user to give input

def alarmTime():
    setTime = f"{hour.get()} : {minute.get()} : {second.get()}"
    clock(setTime)

#create a window for GUI

gui = Tk()
gui.title("Alarm Clock")
gui.geometry("600x300")

Aclock = Label(gui,text="Alarm Clock",bg="Black",fg="red",font=("Arial Rounded MT",26)).place(x=180,y=10)
timeDesign = Label(gui,text="Clock is in 24hrs format", bg="black",fg="red",font=("Algerian",22)).place(x=100,y=80)
setTime = Label(gui,text="Set Your Alarm - ",bg="#FF7F50",fg="Black",relief="solid").place(x=20,y=150)
addTime = Label(gui,text="Hour   Min   Sec",fg="#FFBF00").place(x=170,y=150)

#variable required to set Alarm

hour = StringVar()
minute = StringVar()
second = StringVar()

hourTime = Entry(gui,textvariable = hour,bg="#CCCCFF",width=5,font=(20)).place(x=150,y=150)
minuteTime = Entry(gui,textvariable = minute,bg="#CCCCFF",width=5,font=(20)).place(x=180,y=150)
secondTime = Entry(gui,textvariable = second,bg="#CCCCFF",width=5,font=(20)).place(x=220,y=150)

#crate a button to submit the time

submit = Button(gui,text="Set alarm",bg="#40E0D0",font="White",width=15,command=alarmTime).place(x=130,y=200)

#define mainloop to run the code

gui.mainloop()





