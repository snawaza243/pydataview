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

#######
# @Title : Correlation Analysis
# @Author : Dr. Rajeev Gupta
# @Co-Author : Shahnawaz Alam(11202722)
# @Version : 1.00 29.12.2021
########

# Creating main window
window = Tk()
window.title("Project-3: Correlation Analysis")

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
