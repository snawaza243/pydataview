import builtins
from tkinter import*
from tkinter import font
from matplotlib import pyplot as plt
import seaborn as sns
from numpy import random
from tktooltip import ToolTip



#######
# @Title : Distribution Calculator
# @Author : Dr. Rajeev Gupta
# @Co-Author : Shahnawaz Alam(11202722)
# @Version : 1.00 29.12.2021
########


window = Tk()
window.title("Distribution Calculator with figure")
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
