
import tkinter as tk
import tkinter.font as tkFont
from subprocess import call
from tkinter import *
from PIL import Image, ImageTk



class info:
    name=""
    age=""
    def __init__(self, root):
        #setting title
        root.title("Sign up")
        #setting window size
        width=599
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=True, height=True)

        info.bg4 = ImageTk.PhotoImage(file="N_Pics/Buttons/pexels-johannes-plenio-1103970.jpg")
        l1 = Label(root, image=info.bg4)
        l1.place(x=0, y=0, width=599, height=522)
        '''info.photo = PhotoImage(file="N_Pics/Buttons/pexels-fwstudio-129731.png")
        n_lable=Label(image=info.photo)
        n_lable.pack()'''



        ft = tkFont.Font(family='Times',size=18)
        GLabel_296=tk.Label(root)
        GLabel_296["font"] = ft
        GLabel_296["fg"] = "#333333"
        GLabel_296["justify"] = "center"
        GLabel_296["text"] = "Full Name:"
        GLabel_296.place(x=70,y=80,width=121,height=55)

        info.name = StringVar()
        ft = tkFont.Font(family='Times',size=15)
        GLineEdit_996=tk.Entry(root)
        GLineEdit_996["borderwidth"] = "1px"
        GLineEdit_996["font"] = ft
        GLineEdit_996["fg"] = "#333333"
        GLineEdit_996["justify"] = "center"
        GLineEdit_996["text"] = ""
        GLineEdit_996.place(x=210,y=90,width=124,height=30)
        GLineEdit_996.configure(textvariable=info.name)

        ft = tkFont.Font(family='Times',size=18)
        GLabel_203=tk.Label(root)
        GLabel_203["font"] = ft
        GLabel_203["fg"] = "#333333"
        GLabel_203["justify"] = "center"
        GLabel_203["text"] = "Age:"
        GLabel_203.place(x=100,y=150,width=70,height=25)

        info.age = IntVar()
        ft = tkFont.Font(family='Times',size=15)
        GLineEdit_593=tk.Entry(root)
        GLineEdit_593["borderwidth"] = "1px"
        GLineEdit_593["font"] = ft
        GLineEdit_593["fg"] = "#333333"
        GLineEdit_593["justify"] = "center"
        GLineEdit_593["text"] = ""
        GLineEdit_593.place(x=210,y=150,width=125,height=30)
        GLineEdit_593.configure(textvariable=info.age)

        ft = tkFont.Font(family='Times',size=18)
        GLabel_73=tk.Label(root)
        GLabel_73["font"] = ft
        GLabel_73["fg"] = "#333333"
        GLabel_73["justify"] = "center"
        GLabel_73["text"] = "Sex:"
        GLabel_73.place(x=100,y=210,width=70,height=25)

        sex=IntVar()
        ft = tkFont.Font(family='Times',size=13)
        GRadio_363=tk.Radiobutton(root)
        GRadio_363["font"] = ft
        GRadio_363["fg"] = "#333333"
        GRadio_363["justify"] = "center"
        GRadio_363["text"] = "Male"
        GRadio_363.place(x=190,y=210,width=85,height=25)
        GRadio_363["variable"] = sex
        GRadio_363["value"] = 3

        #GRadio_363["command"] = self.GRadio_363_command

        ft = tkFont.Font(family='Times',size=13)
        GRadio_631=tk.Radiobutton(root)
        GRadio_631["font"] = ft
        GRadio_631["fg"] = "#333333"
        GRadio_631["justify"] = "center"
        GRadio_631["text"] = "Female"
        GRadio_631.place(x=280,y=210,width=85,height=25)
        GRadio_631["variable"] = sex
        GRadio_631["value"] = 1
        #GRadio_631["command"] = self.GRadio_631_command

        ft = tkFont.Font(family='Times',size=13)
        GRadio_340=tk.Radiobutton(root)
        GRadio_340["font"] = ft
        GRadio_340["fg"] = "#333333"
        GRadio_340["justify"] = "center"
        GRadio_340["text"] = "Other"
        GRadio_340.place(x=370,y=210,width=85,height=25)
        GRadio_340["variable"] = sex
        GRadio_340["value"] = 2

        #GRadio_340["command"] = self.GRadio_340_command

        ft = tkFont.Font(family='Times',size=18)
        GLabel_729=tk.Label(root)
        GLabel_729["font"] = ft
        GLabel_729["fg"] = "#333333"
        GLabel_729["justify"] = "center"
        GLabel_729["text"] = "e-mail:"
        GLabel_729.place(x=90,y=270,width=70,height=25)

        ft = tkFont.Font(family='Times',size=13)
        GLineEdit_697=tk.Entry(root)
        GLineEdit_697["borderwidth"] = "1px"
        GLineEdit_697["font"] = ft
        GLineEdit_697["fg"] = "#333333"
        GLineEdit_697["justify"] = "center"
        GLineEdit_697["text"] = ""
        GLineEdit_697.place(x=210,y=270,width=373,height=30)
        #GLineEdit_697["validatecommand"] = "@"

        ft = tkFont.Font(family='Times',size=18)
        GLabel_26=tk.Label(root)
        GLabel_26["font"] = ft
        GLabel_26["fg"] = "#333333"
        GLabel_26["justify"] = "center"
        GLabel_26["text"] = "Favourite genre:"
        GLabel_26.place(x=0,y=330,width=194,height=30)

        ft = tkFont.Font(family='Times',size=13)
        GCheckBox_228=tk.Checkbutton(root)
        GCheckBox_228["font"] = ft
        GCheckBox_228["fg"] = "#333333"
        GCheckBox_228["justify"] = "center"
        GCheckBox_228["text"] = "Comedy"
        GCheckBox_228.place(x=210,y=330,width=80,height=31)
        GCheckBox_228["offvalue"] = "0"
        GCheckBox_228["onvalue"] = "1"
        #GCheckBox_228["command"] = self.GCheckBox_228_command

        ft = tkFont.Font(family='Times',size=13)
        GCheckBox_967=tk.Checkbutton(root)
        GCheckBox_967["font"] = ft
        GCheckBox_967["fg"] = "#333333"
        GCheckBox_967["justify"] = "center"
        GCheckBox_967["text"] = "Fiction"
        GCheckBox_967.place(x=300,y=330,width=70,height=25)
        GCheckBox_967["offvalue"] = "0"
        GCheckBox_967["onvalue"] = "1"
        #GCheckBox_967["command"] = self.GCheckBox_967_command

        ft = tkFont.Font(family='Times',size=13)
        GCheckBox_703=tk.Checkbutton(root)
        GCheckBox_703["font"] = ft
        GCheckBox_703["fg"] = "#333333"
        GCheckBox_703["justify"] = "center"
        GCheckBox_703["text"] = "Horror"
        GCheckBox_703.place(x=390,y=330,width=70,height=25)
        GCheckBox_703["offvalue"] = "0"
        GCheckBox_703["onvalue"] = "1"
        #GCheckBox_703["command"] = self.GCheckBox_703_command

        ft = tkFont.Font(family='Times',size=13)
        GCheckBox_130=tk.Checkbutton(root)
        GCheckBox_130["font"] = ft
        GCheckBox_130["fg"] = "#333333"
        GCheckBox_130["justify"] = "center"
        GCheckBox_130["text"] = "Sci-fi"
        GCheckBox_130.place(x=200,y=380,width=70,height=25)
        GCheckBox_130["offvalue"] = "0"
        GCheckBox_130["onvalue"] = "1"
        #GCheckBox_130["command"] = self.GCheckBox_130_command

        ft = tkFont.Font(family='Times',size=13)
        GCheckBox_402=tk.Checkbutton(root)
        GCheckBox_402["font"] = ft
        GCheckBox_402["fg"] = "#333333"
        GCheckBox_402["justify"] = "center"
        GCheckBox_402["text"] = "Romance"
        GCheckBox_402.place(x=300,y=380,width=84,height=30)
        GCheckBox_402["offvalue"] = "0"
        GCheckBox_402["onvalue"] = "1"
        #GCheckBox_402["command"] = self.GCheckBox_402_command

        ft = tkFont.Font(family='Times',size=13)
        GCheckBox_622=tk.Checkbutton(root)
        GCheckBox_622["font"] = ft
        GCheckBox_622["fg"] = "#333333"
        GCheckBox_622["justify"] = "center"
        GCheckBox_622["text"] = "Other"
        GCheckBox_622.place(x=400,y=380,width=84,height=30)
        GCheckBox_622["offvalue"] = "0"
        GCheckBox_622["onvalue"] = "1"
        #GCheckBox_622["command"] = self.GCheckBox_622_command

        ft = tkFont.Font(family='Times',size=13)
        GButton_806=tk.Button(root)
        GButton_806["bg"] = "#efefef"
        GButton_806["font"] = ft
        GButton_806["fg"] = "#000000"
        GButton_806["justify"] = "center"
        GButton_806["text"] = "Next"
        GButton_806.place(x=500,y=460,width=70,height=25)
        GButton_806["command"] = self.GButton_806_command





    def GButton_806_command(self):
        if info.name.get()=="":
            ft = tkFont.Font(family='Times',size=12)
            error = tk.Label(root,font=ft,text="Name can not be empty",fg="red")
            error.place(x=350,y=90,width=150,height=35)
        if info.age.get()==0:
            ft = tkFont.Font(family='Times',size=12)
            error = tk.Label(root,font=ft,text="Age can not be empty",fg="red")
            error.place(x=350,y=150,width=150,height=35)
        else:
            call(["python","userpass.py"])
            exit()

if __name__ == "__main__":
    root = tk.Tk()
    info = info(root)
    root.mainloop()
