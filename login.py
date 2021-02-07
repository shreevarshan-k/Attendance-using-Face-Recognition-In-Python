from tkinter import*
import os
from tkinter import messagebox
class Login:
     

        def __init__(self,root):
            self.root=root
            self.root.title("Login")
            self.root.geometry("1350x700+0+0")

            def function():
                    os.system("py firstpage.py")
            def function1():
                    os.system("py teacher.py")
            def loginp():
                    if self.uname.get()=="admin" or  self.pwd.get()=="rec":
                            function()
                    elif  self.uname.get()=="staff" or  self.pwd.get()=="id":
                            function1()
                    else:
                            print("error")
            self.uname=StringVar()
            self.pwd=StringVar()
            title=Label(self.root,text="Login",font=("times new roman",40,"bold"),bg="violet",fg="white")
            title.place(x=0,y=0,relwidth=1)

            Login_Frame=Frame(self.root,bg="violet")
            Login_Frame.place(x=400,y=150)

            username=Label(Login_Frame,text="Username",compound=LEFT,font=("times new roman",20,"bold"),bg="violet").grid(row=0,column=0,padx=20,pady=10)
            txtuser=Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15),text='str').grid(row=0,column=1,padx=20)
            

            password=Label(Login_Frame,text="Password",compound=LEFT,font=("times new roman",20,"bold"),bg="violet").grid(row=1,column=0,padx=20,pady=10)
            txtpwd=Entry(Login_Frame,bd=5,relief=GROOVE,textvariable=self.pwd,font=("",15),show="*").grid(row=1,column=1,padx=20)
        
            btn_log=Button(Login_Frame,text="Login",width=15,font=("times new roman",14,"bold"),bg="violet",fg="white",command=loginp).grid(row=2,column=1,pady=10)
           
root =Tk()
obj=Login(root)
root.mainloop()
