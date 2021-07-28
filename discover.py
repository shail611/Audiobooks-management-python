import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from subprocess import call
from PIL import Image, ImageTk
import fileinput
import home
from q2 import q
import playlist
class discover:
    count=0
    def __init__(self, root):
        #setting title
        #root.title("Dashboard")
        #setting window size
        discover.ln = ImageTk.PhotoImage(file="pics/l.png")
        discover.read1 = tk.Button(d.second_frame,image=discover.ln)
        discover.read2 = tk.Button(d.second_frame,image=discover.ln)
        discover.read3 = tk.Button(d.second_frame,image=discover.ln)
        discover.read4 = tk.Button(d.second_frame,image=discover.ln)
        discover.read5 = tk.Button(d.second_frame,image=discover.ln)
        discover.read6 = tk.Button(d.second_frame,image=discover.ln)
        discover.read7 = tk.Button(d.second_frame,image=discover.ln)
        discover.read8 = tk.Button(d.second_frame,image=discover.ln)
        discover.read9 = tk.Button(d.second_frame,image=discover.ln)
        discover.read10 = tk.Button(d.second_frame,image=discover.ln)
        discover.read11 = tk.Button(d.second_frame,image=discover.ln)
        discover.read12 = tk.Button(d.second_frame,image=discover.ln)
        discover.read13 = tk.Button(d.second_frame,image=discover.ln)
        discover.read14 = tk.Button(d.second_frame,image=discover.ln)
        discover.read15 = tk.Button(d.second_frame,image=discover.ln)
        discover.read16 = tk.Button(d.second_frame,image=discover.ln)
        discover.read17 = tk.Button(d.second_frame,image=discover.ln)
        discover.read18 = tk.Button(d.second_frame,image=discover.ln)

        discover.bg = ImageTk.PhotoImage(file="N_Pics/lib2.jpg")
        l1= Label(root,image=discover.bg)
        l1.place(x=0,y=0,width=1600,height=1600)
        width=1600
        height=900
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        #root.geometry(alignstr)
        #root.resizable(width=True, height=True)
        discover.co = ImageTk.PhotoImage(file="pics/c.jfif")
        ft = tkFont.Font(family='TimesNewRoman',size=10)
        coin = tk.Label(root,image=discover.co)
        coin.place(x=780,y=90,width=80,height=30)
        num = tk.Label(root,text=d.coins,font=ft)
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
        homeButton["command"]=self.homeButton_command

        home.im3 = ImageTk.PhotoImage(file="N_Pics/button-2 copy.png")
        playlistButton = tk.Button(root,image= home.im3)
        playlistButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        playlistButton["font"] = ft
        playlistButton["fg"] = "#000000"
        playlistButton["justify"] = "center"
        playlistButton["text"] = "My Playlist"
        playlistButton.place(x=374+100,y=75,width=165,height=40)
        playlistButton["command"] = self.playlistButton_command

        home.im4 = ImageTk.PhotoImage(file="N_Pics/button-3 copy.png")
        disButton = tk.Button(root,image= home.im4)
        disButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        disButton["font"] = ft
        disButton["fg"] = "#000000"
        disButton["justify"] = "center"
        disButton["text"] = "Discover"
        disButton.place(x=374*2+300,y=75,width=160,height=40)


        moreButton=tk.Button(root)
        moreButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        moreButton["font"] = ft
        moreButton["fg"] = "#000000"
        moreButton["justify"] = "center"
        moreButton["text"] = "More"
        moreButton.place(x=374*3+280,y=20,width=70,height=30)
        moreButton["command"] = self.moreButton_command

        discover.b1 = ImageTk.PhotoImage(file="N_Pics/The Egg.jpg")
        book1ImageButton=tk.Button(root,image=discover.b1)
        book1ImageButton.place(x=10,y=330,width=250,height=310)
        book1ImageButton["command"] = self.book1ImageButton_command
        a=10
        b=330
        c=250

        discover.meat = ImageTk.PhotoImage(file="pics/m2.JPG")
        book2ImageButton=tk.Button(root,image=discover.meat)
        book2ImageButton.place(x=a+c+60,y=b,width=185,height=270)
        book2ImageButton["command"] = self.book2ImageButton_command
        a=a+c+60
        c=185


        book3ImageButton=tk.Button(root)
        book3ImageButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        book3ImageButton["font"] = ft
        book3ImageButton["fg"] = "#000000"
        book3ImageButton["justify"] = "center"
        book3ImageButton["text"] = "a story without title"
        discover.b3 = ImageTk.PhotoImage(file="N_Pics/A story without title.png")
        book3ImageButton = tk.Button(root, image=discover.b3)
        book3ImageButton.place(x=a+c+60,y=b,width=200,height=270)
        book3ImageButton["command"] = self.book3ImageButton_command
        a=a+c+60
        c=200

        book4ImageButton=tk.Button(root)
        book4ImageButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        book4ImageButton["font"] = ft
        book4ImageButton["fg"] = "#000000"
        book4ImageButton["justify"] = "center"
        book4ImageButton["text"] = "A Tent In Agony"
        discover.b4 = ImageTk.PhotoImage(file="N_Pics/A Tent In Agony.jpg")
        book4ImageButton = tk.Button(root, image=discover.b4)
        book4ImageButton.place(x=a+c+60,y=b,width=200,height=270)
        book4ImageButton["command"] = self.book4ImageButton_command
        a=a+c+50
        c=200

        book5ImageButton=tk.Button(root)
        book5ImageButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        book5ImageButton["font"] = ft
        book5ImageButton["fg"] = "#000000"
        book5ImageButton["justify"] = "center"
        book5ImageButton["text"] = "A Terrible Thing Has Happened"
        discover.b5 = ImageTk.PhotoImage(file="N_Pics/A Terrible Thing Has Happened.jpg")
        book5ImageButton = tk.Button(root, image=discover.b5)
        book5ImageButton.place(x=a+c+60,y=b,width=200,height=270)
        book5ImageButton["command"] = self.book5ImageButton_command
        a=a+c+50
        c=200

        book6ImageButton=tk.Button(root)
        book6ImageButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        book6ImageButton["font"] = ft
        book6ImageButton["fg"] = "#000000"
        book6ImageButton["justify"] = "center"
        book6ImageButton["text"] = "Case Closed"
        discover.b6 = ImageTk.PhotoImage(file="N_Pics/Case Closed.jpg")
        book6ImageButton = tk.Button(root, image=discover.b6)
        book6ImageButton.place(x=a+c+60,y=b,width=200,height=270)
        book6ImageButton["command"] = self.book6ImageButton_command
        a=a+c+50
        c=200
        b=800
        book7ImageButton=tk.Button(root,text="destiny")
        discover.b7 = ImageTk.PhotoImage(file="N_Pics/destiny.jpg")
        book7ImageButton = tk.Button(root, image=discover.b7)
        book7ImageButton.place(x=10,y=b,width=250,height=310)
        book7ImageButton["command"] = self.book7ImageButton_command
        a=10
        b=800
        c=250

        book8ImageButton=tk.Button(root,text="Fall Of the Stars")
        discover.b8 = ImageTk.PhotoImage(file="N_Pics/Fall Of the Stars.jpg")
        book8ImageButton = tk.Button(root, image=discover.b8)
        book8ImageButton.place(x=a+c+60,y=b,width=185,height=270)
        book8ImageButton["command"] = self.book8ImageButton_command
        a=a+c+60
        c=185


        book9ImageButton=tk.Button(root)
        book9ImageButton["bg"] = "#efefef"
        ft =tkFont.Font(family='Times',size=10)
        book9ImageButton["font"] = ft
        book9ImageButton["fg"] = "#000000"
        book9ImageButton["justify"] = "center"
        book9ImageButton["text"] = "Infinity "
        discover.b9 = ImageTk.PhotoImage(file="N_Pics/Infinity.jpg")
        book9ImageButton = tk.Button(root, image=discover.b9)
        book9ImageButton.place(x=a+c+60,y=b,width=200,height=270)
        book9ImageButton["command"] = self.book9ImageButton_command
        a=a+c+60
        c=200

        book10ImageButton=tk.Button(root)
        book10ImageButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        book10ImageButton["font"] = ft
        book10ImageButton["fg"] = "#000000"
        book10ImageButton["justify"] = "center"
        book10ImageButton["text"] = "Margaret's Perfume"
        discover.b10 = ImageTk.PhotoImage(file="N_Pics/Margaret's Perfume2.jpg")
        book10ImageButton = tk.Button(root, image=discover.b10)
        book10ImageButton.place(x=a+c+60,y=b,width=200,height=270)
        book10ImageButton["command"] = self.book10ImageButton_command
        a=a+c+50
        c=200

        book11ImageButton=tk.Button(root)
        book11ImageButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        book11ImageButton["font"] = ft
        book11ImageButton["fg"] = "#000000"
        book11ImageButton["justify"] = "center"
        book11ImageButton["text"] = "Mind Games"
        discover.b11 = ImageTk.PhotoImage(file="N_Pics/Mind Games.jpg")
        book11ImageButton = tk.Button(root, image=discover.b11)
        book11ImageButton.place(x=a+c+60,y=b,width=200,height=270)
        book11ImageButton["command"] = self.book11ImageButton_command
        a=a+c+50
        c=200

        book12ImageButton=tk.Button(root)
        book12ImageButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        book12ImageButton["font"] = ft
        book12ImageButton["fg"] = "#000000"
        book12ImageButton["justify"] = "center"
        book12ImageButton["text"] = "Scared to Death to Live"
        discover.b12 = ImageTk.PhotoImage(file="N_Pics/Scared to Death to Live.jpg")
        book12ImageButton = tk.Button(root, image=discover.b12)
        book12ImageButton.place(x=a+c+60,y=b,width=200,height=270)
        book12ImageButton["command"] = self.book12ImageButton_command
        a=a+c+50
        c=200

        book13ImageButton=tk.Button(root,text="the aged mother")
        discover.b13 = ImageTk.PhotoImage(file="N_Pics/the aged mother.jpg")
        book13ImageButton = tk.Button(root, image=discover.b13)
        book13ImageButton.place(x=10,y=1200,width=250,height=310)
        book13ImageButton["command"] = self.book13ImageButton_command
        a=10
        b=1200
        c=250

        book14ImageButton=tk.Button(root,text="The Busy Over Gate")
        discover.b14 = ImageTk.PhotoImage(file="N_Pics/The Busy Over Gate.jpg")
        book14ImageButton = tk.Button(root, image=discover.b14)
        book14ImageButton.place(x=a+c+60,y=b,width=185,height=270)
        book14ImageButton["command"] = self.book14ImageButton_command
        a=a+c+60
        c=185


        book15ImageButton=tk.Button(root)
        book15ImageButton["bg"] = "#efefef"
        ft =tkFont.Font(family='Times',size=10)
        book15ImageButton["font"] = ft
        book15ImageButton["fg"] = "#000000"
        book15ImageButton["justify"] = "center"
        book15ImageButton["text"] = "the golden windows"
        discover.b15 = ImageTk.PhotoImage(file="N_Pics/the golden windows.jpg")
        book15ImageButton = tk.Button(root, image=discover.b15)
        book15ImageButton.place(x=a+c+60,y=b,width=200,height=270)
        book15ImageButton["command"] = self.book15ImageButton_command
        a=a+c+60
        c=200

        book16ImageButton=tk.Button(root)
        book16ImageButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        book16ImageButton["font"] = ft
        book16ImageButton["fg"] = "#000000"
        book16ImageButton["justify"] = "center"
        book16ImageButton["text"] = "the last dream of olad oak"
        discover.b16 = ImageTk.PhotoImage(file="N_Pics/the last dream of olad oak.jpg")
        book16ImageButton = tk.Button(root, image=discover.b16)
        book16ImageButton.place(x=a+c+60,y=b,width=200,height=270)
        book16ImageButton["command"] = self.book16ImageButton_command
        a=a+c+50
        c=200

        if d.coins>200:

            book17ImageButton=tk.Button(root)
            book17ImageButton["bg"] = "#efefef"
            ft = tkFont.Font(family='Times',size=10)
            book17ImageButton["font"] = ft
            book17ImageButton["fg"] = "#000000"
            book17ImageButton["justify"] = "center"
            book17ImageButton["text"] = "The Last Gift"
            discover.b17 = ImageTk.PhotoImage(file="N_Pics/The Last Gift.jpg")
            book17ImageButton = tk.Button(root, image=discover.b17)
            book17ImageButton.place(x=a+c+60,y=b,width=200,height=270)
            book17ImageButton["command"] = self.book17ImageButton_command
        else:
            book17ImageButton=tk.Button(root)
            book17ImageButton["bg"] = "#efefef"
            ft = tkFont.Font(family='Times',size=10)
            book17ImageButton["font"] = ft
            book17ImageButton["fg"] = "#000000"
            book17ImageButton["justify"] = "center"
            book17ImageButton["text"] = "Unlocked at 200+ Coins"
            book17ImageButton.place(x=a+c+60,y=b,width=200,height=270)

        a=a+c+50
        c=200
        if d.coins>300:

            book18ImageButton=tk.Button(root)
            book18ImageButton["bg"] = "#efefef"
            ft = tkFont.Font(family='Times',size=10)
            book18ImageButton["font"] = ft
            book18ImageButton["fg"] = "#000000"
            book18ImageButton["justify"] = "center"
            book18ImageButton["text"] = "The Luck of Roaring Camp"
            discover.b18 = ImageTk.PhotoImage(file="N_Pics/The Luck of Roaring Camp.jpg")
            book18ImageButton = tk.Button(root, image=discover.b18)
            book18ImageButton.place(x=a+c+60,y=b,width=200,height=270)
            book18ImageButton["command"] = self.book18ImageButton_command
        else:
            book18ImageButton=tk.Button(root)
            book18ImageButton["bg"] = "#efefef"
            ft = tkFont.Font(family='Times',size=10)
            book18ImageButton["font"] = ft
            book18ImageButton["fg"] = "#000000"
            book18ImageButton["justify"] = "center"
            book18ImageButton["text"] = "Unlocked at 300+ Coins"
            #discover.b18 = ImageTk.PhotoImage(file="N_Pics/The Luck of Roaring Camp.jpg")
            #book18ImageButton = tk.Button(root, image=discover.b18)
            book18ImageButton.place(x=a+c+60,y=b,width=200,height=270)
        a=a+c+50
        c=200

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
        d.root.destroy()
        h=home.r(d.username)
        #exit()

    def playlistButton_command(self):
        d.root.destroy()
        pl=playlist.p(d.username)
        #exit()
    def close_command(self):
        exit()

    def playe(self,name):
        pl = q(name)


    def check(self,bname):
        s="userdocs/"+d.username+"books.txt"
        try:
            file = open(s,"r")
            f=0
            for i in file:
                if i.strip()==bname:
                    f=1
                    break
            if f!=1:
                file=open(s,"a")
                file.write(bname+"\n")
                file.close()

        except:
            file = open(s,"x")
            file=open(s,"a")
            file.write(bname+"\n")
            file.close()

    def inc(self):
        d.coins+=20
        ft = tkFont.Font(family='TimesNewRoman',size=10)

        num = tk.Label(d.second_frame,text=d.coins,font=ft)
        num.place(x=870,y=90,width=30,height=30)
        num.configure(background="white")
        filename = "login_credentials.txt"

        with fileinput.FileInput(filename,inplace = True,backup=".bak") as f:
            flag=0
            for i,line in enumerate(f):
                if flag==11:
                    print(line,end='')
                    continue
                if flag==0:

                    print(line, end ='')
                    if line.strip()==d.username:
                        flag=1
                        continue

                if flag==1:
                    flag+=1
                    print(line, end ='')
                    continue
                if flag==2:
                    print(d.coins, end ='\n')
                    flag=11
                    continue


    def book1ImageButton_command(self):
        name="The Egg"
        discover.read1 = tk.Button(d.second_frame,image=discover.ln)

        discover.read1["command"] = lambda:[self.inc(),self.playe(name),self.check(name)]
        discover.read1.place(x=75,y=640,width=100,height=25)
        self.forget(1)



    def book2ImageButton_command(self):
        name="They're made out of meat"

        discover.read2 = tk.Button(d.second_frame,image=discover.ln)
        discover.read2.place(x=360,y=600,width=100,height=25)
        discover.read2["command"] = lambda:[self.inc(),self.playe(name),self.check(name)]
        self.forget(2)

    def book3ImageButton_command(self):
        name="a story without title"
        discover.read3 = tk.Button(d.second_frame,image=discover.ln)
        discover.read3.place(x=610,y=600,width=100,height=25)
        discover.read3["command"] = lambda:[self.inc(),self.playe(name),self.check(name)]
        self.forget(3)



    def book4ImageButton_command(self):
        name="A Tent In Agony"
        discover.read4 = tk.Button(d.second_frame,image=discover.ln)
        discover.read4.place(x=870,y=600,width=100,height=25)
        discover.read4["command"] = lambda:[self.inc(),self.playe(name),self.check(name)]
        self.forget(4)


    def book5ImageButton_command(self):
        name="A Terrible Thing Has Happened"
        discover.read5 = tk.Button(d.second_frame,image=discover.ln)
        discover.read5.place(x=1125,y=600,width=100,height=25)
        discover.read5["command"] = lambda:[self.inc(),self.playe(name),self.check(name)]
        self.forget(5)


    def book6ImageButton_command(self):
        name="Case Closed"
        discover.read6 = tk.Button(d.second_frame,image=discover.ln)
        discover.read6.place(x=1375,y=600,width=100,height=25)
        discover.read6["command"] = lambda:[self.inc(),self.playe(name),self.check(name)]
        self.forget(6)


    def book7ImageButton_command(self):
        name="destiny"
        discover.read7 = tk.Button(d.second_frame,image=discover.ln)
        discover.read7.place(x=75,y=1110,width=100,height=25)
        discover.read7["command"] = lambda:[self.inc(),self.playe(name),self.check(name)]
        self.forget(7)


    def book8ImageButton_command(self):
        name="Fall Of the Stars"

        discover.read8 = tk.Button(d.second_frame,image=discover.ln)
        discover.read8.place(x=360,y=1070,width=100,height=25)
        discover.read8["command"] = lambda:[self.inc(),self.playe(name),self.check(name)]
        self.forget(8)


    def book9ImageButton_command(self):
        name="Infinity"

        discover.read9 = tk.Button(d.second_frame,image=discover.ln)
        discover.read9.place(x=610,y=1070,width=100,height=25)
        discover.read9["command"] = lambda:[self.inc(),self.playe(name),self.check(name)]
        self.forget(9)


    def book10ImageButton_command(self):
        name="Margaret's Perfume"

        discover.read10 = tk.Button(d.second_frame,image=discover.ln)
        discover.read10.place(x=880,y=1070,width=100,height=25)
        discover.read10["command"] = lambda:[self.inc(),self.playe(name),self.check(name)]
        self.forget(10)


    def book11ImageButton_command(self):
        name="Mind Games"

        discover.read11 = tk.Button(d.second_frame,image=discover.ln)
        discover.read11.place(x=1135,y=1070,width=100,height=25)
        discover.read11["command"] = lambda:[self.inc(),self.playe(name),self.check(name)]
        self.forget(11)


    def book12ImageButton_command(self):
        name="Scared to Death to Live"

        discover.read12 = tk.Button(d.second_frame,image=discover.ln)
        discover.read12.place(x=1375,y=1070,width=100,height=25)
        discover.read12["command"] = lambda:[self.inc(),self.playe(name),self.check(name)]
        self.forget(12)


    def book13ImageButton_command(self):
        name="the aged mother"

        discover.read13 = tk.Button(d.second_frame,image=discover.ln)
        discover.read13.place(x=75,y=1510,width=100,height=25)
        discover.read13["command"] = lambda:[self.inc(),self.playe(name),self.check(name)]
        self.forget(13)


    def book14ImageButton_command(self):
        name="The Busy Over Gate"

        discover.read14 = tk.Button(d.second_frame,image=discover.ln)
        discover.read14.place(x=360,y=1470,width=100,height=25)
        discover.read14["command"] = lambda:[self.inc(),self.playe(name),self.check(name)]
        self.forget(14)


    def book15ImageButton_command(self):
        name="the golden windows"

        discover.read15 = tk.Button(d.second_frame,image=discover.ln)
        discover.read15.place(x=610,y=1470,width=100,height=25)
        discover.read15["command"] = lambda:[self.inc(),self.playe(name),self.check(name)]
        self.forget(15)


    def book16ImageButton_command(self):
        name="the last dream of olad oak"

        discover.read16 = tk.Button(d.second_frame,image=discover.ln)
        discover.read16.place(x=880,y=1470,width=100,height=25)
        discover.read16["command"] = lambda:[self.inc(),self.playe(name),self.check(name)]
        self.forget(16)

    def book17ImageButton_command(self):
        name="The Last Gift"

        discover.read17 = tk.Button(d.second_frame,image=discover.ln)
        discover.read17.place(x=1135,y=1470,width=100,height=25)
        discover.read17["command"] = lambda:[self.inc(),self.playe(name),self.check(name)]
        self.forget(17)



    def book18ImageButton_command(self):
        name="The Luck of Roaring Camp"

        discover.read18 = tk.Button(d.second_frame,image=discover.ln)
        discover.read18.place(x=1375,y=1470,width=100,height=25)
        discover.read18["command"] = lambda:[self.inc(),self.playe(name),self.check(name)]
        self.forget(18)

    def forget(self,n):
        if n!=1:
            discover.read1.place_forget()
        if n!=2:
            discover.read2.place_forget()
        if n!=3:
            discover.read3.place_forget()
        if n!=4:
            discover.read4.place_forget()
        if n!=5:
            discover.read5.place_forget()
        if n!=6:
            discover.read6.place_forget()
        if n!=7:
            discover.read7.place_forget()
        if n!=8:
            discover.read8.place_forget()
        if n!=9:
            discover.read9.place_forget()
        if n!=10:
            discover.read10.place_forget()
        if n!=11:
            discover.read11.place_forget()
        if n!=12:
            discover.read12.place_forget()
        if n!=13:
            discover.read13.place_forget()
        if n!=14:
            discover.read14.place_forget()
        if n!=15:
            discover.read15.place_forget()
        if n!=16:
            discover.read16.place_forget()
        if n!=17:
            discover.read17.place_forget()
        if n!=18:
            discover.read18.place_forget()

    def moreButton_command(self):

        lb=tk.Listbox(d.second_frame)
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
            d.root.destroy()
            call(["python","main.py"])

class d:
    def __init__(self,username):
        d.username = username
        file = open("login_credentials.txt","r")
        flag=0
        d.coins=0
        for i,line in enumerate(file):
            if flag==0:
                if line.strip()==username:
                    flag=1
                    continue
            if flag==1:
                flag+=1
                continue
            if flag==2:
                d.coins = int(line.strip())
                break
        file.close()
        d.root = Tk()
        main_frame = Frame(d.root)
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
        d.second_frame = Frame(my_canvas)



        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0,0), window=d.second_frame, anchor="nw")
        dis = discover(d.second_frame)
        Label(d.second_frame).grid(row=0, column=0, pady=780, padx=1600)


        d.root.attributes('-fullscreen',True)

        d.root.mainloop()
