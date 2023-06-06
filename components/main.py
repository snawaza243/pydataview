import os
from tkinter import *
import tkinter as tk
import pyttsx3
import tkinter.messagebox
from hyperlink import*
import webbrowser
from functools import partial

from PIL import ImageTk, Image
engine = pyttsx3.init()


import statistics as st
import numpy as np
from tkinter import font


import builtins
from tkinter import*
from matplotlib import pyplot as plt
import seaborn as sns
from numpy import random
from tktooltip import ToolTip


import seaborn as sns
from numpy import mean, std, cov
from numpy.random import randn, seed
from scipy.stats import pearsonr
from scipy.stats import spearmanr
from tktooltip import ToolTip

from PIL import ImageTk, Image # for bg pic


#######
# @Title : Distribution Calculator
# @Author : Dr. Rajeev Gupta
# @Co-Author : Shahnawaz Alam(11202722)
# @Version : 1.00 29.12.2021
########

# Define the function to create a new window
def create_window1(title):
    window = tk.Toplevel(root)
    window.title(title)

    # creating Main window 
    window.minsize(width=680,height=420)

    # Creating a class as stats
    class stats:
        def __init__(self, constant):

            # Variace data to be find with index
            self.types_list = ["mean", "median","mode","gmean","hmean","range","quartile","variance","std","cv"]
            self.type = self.types_list[9]

            self.values = []
            
            # Enter the data to calculate
            lb1=Label(window, text="Enter Data", )
            lb1.place(relx = .02, rely = .05,relwidth = .1, relheight = .05,)
            self.input_data = Entry(constant)
            self.input_data.place(relx = .15, rely = .05, relwidth = .50, relheight = .05)
        

        # Calculate button with specified command to be select
            self.type_label = Label(constant, text = "Median", )
            self.type_label.place(relx = .67, rely = .05, relwidth = .17, relheight = .05)

            self.check = Button(constant, text = "Calculate",  command = self.get_values, cursor="hand2", bg="gray")
            self.check.place(relx = .85, rely = .05,relwidth = .1, relheight = .05)
            

        # GUI for Measuring Central of Tendency
            lable2=Label(window, text="Measuring Central of Tendency", font=('Times',15))
            lable2.place(relx = .1, rely = .15,relwidth = .9, relheight = .05)

            self.mean = Button(constant, text = "Arithmetic Mean",bg="gray" ,command = self.set_mean ,cursor="hand2",)
            self.mean.place(relx = .02, rely = .25, relwidth = .18, relheight = .1)

            self.median = Button(constant, text = "Median",bg="gray",command = self.set_median, cursor="hand2",)
            self.median.place(relx = .8, rely = .25, relwidth = .18, relheight = .1)

            self.mode = Button(constant, text = "Mode",bg="gray",command = self.set_mode ,cursor="hand2",)
            self.mode.place(relx = .6, rely = .25, relwidth = .2, relheight = .1)

            self.gmean = Button(constant, text = "Geometric Mean",bg="gray",command = self.set_gmean, cursor="hand2",)
            self.gmean.place(relx = .4, rely = .25, relwidth = .2, relheight = .1)

            self.hmean = Button(constant, text ="Harmonic Mean",bg="gray",command = self.set_hmean ,cursor="hand2",)
            self.hmean.place(relx = .2, rely = .25, relwidth = .2, relheight = .1)


        # GUI for Measuring Dispersion
            lable2=Label(window, text="Measuring Dispersion", font=('Times',15))
            lable2.place(relx = .1, rely = .44,relwidth = .9, relheight = .05)

            self.mean = Button(constant, text = "Range",bg="gray" ,command = self.set_range , cursor="hand2",)
            self.mean.place(relx = .02, rely = .55, relwidth = .18, relheight = .1)

            self.quartile = Button(constant, text = "Quartile",bg="gray",command = self.set_quartile,  cursor="hand2",)
            self.quartile.place(relx = .8, rely = .55, relwidth = .18, relheight = .1)

            self.variance = Button(constant, text = "Variance",bg="gray",command = self.set_variance,  cursor="hand2",)
            self.variance.place(relx = .6, rely = .55, relwidth = .2, relheight = .1)

            self.std = Button(constant, text = "Standard Deviation",bg="gray",command = self.set_std,  cursor="hand2",)
            self.std.place(relx = .4, rely = .55, relwidth = .2, relheight = .1)

            self.cv = Button(constant, text ="Coefficient Variance",bg="gray",command = self.set_cv,  cursor="hand2",)
            self.cv.place(relx = .2, rely = .55, relwidth = .2, relheight = .1)

            lbv1=Label(window, text="Version: 1.01 09.11.2021", )
            lbv1.place(relx = .65, rely = .90,relwidth = .4, relheight = .05,)
            
            quiteButton=Button(window, text="Quit", command=quit, width=10, background='red', cursor="hand2" )
            quiteButton.place(relx = .88, rely = .90,relwidth = .1, relheight = .05)

            


        # Result label to be display
            lb0=Label(window, text="Result: ",font=('Times',15) )
            lb0.place(relx = .02, rely = .65, relwidth = .2, relheight = .1)

            self.answer_label = Label(constant, text = " ",font=('Times',20))
            self.answer_label.place(relx = .19, rely = .65, relwidth = .6, relheight = .1)

            # Black line 
            lbv11=Label(window, text=" ", bg="black",)
            lbv11.place(relx = .02, rely = .75,relwidth = .96, relheight = .01,)

            
        # Command defining of Central Tendancy
        def set_mean(self):
            self.type = self.types_list[0]
            self.type_label.config(text = "Arithmetic Mean")

        def set_median(self):
            self.type = self.types_list[1]
            self.type_label.config(text = "Median")
        def set_mode(self):    
            self.type = self.types_list[2]
            self.type_label.config(text = "Mode")

        def set_gmean(self):        
            self.type = self.types_list[3]
            self.type_label.config(text = " Geometric Mean")

        def set_hmean(self):            
            self.type = self.types_list[4]
            self.type_label.config(text = "Harmonic Mean")

        # Command defining of Dispersion
        def set_range(self):
            self.type = self.types_list[5]
            self.type_label.config(text = "Range")

        def set_quartile(self):            
            self.type = self.types_list[6]
            self.type_label.config(text = "Quartile") 

        def set_variance(self):            
            self.type = self.types_list[7]
            self.type_label.config(text = "Variance")

        def set_std(self):
            self.type = self.types_list[8]
            self.type_label.config(text = "Standard Deviatoin")  

        def set_cv(self):            
            self.type = self.types_list[9]
            self.type_label.config(text = "Coefficiant Variance")                   
                    
        
        # Formula assinged for various command
        def get_values(self):

            # Entery value get
            self.values = self.input_data.get()

            # For calculating the value of Central Tendancy
            if self.type == self.types_list[0]:
                mean = st.mean(eval(self.values))
                self.answer_label.config(text = mean)

            elif self.type == self.types_list[1]:
                median = st.median(eval(self.values))
                self.answer_label.config(text = median)
                
            elif self.type == self.types_list[2]:    
                mode = st.mode(eval(self.values))
                self.answer_label.config(text = mode) 

            elif self.type == self.types_list[3]:        
                gmean= st.geometric_mean(eval(self.values))
                self.answer_label.config(text = gmean)    

            elif self.type == self.types_list[4]:
                hmean= st.harmonic_mean(eval(self.values))
                self.answer_label.config(text = hmean)   

            # For calculating the value of Dispersion
            elif self.type == self.types_list[5]:            
                range1= range(eval(self.values))
                self.answer_label.config(text = range1) 

            elif self.type == self.types_list[6]:
                arr=[eval(self.values)]
                quartile1= np.quantile(arr, 1)
                self.answer_label.config(text = quartile1) 

            elif self.type == self.types_list[7]:
                variance= np.var(eval(self.values))
                self.answer_label.config(text = variance) 

            elif self.type == self.types_list[8]:
                std= np.std(eval(self.values))
                self.answer_label.config(text = std) 

            elif self.type == self.types_list[9]:
                mean1=np.mean(eval(self.values))
                std1=np.std(eval(self.values))
                cv=mean1/std1
                self.answer_label.config(text = cv) 
    s = stats(window)
    mainloop()

    
