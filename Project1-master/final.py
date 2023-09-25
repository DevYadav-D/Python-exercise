import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import tkinter as tk

global s
s=0

#click function
def click():
    global s
    if var1.get()==1 and var2.get()==0:
        t = np.linspace(1, 100, 1000)
        x = s*np.sin(t/(2*np.pi))
        plt.subplot(1,1,1)   
        plt.plot(t, x)
        plt.title('Sinusoidal Signal') 
        plt.ylabel('Value (V)')
        plt.xlabel('Time (s)')
        plt.show()
    elif var2.get()==1 and var1.get()==0:
        tar_noise=10
        mean_noise=0
        t = np.linspace(1, 100, 1000)
        a = s*np.sin(t/(2*np.pi))
        noise=np.random.normal(mean_noise, np.sqrt(tar_noise),len(a**2))
        sig_avg= np.mean(a)
        y=a+noise
        plt.subplot(1,1,1)
        plt.plot(t, y)
        plt.title('Signal with noise')
        plt.ylabel('Value (V)')
        plt.xlabel('Time (s)')
        plt.show()
    elif var1.get()==1 and var2.get()==1 :
        t = np.linspace(1, 100, 1000)
        b = s*np.sin(t/(2*np.pi))
        plt.subplot(3,1,1)   
        plt.plot(t, b)
        plt.title('Sinusoidal Signal') 
        plt.ylabel('Value (V)')
        plt.xlabel('Time (s)')
        tar_noise=10
        mean_noise=0
        noise=np.random.normal(mean_noise, np.sqrt(tar_noise),len(b**2))
        sig_avg= np.mean(b)
        y=b+noise
        plt.subplot(3,1,3)
        plt.plot(t, y)
        plt.title('Signal with noise')
        plt.ylabel('Value (V)')
        plt.xlabel('Time (s)')
        plt.show()
    else :
        Label(window, text="Select atleast one box", bg="black",fg="white",font="none 12 bold" ).grid(row=11, column=0, sticky=W)
        


# main 
window=tk.Tk()
window.title("Sin(t) graph and Gaussian Noise")
window.configure(background="white")
#title
title=tk.Label(text="Choose the graph: Sin or Gaussian Noise")
title.grid(row=0, column=0)


# creating the check button

Label(window, text="Choose value of amplitude of the function:",bg="grey").grid(row=1, sticky=W)
var3 = IntVar()
Checkbutton(window, text="Random(value taken is 10)", variable=var3).grid(row=2, sticky=W)
var4 = IntVar()
Checkbutton(window, text="Manual", variable=var4).grid(row=3, sticky=W)

def click1():
    global s
    if var4.get()== 1:
        textentry= tk.Entry(width =40, bg='white')
        textentry.grid(row=5,column=0)
        def click2():
            global s
            s=float(textentry.get())
            print("amplitude", s)
        button1=tk.Button(text="Submit", command=click2)
        button1.grid(row=6, column=0)
        var3==0
        print("earlier amplitude",s)
    else :
        Label(window, text="Random value is selected").grid(row=5, column=0, sticky=W)
        var4==0
        s=10
        print("amplitude",s)
button2=tk.Button(text="Submit", command=click1)
button2.grid(row=4, column=0)

Label(window, text="Choose the Graph:",bg="grey").grid(row=7, sticky=W)
var1 = IntVar()
Checkbutton(window, text="Sin", variable=var1).grid(row=8, sticky=W)
var2 = IntVar()
Checkbutton(window, text="Gaussian Noise", variable=var2).grid(row=9, sticky=W)
button3=tk.Button(text="Submit", command=click)
button3.grid(row=10, column=0)
#exit function
def close_window():
    window.destroy()
    exit()
#exit 
button4=tk.Button(text="Exit", command=close_window)
button4.grid(row=12, column=0)


### run the main loop

window.mainloop()



