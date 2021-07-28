import tkinter as tk
from tkinter import *
import sys
import os
import tkinter.font as tkFont
from PIL import Image, ImageTk
from subprocess import call
sys.path.append(".")
from home import r
class login:
    us=""
    pa=""

    def __init__(self, root):
        #setting title
        root.title("Login Page")
        #setting window size
        width=530
        height=412
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(background="pink")
        login.bg = ImageTk.PhotoImage(file="N_Pics/Buttons/pexels-johannes-plenio-1103970.jpg")
        l1 = Label(root, image=login.bg,)
        l1.place(x=0, y=0, width=530, height=422)




        """ft = tkFont.Font(family='Times',size=18)
        userLabel=tk.Label(root,font=ft,justify="center",text="Username:")
        userLabel.place(x=100,y=120,width=105,height=30)"""

        login.bg2 = ImageTk.PhotoImage(file="N_Pics/button.png")
        l1 = Label(root, image=login.bg2)
        l1.place(x=100, y=120, width=140, height=35)


        login.us = StringVar()
        ft = tkFont.Font(family='Times',size=10)
        userValue=tk.Entry(root,borderwidth="0px",font=ft,justify="center")
        userValue.place(x=260,y=120,width=157,height=35)
        userValue.configure(textvariable=login.us)

        """ft = tkFont.Font(family='Times',size=18)
        passLabel=tk.Label(root,font=ft,justify="center",text="Password:")
        passLabel.place(x=100,y=200,width=105,height=30)"""

        login.bg3 = ImageTk.PhotoImage(file="N_Pics/PassWord.png")
        l1 = Label(root, image=login.bg3 )
        l1.place(x=100, y=200, width=140, height=35)

        login.pa = StringVar()
        ft = tkFont.Font(family='Times',size=10)
        passValue=tk.Entry(root,font=ft,borderwidth="0px",justify="center",show="*")
        passValue.place(x=260,y=200,width=157,height=35)
        passValue.configure(textvariable=login.pa)


        login.im = ImageTk.PhotoImage(file="N_Pics/button-3.png")
        log=tk.Button(root,font=ft,justify="center",text="Login",command=self.login_command,image=login.im)
        log.place(x=150, y=280, width=110, height=30)

        """login.bg4 = ImageTk.PhotoImage(file="N_Pics/button-3.png")
        l1 = Label(root, image=login.bg4)
        l1.place(x=150, y=280, width=110, height=30)"""

        login.im2 = ImageTk.PhotoImage(file="N_Pics/button-2.png")
        sign=tk.Button(root,font=ft,justify="center",text="Sign up",command=self.sign_command,image=login.im2)
        sign.place(x=270,y=280,width=110,height=30)

        """login.bg5 = ImageTk.PhotoImage(file="N_Pics/button-2.png")
        l1 = Label(root, image=login.bg5)
        l1.place(x=270, y=280, width=110, height=30)"""

        log=tk.Button(root, font=ft, justify="center", text="Login", command=self.login_command)
        log.place(x=150, y=1330, width=70, height=25)


    def login_command(self):
        file = open("login_credentials.txt","r")
        flag=0
        for i,line in enumerate(file):
            if i%3==0:
            #if flag!=1:
                if line.strip() == login.us.get():
                    flag=1
                    continue
            if flag==1:
                flag=0
                if line.strip()==login.pa.get():
                    flag=11
                    root.destroy()
                    #h = home(root)
                    file.close()

                    h=r(login.us.get())
                    break
                    #call(["python","home.py"])

        if flag!=11:
            ft = tkFont.Font(family='Times',size=12)
            error = tk.Label(root,text="Login credentials did not match. Try again")
            error.place(x=0,y=35,width=530,height=27)


    def sign_command(self):
        call(["python","info.py"])








root = tk.Tk()

login = login(root)

root.mainloop()