def create_window2(title):
    window = tk.Toplevel(root)
    window.title(title)
    # window.geometry("500x500")
    
    window.maxsize(width=690,height=500)

    
    
    def Poissondistribution():
        lamp = int(value1p.get())
        sizep = int(value2p.get())

        xp = random.poisson(lamp, sizep)
        sns.distplot(random.poisson(lamp, sizep), kde=False)
        plt.show()
        print(xp)
        t30.delete("1.0", END), t30.insert(END, xp)


    l00 = Label(window, text="Poisson Distribution: ", font=('Helvetica', 18, 'bold'))
    
    l10 = Label(window, text="lam: Rate or known number", anchor="w")
    l11 = Label(window, text="Size: Shape of returned array", anchor="w")

    value1p = StringVar()
    value2p = StringVar()
    
    e20 = Entry(window, textvariable=value1p)
    ToolTip(e20, msg="lam - rate or known number", )
    e21 = Entry(window, textvariable=value2p)
    ToolTip(e21, msg="Size - The shape of the returned array")

    b23 = Button(window, text="Calculate", command=Poissondistribution, bg="gray", cursor="hand2",)
    l300 = Label(window, text="Result: " , anchor="w" )
    t30 = Text(window, height=3,  width=15  )
    l00.grid(row=0, columnspan=2) 
    
    l10.grid(row=1, column=0) # test 1
    e20.grid(row=1, column=1) # input 1
    l11.grid(row=2, column=0) # test 2
    e21.grid(row=2, column=1) # input 2
    l300.grid(row=3, column=0) #result text
    t30.grid(row=3, column=1,) # result out
    b23.grid(row=3, column=2) # calculate




    def binomialdistribution():
        nb = int(value1b.get())
        pb = float(value2b.get())
        sizeb = int(value3b.get())

        xb = random.binomial(nb, pb, sizeb)
        sns.distplot(random.binomial(nb, pb, sizeb), hist=True, kde=False)
        plt.show()

        t80.delete("1.0", END), t80.insert(END, xb)


    l50 = Label(
        window, text="Binomial Distribution:", font=('Helvetica', 18, 'bold'))
    l60 = Label(window, text="No of Trails (n)")
    l61 = Label(window, text="Probability (p ≤ 1)", )
    l62 = Label(window, text="Size")

    value1b = StringVar()
    value2b = StringVar()
    value3b = StringVar()
    e70 = Entry(window, textvariable=value1b)
    e71 = Entry(window, textvariable=value2b)
    e72 = Entry(window, textvariable=value3b)

    b73 = Button(window, text="Calculate", command=binomialdistribution, bg="gray",  cursor="hand2",)

    l800 = Label(window, text="Result: ")
    t80 = Text(window, height=3,  width=15 )

    l50.grid(row=5, columnspan=2) # head
    
    l60.grid(row=6, column=0)
    l61.grid(row=7, column=0)
    l62.grid(row=8, column=0)
    
    e70.grid(row=6, column=1)
    e71.grid(row=7, column=1)
    e72.grid(row=8, column=1)
    
    l800.grid(row=9, column=0)
    t80.grid(row=9, column=1)
    b73.grid(row=9, column=2)


    def normaldistribution():
        locn = float(value1n.get())
        scalen = float(value2n.get())
        sizeAn = int(value3n.get())
        sizeBn = int(value4n.get())
        xn = random.normal(locn, scalen, size=(sizeAn, sizeBn))
        sns.distplot(random.normal(xn), hist=False)
        plt.show()
        print(xn)

        t130.delete("1.0", END), t130.insert(END, xn)


    l100 = Label(window, text="Normal Distribution:  ", font=('Helvetica', 18, 'bold'))
    l110 = Label(window, text="loc: (Mean)")
    l111 = Label(window, text="scale: (Standard Deviation)", )
    l112 = Label(window, text="Size A ")
    l113 = Label(window, text="Size B")

    value1n = StringVar()
    value2n = StringVar()
    value3n = StringVar()
    value4n = StringVar()
    e120 = Entry(window, textvariable=value1n)
    e121 = Entry(window, textvariable=value2n)
    e122 = Entry(window, textvariable=value3n, )
    e123 = Entry(window, textvariable=value4n, width=20)

    b123 = Button(window, text="Calculate", command=normaldistribution,  bg="gray",  cursor="hand2",)

    l1300 = Label(window, text="Result: ")
    t130 = Text(window, height=3,  width=15 )

    l100.grid(row=10, columnspan=2)
    
    l110.grid(row=11, column=0)
    l111.grid(row=11, column=1)
    
    e120.grid(row=12, column=0)
    e121.grid(row=12, column=1)
    
    l112.grid(row=13, column=0) # A text
    l113.grid(row=13, column=1 ) # B text

    e122.grid(row=14, column=0) # A out
    e123.grid(row=14, column=1) # B out
    


    l1300.grid(row=15, column=0)
    t130.grid(row=15, column=1)
    b123.grid(row=15, column=2)

  
    l1300 = Label(window, text=" ")
    l1300.grid(row=16, column=0 )
    
    b143 = Button(window, text="Quit", command=quit, width=7, background="red",   cursor="hand2", padx=10)
    b143.grid(row=16, column=2)

    window.mainloop()


