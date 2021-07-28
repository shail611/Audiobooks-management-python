#from PIL import Image, ImageTk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from subprocess import call
from PIL import Image, ImageTk
import info
class userpass():
    user=""
    pa=""
    cpa=""
    def __init__(self, root):
        #setting title
        root.title("Credentials")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        userpass.bg1 = ImageTk.PhotoImage(file="N_Pics/Buttons/blur.jpg")
        l1 = Label(root, image=userpass.bg1)
        l1.place(x=0, y=0, width=600, height=500)

        userpass.bg2 = ImageTk.PhotoImage(file="N_Pics/button.png")
        l1=tk.Label(root,image=userpass.bg2)
        ft = tkFont.Font(family='Times',size=18)
        l1["font"] = ft
        l1["fg"] = "#333333"
        l1["justify"] = "center"
        l1["text"] = "Username:"
        l1.place(x=80,y=90,width=138,height=41)


        userpass.user = StringVar()
        uvalue=tk.Entry(root)
        uvalue["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=13)
        uvalue["font"] = ft
        uvalue["fg"] = "#333333"
        uvalue["justify"] = "center"
        uvalue["text"] = ""
        uvalue.configure(textvariable=userpass.user)
        uvalue.place(x=280,y=100,width=157,height=30)

        userpass.bg4 = ImageTk.PhotoImage(file="N_Pics/PassWord.png")
        l2=tk.Label(root,image=userpass.bg4)
        ft = tkFont.Font(family='Times',size=18)
        l2["font"] = ft
        l2["fg"] = "#333333"
        l2["justify"] = "center"
        l2["text"] = "Password:"
        l2.place(x=90,y=190,width=140,height=35)

        l3=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        l3["font"] = ft
        l3["fg"] = "#333333"
        l3["justify"] = "center"
        l3["text"] = "Confirm Password:"
        l3.place(x=40,y=300,width=215,height=40)

        userpass.pa=StringVar()
        pvalue=tk.Entry(root)
        pvalue["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        pvalue["font"] = ft
        pvalue["fg"] = "#333333"
        pvalue["justify"] = "center"
        pvalue["text"] = ""
        pvalue.configure(textvariable=userpass.pa)
        pvalue.place(x=280,y=190,width=160,height=35)

        userpass.cpa = StringVar()
        cpvalue=tk.Entry(root)
        cpvalue["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        cpvalue["font"] = ft
        cpvalue["fg"] = "#333333"
        cpvalue["justify"] = "center"
        cpvalue["text"] = ""
        cpvalue.configure(textvariable=userpass.cpa)
        cpvalue.place(x=280,y=300,width=173,height=30)

        userpass.check=tk.Button(root)
        userpass.check["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=13)
        userpass.check["font"] = ft
        userpass.check["fg"] = "#000000"
        userpass.check["justify"] = "center"
        userpass.check["text"] = "Check and finish"
        userpass.check.place(x=260,y=410,width=140,height=25)
        userpass.check["command"] = self.check_command



    def check_command(self):

        if userpass.pa.get()!=userpass.cpa.get() or userpass.pa.get()=="":
            ft = tkFont.Font(family='Times',size=14)
            error = tk.Label(root,font=ft,text="Passwords didn't match.")
            error.place(x=200,y=350,width=200,height=35)
            error = tk.Label(root,text="")
            error.place(x=250,y=140,width=200,height=35)
        else:
            error = tk.Label(root,text="")
            error.place(x=200,y=350,width=200,height=35)
            error = tk.Label(root,text="")
            error.place(x=250,y=140,width=200,height=35)
            flag=0
            if userpass.user.get()=="":
                ft = tkFont.Font(family='Times',size=14)
                error = tk.Label(root,font=ft,text="Username empty")
                error.place(x=250,y=140,width=200,height=35)
            else:

                file = open("login_credentials.txt","r")
                for i in file:
                    if i.strip() == userpass.user.get():
                        ft = tkFont.Font(family='Times',size=12)
                        error = tk.Label(root,font=ft,text="Username already taken")
                        error.place(x=250,y=140,width=200,height=35)
                        flag=1
                        file.close()
                        break
                if flag==0:
                    error = tk.Label(root,text="")
                    error.place(x=250,y=140,width=200,height=35)
                    f=open("login_credentials.txt","a")
                    str = userpass.user.get()+"\n"+userpass.pa.get()+"\n"
                    f.write(str)
                    f.write("100\n")
                    exit()



root = tk.Tk()
userpass = userpass(root)
root.mainloop()
