import tkinter as tk

from tkinter import *
import statistics as st
import numpy as np
from tkinter import font


import builtins
from tkinter import*
from tkinter import font
from matplotlib import pyplot as plt
import seaborn as sns
from numpy import random
from tktooltip import ToolTip

import builtins
from tkinter import*
from tkinter import font
from matplotlib import pyplot as plt
import seaborn as sns
from numpy import mean, std, cov
from numpy.random import randn, seed
from matplotlib import pyplot
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
    # window = Tk()
    window.minsize(width=680,height=420)
    # window.title("Project-1: Measure of Central Tendency and Dispersion")


    #######
    # @Title       : Measure of Central Tendancy and Dispersion
    # @Author      : Dr. Rajeev Gupta
    # @Co-Author   : Shahnawaz Alam(11202722), Sunidhi Saurabh(11202723)
    # @Version     : 1.00 07.10.2021 -  Baseline Code
    # @Update-Ver. : 1.01 09.11.2021
    ########

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

            self.check = Button(constant, text = "Calculate",  command = self.get_values)
            self.check.place(relx = .85, rely = .05,relwidth = .1, relheight = .05)
            

        # GUI for Measuring Central of Tendency
            lable2=Label(window, text="Measuring Central of Tendency", font=('Times',15))
            lable2.place(relx = .1, rely = .15,relwidth = .9, relheight = .05)

            self.mean = Button(constant, text = "Arithmetic Mean",bg="gray" ,command = self.set_mean)
            self.mean.place(relx = .02, rely = .25, relwidth = .18, relheight = .1)

            self.median = Button(constant, text = "Median",bg="gray",command = self.set_median)
            self.median.place(relx = .8, rely = .25, relwidth = .18, relheight = .1)

            self.mode = Button(constant, text = "Mode",bg="gray",command = self.set_mode)
            self.mode.place(relx = .6, rely = .25, relwidth = .2, relheight = .1)

            self.gmean = Button(constant, text = "Geometric Mean",bg="gray",command = self.set_gmean)
            self.gmean.place(relx = .4, rely = .25, relwidth = .2, relheight = .1)

            self.hmean = Button(constant, text ="Harmonic Mean",bg="gray",command = self.set_hmean)
            self.hmean.place(relx = .2, rely = .25, relwidth = .2, relheight = .1)


        # GUI for Measuring Dispersion
            lable2=Label(window, text="Measuring Dispersion", font=('Times',15))
            lable2.place(relx = .1, rely = .44,relwidth = .9, relheight = .05)

            self.mean = Button(constant, text = "Range",bg="gray" ,command = self.set_range)
            self.mean.place(relx = .02, rely = .55, relwidth = .18, relheight = .1)

            self.quartile = Button(constant, text = "Quartile",bg="gray",command = self.set_quartile)
            self.quartile.place(relx = .8, rely = .55, relwidth = .18, relheight = .1)

            self.variance = Button(constant, text = "Variance",bg="gray",command = self.set_variance)
            self.variance.place(relx = .6, rely = .55, relwidth = .2, relheight = .1)

            self.std = Button(constant, text = "Standard Deviation",bg="gray",command = self.set_std)
            self.std.place(relx = .4, rely = .55, relwidth = .2, relheight = .1)

            self.cv = Button(constant, text ="Coefficient Variance",bg="gray",command = self.set_cv)
            self.cv.place(relx = .2, rely = .55, relwidth = .2, relheight = .1)

            lbv1=Label(window, text="Version: 1.01 09.11.2021", )
            lbv1.place(relx = .68, rely = .93,relwidth = .4, relheight = .05,)
            


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

    # window = Tk()
    # window.title("Project: Distribution Calculator with figure")
    def Poissondistribution():
        lamp = int(value1p.get())
        sizep = int(value2p.get())

        xp = random.poisson(lamp, sizep)
        sns.distplot(random.poisson(lamp, sizep), kde=False)
        plt.show()
        print(xp)

        t30.delete("1.0", END), t30.insert(END, xp)


    l00 = Label(window, text="Poisson Distribution: ", font=('Helvetica', 18, 'bold'))
    l10 = Label(window, text="lam - rate or known number")
    l11 = Label(window, text="Size - The shape of the returned array", )

    value1p = StringVar()
    value2p = StringVar()
    e20 = Entry(window, textvariable=value1p)
    ToolTip(e20, msg="lam - rate or known number")

    e21 = Entry(window, textvariable=value2p)
    ToolTip(e21, msg="Size - The shape of the returned array")



    b23 = Button(window, text="Claculate", command=Poissondistribution, bg="gray")


    l300 = Label(window, text="Result: ")
    t30 = Text(window, height=3, width=40)


    l00.grid(row=0, columnspan=2)
    l10.grid(row=1, column=0)
    l11.grid(row=1, column=1)
    e20.grid(row=2, column=0)
    e21.grid(row=2, column=1)
    b23.grid(row=2, column=4)
    l300.grid(row=4, columnspan=1)
    t30.grid(row=4, columnspan=4)




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

    b73 = Button(window, text="Claculate", command=binomialdistribution, bg="gray")

    l800 = Label(window, text="Result: ")
    t80 = Text(window, height=3, width=40)

    l50.grid(row=5, columnspan=2)
    l60.grid(row=6, column=0)
    l61.grid(row=6, column=1)
    l62.grid(row=6, column=2)
    e70.grid(row=7, column=0)
    e71.grid(row=7, column=1)
    e72.grid(row=7, column=2)
    b73.grid(row=7, column=4)
    l800.grid(row=8, columnspan=1)
    t80.grid(row=8, columnspan=4)




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
    l110 = Label(window, text="loc - (Mean)")
    l111 = Label(window, text="scale - (Standard Deviation)", )
    l112 = Label(window, text="Size A ")
    l113 = Label(window, text="Size B")

    value1n = StringVar()
    value2n = StringVar()
    value3n = StringVar()
    value4n = StringVar()
    e120 = Entry(window, textvariable=value1n)
    e121 = Entry(window, textvariable=value2n)
    e122 = Entry(window, textvariable=value3n, )
    e123 = Entry(window, textvariable=value4n, width=10)

    b123 = Button(window, text="Claculate", command=normaldistribution,  bg="gray" )

    l1300 = Label(window, text="Result: ")
    t130 = Text(window, height=4, width=40)

    l100.grid(row=10, columnspan=2)
    l110.grid(row=11, column=0)
    l111.grid(row=11, column=1)
    l112.grid(row=11, column=2)
    l113.grid(row=11, column=3)

    e120.grid(row=12, column=0)
    e121.grid(row=12, column=1)
    e122.grid(row=12, column=2)
    e123.grid(row=12, column=3)

    b123.grid(row=12, column=4)

    t130.grid(row=14, columnspan=4)

    l1300.grid(row=14, columnspan=1)
    t130.grid(row=14, columnspan=4)

    b143 = Button(window, text="Quit", command=quit, width=7, background="red",  )
    b143.grid(row=14, column=4)

    l1300 = Label(window, text=" ")
    l1300.grid(row=15, columnspan=1)



    window.mainloop()


