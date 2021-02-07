
from tkinter import *
import os
from datetime import datetime;

root=Tk()

root.configure(background="white")

#root.geometry("300x300")

def function1():
    
    os.system("py Creater.py")
    
def function2():
    
    os.system("py trainer.py")

def function3():

    os.system("py Recog_original.py")

def function4():
    os.system("py mail.py") 
    

def function6():

    root.destroy()

def attend():
    os.startfile(os.getcwd()+"/firebase/attendance_files/attendance"+str(datetime.now().date())+'.xls')


root.title("AUTOMATIC FACE RECOGNITION ATTENDANCE SYSTEM")


Label(root, text="AUTOMATIC  ATTENDANCE SYSTEM USING FACE RECOGNITION",font=("Blackletter",20),fg="white",bg="violet",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


Button(root,text="Create Dataset",font=("times new roman",20),bg="white",fg='violet',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)


Button(root,text="Train Dataset",font=("Decorative",20),bg="violet",fg='white',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Recognize",font=('times new roman',20),bg="white",fg="violet",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Attendance Sheet",font=('Decorative',20),bg="violet",fg="white",command=attend).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Mail",font=('Decorative',20),bg="white",fg="violet",command=function4).grid(row=7,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


Button(root,text="Exit",font=('times new roman',20),bg="black",fg="white",command=function6).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
