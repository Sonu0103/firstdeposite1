

from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
# from hotel import HotelManagementSystem


class Login_window:
    def __init__(self,rppt): 
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Acer\OneDrive\New folder\bg.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=500,y=150,width=350,height=450)

        img1=Image.open(r"C:\Users\Acer\OneDrive\New folder\295128.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=625,y=150,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        # labels 
        username=lbl=Label(frame,text="username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=50,y=140)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=20,y=170,width=270)
        
        password=lbl=Label(frame,text="password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=50,y=210)
        
        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=20,y=250,width=270)
      

         
        # login button
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=120,y=300,width=70,height=30)

        # registerbutton
        registerbtn=Button(frame,text="New User Register",font=("times new roman",15,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=10,y=330,width=160)
        
        #forgetpassword button
        registerbtn=Button(frame,text="Forget Password",font=("times new roman",15,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=8,y=360,width=160) 

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="sonu" and self.txtpass.get()=="ashi":
            messagebox.showinfo("Success","Welcome to hotel")
        else:
            messagebox.showerror("Invalid","Invalid username&password")


if __name__=="__main__":
    root=Tk()
    app=Login_window(root)
    root.mainloop()
    