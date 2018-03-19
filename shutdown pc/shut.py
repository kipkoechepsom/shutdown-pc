#clylinder operations
from tkinter import *
import sys
import os

root = Tk()
root.title("AUTOMATIC SHUTDOWN")
root.configure(bg="blue")
root.minsize(400,300)
root.maxsize(500,400)


def shut15():
    os.system("shutdown -s -t  900")
    return
def shut30():
    os.system("shutdown -s -t 1800")
    return   
def shut45():
    os.system("shutdown -s -t 2700")
    return  
def shut60():
    os.system("shutdown -s -t 3600")
    return
def cancel():
    os.system("shutdown -a")
    return 

def shutnow():
    os.system("shutdown -s -t 1")
    return

#frame 000
topframe0 = Frame(root,bd=20)
topframe0.pack(side=TOP)
topframe0.configure(bg="blue")

label = Label(topframe0,text="AUTOMATIC SHUTDOWN AFTER",foreground="white",font="Courier",bg="blue")
label.pack(side=LEFT)

#frame four
topframe3 = Frame(root,bd=20)
topframe3.pack(side=TOP)
topframe3.configure(bg="blue")



but = Button(topframe3,text="15 mins",command=shut15,bd=6,foreground="white",font="Courier",bg="blue")
but.pack(side=LEFT)

but = Button(topframe3,text="30 mins",command=shut30,bd=6,foreground="white",font="Courier",bg="blue")
but.pack(side=LEFT)

but = Button(topframe3,text="45 mins",command=shut45,bd=6,foreground="white",font="Courier",bg="blue")
but.pack(side=LEFT)

but = Button(topframe3,text="60 mins",command=shut60,bd=6,foreground="white",font="Courier",bg="blue")
but.pack(side=LEFT)

#frame five
topframe4 = Frame(root,bd=20)
topframe4.pack(side=TOP)
topframe4.configure(bg="blue")

but = Button(topframe4,text="SHUT NOW",command=shutnow,bd=5,foreground="white",font="Courier",bg="blue")
but.pack(side=LEFT)

but = Button(topframe4,text="Cancel",command=cancel,bd=5,foreground="white",font="Courier",bg="blue")
but.pack(side=LEFT)



topframe45 = Frame(root,bd=20)
topframe45.pack(side=TOP)
topframe45.configure(bg="blue")

label = Label(topframe45,text="courtesy of kipkoechepsom@2017",foreground="#FFD4FF",font="Courier",bg="blue")
label.pack(side=LEFT)
root.mainloop()
