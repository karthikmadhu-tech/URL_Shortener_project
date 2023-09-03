import pyshorteners
from tkinter import *

win = Tk()
win.geometry("400x270")
win.configure(bg="pink")
#button function
def short():
    url= entry1.get()
    s = pyshorteners.Shortener().tinyurl.short(url)

    entry2.insert(END,s)

#label for entering user url
Label(win, text= "Enter your URL link ", font="impack 17 bold", bg="black", fg="white").pack(fill="x")
Label(win, text= "by Karthik Madhu ", font="impack 10 ", bg="black", fg="white").pack(fill="x")

#entry box
entry1 = Entry(win, font="10",bg="white",fg="blue", bd=3,width =40)
entry1.pack(pady=30)
#button
Button(win,text = "Click Me", font ="impack 12 bold", bg="white",fg="red", command = short).pack()
#entry2
entry2 = Entry(win, font="impack 16 bold",bg="pink", fg="blue" ,bd= 0,width =24)
entry2.pack(pady=30)


mainloop()