def create_window3(title):
    window = tk.Toplevel(root)
    window.title(title)
    window.maxsize(width=690,height=320)
    
    # Defining the calculation
    def correlation():
        x1 = int(value1.get())
        xy1 = int(value2.get())
        y1 = int(value3.get())

        x2 = int(value4.get())
        xy2 = int(value5.get())
        y2 = int(value6.get())

        # seed random number generator
        seed(1)
        # prepare data
        data1 = x1 * randn(xy1) + y1
        data2 = data1 + (x2 * randn(xy2) + y2)
        # summarize
        m1 = ('%.3f'%(mean(data1)))
        m2 = ('%.3f'%(mean(data2)))
        sd1 = ('%.3f'%(std(data1)))
        sd2 = ('%.3f'%(std(data2)))
        covariance = cov(data1, data2)
        corr1, _ = (pearsonr(data1, data2))
        corr2, _ = (spearmanr(data1, data2))

        pyplot.scatter(data1, data2)
        pyplot.show()
        t40.delete("1.0", END), t40.insert(END, m1)

        t50.delete("1.0", END), t50.insert(END, m2)

        t60.delete("1.0", END), t60.insert(END, sd1)

        t70.delete("1.0", END), t70.insert(END, sd2)

        t80.delete("1.0", END), t80.insert(END, covariance)

        t90.delete("1.0", END), t90.insert(END, corr1)

        t100.delete("1.0", END), t100.insert(END, corr2)


    # Defining the GUI with giving config as grid
    l00 = Label(window, text="Enter Data1 & Data2 for Correlation Analysis", font='14')
    l10 = Label(window, text="X")
    ToolTip(l10, msg="Example:  10 to 100")
    l11 = Label(window, text="XY", )
    ToolTip(l11, msg="Example:  1000")

    l12 = Label(window, text="Y")
    ToolTip(l12, msg="Example:  10 to 100")
    l00.grid(row=0, columnspan=3)
    l10.grid(row=1, column=0)
    l11.grid(row=1, column=1)
    l12.grid(row=1, column=2)

    # data1
    value1 = StringVar()
    value2 = StringVar()
    value3 = StringVar()
    e20 = Entry(window, textvariable=value1)
    e21 = Entry(window, textvariable=value2)
    e22 = Entry(window, textvariable=value3)
    e20.grid(row=2, column=0)
    e21.grid(row=2, column=1)
    e22.grid(row=2, column=2)
    
    ToolTip(e20, msg="Data 1 X value\nExample: 10 to 100")
    ToolTip(e21, msg="Data 1 XY value\nExample:  1000")
    ToolTip(e22, msg="Data 1 Y value\nExample: 10 to 100")


    # Action butto cursor="hand2",n
    b23 = Button(window, text="Claculate", command=correlation, bg="gray",  cursor="hand2",)
    b23.grid(row=2, column=3)  # command

    # data2
    value4 = StringVar()
    value5 = StringVar()
    value6 = StringVar()
    e30 = Entry(window, textvariable=value4)
    e31 = Entry(window, textvariable=value5)
    e32 = Entry(window, textvariable=value6)
    e30.grid(row=3, column=0)
    e31.grid(row=3, column=1)
    e32.grid(row=3, column=2)

    ToolTip(e30, msg="Data 2 X value\nExample: 10 to 100")
    ToolTip(e31, msg="Data 2 XY value\nExample:  1000")
    ToolTip(e32, msg="Data 2 Y value\nExample: 10 to 100")

    # Result
    # mean1
    t40 = Text(window, height=1, width=30)
    l40 = Label(window, text="Results: \nMean1:                        ")

    t40.grid(row=4, column=1)
    l40.grid(row=4, column=0)


    # mean2
    t50 = Text(window, height=1, width=30)
    l50 = Label(window, text="Mean2:                       ")
    t50.grid(row=5, column=1)
    l50.grid(row=5, column=0)


    # std1
    t60 = Text(window, height=1, width=30)
    l60 = Label(window, text="STD1:                          ")
    t60.grid(row=6, column=1)
    l60.grid(row=6, column=0)


    # std2
    t70 = Text(window, height=1, width=30)
    l70 = Label(window, text="STD2:                          ")
    t70.grid(row=7, column=1)
    l70.grid(row=7, column=0)


    # Covariance
    t80 = Text(window, height=2, width=30)      
    l80 = Label(window, text="Covariance:                    ")
    t80.grid(row=8, column=1)
    l80.grid(row=8, column=0)


    # Pearson's correlation
    t90 = Text(window, height=1, width=30)  
    l90 = Label(window, text="Pearson's correlation:  ")
    t90.grid(row=9, column=1)
    l90.grid(row=9, column=0)


    # Spearman's Correlation
    t100 = Text(window, height=1, width=30)
    l100 = Label(window, text=" Spearman's Correlation: ")
    b103 = Button(window, text="Quit", command=quit, width=10, background='red', cursor="hand2",)
    t100.grid(row=10, column=1)
    l100.grid(row=10, column=0)
    b103.grid(row=10, column=3)
    
    spaceButton = Label()(window, text=" ", )
    spaceButton.grid(row=11, column=4)


    # Managing GUI Label, Entry, Button and Text as grid in row and column


    window.mainloop()

