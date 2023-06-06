from tkinter import *
import statistics as st
import numpy as np
from tkinter import font

# creating Main window 
window = Tk()
window.minsize(width=680,height=420)
window.title("Project-1: Measure of Central Tendancy and Dispersion")


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
