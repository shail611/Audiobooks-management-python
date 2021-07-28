import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from subprocess import call
from PIL import Image, ImageTk
import tkinter.font as tkFont
from tkinter import ttk
import discover
import home
from q2 import q
import fileinput
class playlist:
    money = 100
    count=0
    def __init__(self, root):
        #setting title
        #root.title("Dashboard")
        #setting window size

        home.bg = ImageTk.PhotoImage(file="pics/shelf.JPG")
        l1= Label(root,image=home.bg)
        l1.place(x=0,y=0,width=1600,height=850)
        l2=Label(root,image=home.bg)
        l2.place(x=0,y=850,width=1600,height=850)
        width=1600
        height=900
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        #root.geometry(alignstr)
        #root.resizable(width=True, height=True)
        s = "userdocs/" + p.username + "books.txt"
        try:
            f = open(s, "r")
            data = f.read()
            if data=="":
                data = "You have not listened to any books yet."
                ft = tkFont.Font(family='Times', size=25)
                im1 = Label(root, text=data,font=ft)
                im1.place(x=400, y=230, width=700, height=350)
            else:
                ft = tkFont.Font(family='Times', size=25)
                im1 = Label(root, text=data,font=ft)
                im1.place(x=400, y=230, width=700, height=350)
        except:
            f = open(s,"x")
            data = "You have not listened to any books yet."
            ft = tkFont.Font(family='Times', size=25)
            im1 = Label(root, text=data,font=ft)
            im1.place(x=400, y=230, width=700, height=350)




        home.co = ImageTk.PhotoImage(file="pics/c.jfif")
        ft = tkFont.Font(family='TimesNewRoman',size=10)
        coin = tk.Label(root,image=home.co)
        coin.place(x=780,y=90,width=80,height=30)
        num = tk.Label(root,text=p.coins,font=ft)
        num.place(x=870,y=90,width=30,height=30)
        num.configure(background="white")

        home.im2 = ImageTk.PhotoImage(file="N_Pics/button copy.png")
        homeButton = tk.Button(root, image=home.im2)
        homeButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        homeButton["font"] = ft
        homeButton["fg"] = "#000000"
        homeButton["justify"] = "center"
        homeButton["text"] = "Home"
        homeButton.place(x=100,y=75,width=112,height=40)
        homeButton["command"] = self.homeButton_command

        home.im3 = ImageTk.PhotoImage(file="N_Pics/button-2 copy.png")
        playlistButton = tk.Button(root, image=home.im3)
        playlistButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        playlistButton["font"] = ft
        playlistButton["fg"] = "#000000"
        playlistButton["justify"] = "center"
        playlistButton["text"] = "My Playlist"
        playlistButton.place(x=374+100,y=75,width=165,height=40)
        #playlistButton["command"] = self.playlistButton_command

        home.im4 = ImageTk.PhotoImage(file="N_Pics/button-3 copy.png")
        disButton = tk.Button(root, image=home.im4)
        disButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        disButton["font"] = ft
        disButton["fg"] = "#000000"
        disButton["justify"] = "center"
        disButton["text"] = "Discover"
        disButton.place(x=374*2+300,y=75,width=160,height=40)
        disButton["command"] = self.disButton_command


        moreButton=tk.Button(root)
        moreButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        moreButton["font"] = ft
        moreButton["fg"] = "#000000"
        moreButton["justify"] = "center"
        moreButton["text"] = "More"
        moreButton.place(x=374*3+280,y=20,width=70,height=30)
        moreButton["command"] = self.moreButton_command

        """home.bgc = ImageTk.PhotoImage(file="pics/l3.JPG")
        noUseButton=tk.Button(root,image=home.bgc)
        #noUseButton["bg"] = "yellow"
        ft = tkFont.Font(family='Times',size=10)
        noUseButton["font"] = ft
        #noUseButton["fg"] = "#000000"
        noUseButton["justify"] = "center"
        #noUseButton["text"] = ""
        noUseButton.place(x=0,y=156,width=1600,height=500)"""


        close=tk.Button(root)
        close["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        close["font"] = ft
        close["fg"] = "#000000"
        close["justify"] = "center"
        close["text"] = " X "
        close.place(x=1490,y=0,width=30,height=30)
        close.configure(background="red")
        close["command"] = self.close_command


    def homeButton_command(self):
        p.root.destroy()
        ho=home.r(p.username)
        #exit()


    def disButton_command(self):
        p.root.destroy()
        de=discover.d(p.username)


    def close_command(self):
        exit()



    def moreButton_command(self):

        lb=tk.Listbox(p.second_frame)
        lb["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        lb["font"] = ft
        lb["fg"] = "#333333"
        lb["justify"] = "center"
        lb.place(x=374*3+280,y=55,width=87,height=90)
        lb["listvariable"] = "lb"
        lb.delete(0, tk.END)
        lb.insert(1,"Coins")
        lb.insert(2,"Best of 2021")
        lb.insert(3,"About Us")
        lb.insert(4,"Logout")
        lb.bind("<Double-Button-1>",self.double)

    def double(self,event):
        widget = event.widget
        selection=widget.curselection()
        if selection[0]==3:
            p.root.destroy()
            call(["python","main.py"])
        elif selection[0]==1:
            p.root.destroy()
            de=discover.d(p.username)




class p:
    def __init__(self,username):
        p.username = username
        file = open("login_credentials.txt","r")
        flag=0
        p.coins=0
        for i,line in enumerate(file):
            if flag==0:
                if line.strip()==p.username:
                    flag=1
                    continue
            if flag==1:
                flag+=1
                continue
            if flag==2:
                p.coins = int(line.strip())
                break
                #p.coins=int(line.strip())
        file.close()
        p.root = tk.Tk()

        main_frame = Frame(p.root)
        main_frame.pack(fill=BOTH, expand=1)

        # Create A Canvas
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        p.second_frame = Frame(my_canvas)



        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0,0), window=p.second_frame, anchor="nw")
        pl = playlist(p.second_frame)
        Label(p.second_frame).grid(row=0, column=0, pady=700, padx=1600)


        p.root.attributes('-fullscreen',True)
        p.root.mainloop()