root = tk.Tk()
root.title('Data Visual')
root.geometry('545x350')
root.maxsize(545, 350)
root.minsize(545, 350)
frame = Frame(root, width=545, height=350)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open(
    "C:/Users/snawa/OneDrive/Documents/GitHub/pydataview/bg (2).jpg"))
# Create a Label Widget to display the text or Image
label = Label(frame, image=img)
label.pack()


def aboutinfo():
    tkinter.messagebox.showinfo(
        "PyData Visual", "\nThank you for using this application.\n \n Lets see what can it do.\n1. Measure Central Tendency and Dispersion\n2. Measure Distribution\n3. Correlation Analysis\n\n1. Measure Central Tendency and Dispersion:\na.) Central Tendency: Find Mean (Arithmetic, Harmonic, Geometric), Mode, Median\nb.)Dispersion: Find range, coefficient variance, standard deviation, variance, quartile\n\n2. Measure distribution: Poisson, Binomial, and Mornal Distribution\n\n3. Correlation Analysis: Analyze correlation of  two data \n\n\nMail us for more info. snawaza243@gmail.com\n\n\n\t\t\tData Visual!")

def exit():
    root.destroy()

lhead = Label(root,  text=" Data Visual", font=(
    "Century Gothic", 32, "bold"), bg='white')
