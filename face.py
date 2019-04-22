from tkinter import *
top = Tk()
top.title('The Main Window')
top.geometry("500x500")
top.resizable(0,0)

def print_content():
    global data 
    global data2 
    content = data.get()
    content2 = data2.get()
    
    print ('Name of Patient    : ',content) 
    print ('Purpose of Patient : ',content2) 

data = StringVar() 
data2 = StringVar()

Label(top,text="Name of Patient : ").grid(row=1,sticky=W)
Entry(top,textvariable=data).grid(row=1,column=1)

Label(top,text="PRPS of Patient :").grid(row=2,sticky=W)
Entry(top,textvariable=data2).grid(row=2,column=1)

b1 = Button(top,text="continue",command=print_content)
b1.grid(row=4,column=1)

top.mainloop()