def create_window3(title):
    window = tk.Toplevel(root)
    window.title(title)
    # window.geometry("200x200")
    # Creating main window
    # window = Tk()
    # window.title("Project-3: Correlation Analysis")

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

    # Action button
    b23 = Button(window, text="Claculate", command=correlation, bg="gray", )
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
    l100 = Label(window, text="Spearman's Correlation: ")
    b103 = Button(window, text="Quit", command=quit, width=10, background='blue')
    t100.grid(row=10, column=1)
    l100.grid(row=10, column=0)
    b103.grid(row=10, column=3)

    # Managing GUI Label, Entry, Button and Text as grid in row and column


    window.mainloop()

# Create the main window
root = tk.Tk()
root.minsize(450, 300)


frame = Frame(root, width=530, height=350)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open(
    "C:/Users/snawa/OneDrive/Documents/GitHub/pydataview/bg4.jpg"))
# Create a Label Widget to display the text or Image
label = Label(frame, image=img)
label.pack()

# Create the buttons
projectTitle1 = "Project-1: Measure of Central Tendency and Dispersion"
projectTitle2 = "Project-2: Distribution Calculator with figure"
projectTitle3 = "Project-3: Correlation Analysis"



# Set the window title and size
root.title("My App")
root.geometry("400x400")

# Create the buttons
button1 = tk.Button(root, text=projectTitle1, cursor="hand2", command=lambda: create_window1(projectTitle1), padx=20, pady=10, bg="#0099cc", fg="white", activebackground="#006699", activeforeground="white")
button2 = tk.Button(root, text=projectTitle2, cursor="hand2", command=lambda: create_window2(projectTitle2), padx=20, pady=10, bg="#cc0000", fg="white", activebackground="#990000", activeforeground="white")
button3 = tk.Button(root, text=projectTitle3, cursor="hand2", command=lambda: create_window3(projectTitle3), padx=20, pady=10, bg="#00cc00", fg="white", activebackground="#006600", activeforeground="white")

# Set the hover colors of the buttons
button1.bind("<Enter>", lambda e: button1.config(bg="#006699"))
button1.bind("<Leave>", lambda e: button1.config(bg="#0099cc"))
button2.bind("<Enter>", lambda e: button2.config(bg="#990000"))
button2.bind("<Leave>", lambda e: button2.config(bg="#cc0000"))
button3.bind("<Enter>", lambda e: button3.config(bg="#006600"))
button3.bind("<Leave>", lambda e: button3.config(bg="#00cc00"))

# Pack the buttons into the window
button1.place(relx=0.5, rely=0.3, anchor="center")
button2.place(relx=0.5, rely=0.5, anchor="center")
button3.place(relx=0.5, rely=0.7, anchor="center")

# Start the main event loop
root.mainloop()