lhead.place(x=160, y=20)


projectTitle1 = "Data Visual: Measure of Central Tendency and Dispersion"
projectTitle2 = "Data Visual: Distribution Calculator with figure"
projectTitle3 = "Data Visual: Correlation Analysis"

button1 = Button(root, 
                 text="Measure Central Tendencty & Dispersion", 
                 width=34, height=2, 
                 command=lambda: create_window1(projectTitle1), 
                 relief=RIDGE, borderwidth=3, 
                 font=('verdana', 11, 'bold'), 
                 cursor="hand2",
                 bg="#0099cc", fg="white", 
                 activebackground="#006699", activeforeground="white")
button1.place(x=115, y=100)


button2 = Button(root, 
                 text="Measure Distribution",
                 width=34, height=2, 
                 command=lambda: create_window2(projectTitle2), 
                 relief=RIDGE, borderwidth=3, 
                 font=('verdana', 11, 'bold'), 
                 cursor="hand2",
                 bg="#cc0000", fg="white", 
                 activebackground="#990000", activeforeground="white")
button2.place(x=115, y=160)

button3 = Button(root, 
                 text="Correlation Analysis", 
                 width=34, height=2, 
                 command=lambda: create_window3(projectTitle3), 
                 relief=RIDGE, borderwidth=3, 
                 font=('verdana', 11, 'bold'), 
                 cursor="hand2",
                 bg="#00cc00", fg="white", activebackground="#006600", activeforeground="white")
button3.place(x=115, y=220)



button1.bind("<Enter>", lambda e: button1.config(bg="#006699"))
button1.bind("<Leave>", lambda e: button1.config(bg="#0099cc"))
button2.bind("<Enter>", lambda e: button2.config(bg="#990000"))
button2.bind("<Leave>", lambda e: button2.config(bg="#cc0000"))
button3.bind("<Enter>", lambda e: button3.config(bg="#006600"))
button3.bind("<Leave>", lambda e: button3.config(bg="#00cc00"))



buttonAbout = Button(root, text="About", relief=RIDGE, borderwidth=1, font=( 'verdana', 10, 'bold'), cursor="hand2", bg='light blue', command=aboutinfo)
buttonAbout.place(anchor='center', x=425, y=325)

buttonExit = Button(root, text="Exit", relief=RIDGE, borderwidth=1, font=('verdana', 10, 'bold'), cursor="hand2", bg='red', command=exit)
buttonExit.place(anchor='center', x=486, y=325)


root.mainloop()
