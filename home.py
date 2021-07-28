import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from subprocess import call
from PIL import Image, ImageTk
import tkinter.font as tkFont
from tkinter import ttk
import discover
import playlist
from q2 import q
import fileinput
class home:
    money = 100
    count=0
    def __init__(self, root):
        #setting title
        #root.title("Dashboard")
        #setting window size
        home.read2=Button()
        home.read4=Button()
        home.bg = ImageTk.PhotoImage(file="N_Pics/libh.jpg")
        l1= Label(root,image=home.bg)
        l1.place(x=-80,y=0,width=1600,height=1200)
        l2=Label(root,image=home.bg)
        l2.place(x=0,y=1200,width=1600,height=1200)
        width=1600
        height=900
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        #root.geometry(alignstr)
        #root.resizable(width=True, height=True)
        home.co = ImageTk.PhotoImage(file="pics/c.jfif")
        ft = tkFont.Font(family='TimesNewRoman',size=10)
        coin = tk.Label(root,image=home.co)
        coin.place(x=780,y=90,width=80,height=30)
        num = tk.Label(root,text=r.coins,font=ft)
        num.place(x=870,y=90,width=30,height=30)
        num.configure(background="white")

        home.im2 = ImageTk.PhotoImage(file="N_Pics/button copy.png")
        homeButton=tk.Button(root,image=home.im2)
        homeButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        homeButton["font"] = ft
        homeButton["fg"] = "#000000"
        homeButton["justify"] = "center"
        homeButton["text"] = "Home"
        homeButton.place(x=100,y=75,width=112,height=40)

        home.im3 = ImageTk.PhotoImage(file="N_Pics/button-2 copy.png")
        playlistButton=tk.Button(root,image=home.im3)
        playlistButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        playlistButton["font"] = ft
        playlistButton["fg"] = "#000000"
        playlistButton["justify"] = "center"
        playlistButton["text"] = "My Playlist"
        playlistButton.place(x=374+100,y=75,width=165,height=40)
        playlistButton["command"] = self.playlistButton_command

        home.im4 = ImageTk.PhotoImage(file="N_Pics/button-3 copy.png")
        disButton=tk.Button(root,image=home.im4)
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



        home.b1 = ImageTk.PhotoImage(file="N_Pics/The Egg.jpg")
        book1ImageButton=tk.Button(root,image=home.b1)
        book1ImageButton.place(x=625,y=300,width=250,height=310)
        book1ImageButton["command"] = self.book1ImageButton_command

        im1 = Label(root,text="The story is about the main character, who is  (in the second person), "
                            "and God, who is  (in the first person). You, a 48-year-old man who dies in \n"
                            "a car crash, meet the narrator, who says that you have been reincarnated many "
                              "times before, and that you are next to be reincarnated as a Chinese peasant \n"
                              "girl in 540 AD. God then explains that you are, in fact, constantly reincarnated "
                              "across time, and that all human beings who have ever lived and will ever live are \n"
                              "incarnations of you. You remark about being Abraham Lincoln, Adolf Hitler and "
                              "Jesus, and God adds that you were also once John Wilkes Booth, every Holocaust \n"
                              "victim and every person who followed Jesus. God explains that in fact there are "
                              "other Godlike beings elsewhere, and that you too will one day become a God. \n"
                              "The entire universe was created as an egg for the main character (all of humanity), "
                              "and once you have lived every human life ever, you will be born as a God. The reason \n"
                              "God created the universe was for the main character, you, to understand this point: "
                              "Every time you victimized someone...you were victimizing yourself. Every act of \n"
                              "kindness you’ve done, you’ve done to yourself. Every happy and sad moment ever "
                              "experienced by any human was, or will be, experienced by you."
                            )
        im1.place(x=200,y=630,width=1100,height=150)
        a=10
        b=330
        c=250

        home.meat = ImageTk.PhotoImage(file="pics/m2.jpg")
        book2ImageButton=tk.Button(root,image=home.meat)
        book2ImageButton.place(x=650,y=810,width=182,height=270)
        book2ImageButton["command"] = self.book2ImageButton_command
        im2 = Label(root,text="The first being simply cannot believe that anything made of meat could be thinking, "
                              "feeling, or creating. The second being tells the first that they probed the lifeforms \n"
                              "and everything - including the brain - is made out of meat. In fact, these suspicious "
                              "creatures are ''...thinking meat! Conscious meat! Loving meat. Dreaming meat. \n"
                              "The meat is the whole deal!''When the first being finally understands that the meaty "
                              "creatures are a possibility, the second tells him that the meat has been trying to \n"
                              "communicate with them for almost 100 years.Again, the first being is amazed that meat "
                              "is able to not only communicate, but use tools and machines to do so. The second being \n"
                              "advises the first, both officially and unofficially, what to do with the meat. "
                              "Officially, the beings should welcome the meat creatures without prejudice. \n"
                              "Unofficially, however, the second being recommends forgetting all about them."
                              "At the end of the story, they close the case of the meat creatures and turn \n"
                              "their attention to other interesting things on that side of the galaxy. "
                              "A ''rather shy but sweet hydrogen core cluster intelligence in a class nine star \n"
                              "in G445 zone'' has reached out to them again. They're happy to reconnect: ''Imagine "
                              "how unbearably, how unutterably cold the Universe would be if one were all alone...''")
        im2.place(x=200,y=1110,width=1100,height=135)
        a=a+c+60
        c=185


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


    def playlistButton_command(self):
        r.root.destroy()
        pl = playlist.p(r.username)
        #exit()


    def disButton_command(self):
        r.root.destroy()
        de=discover.d(r.username)


    def close_command(self):
        exit()

    def inc(self):
        r.coins+=20
        ft = tkFont.Font(family='TimesNewRoman',size=10)

        num = tk.Label(r.second_frame,text=r.coins,font=ft)
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
                    if line.strip()==r.username:
                        flag=1
                        continue

                if flag==1:
                    flag+=1
                    print(line, end ='')
                    continue
                if flag==2:
                    print(r.coins, end ='\n')
                    flag=11
                    continue



    def playe(self,name):
        pl = q(name)

    def book1ImageButton_command(self):

        name = "The Egg"
        home.ln = ImageTk.PhotoImage(file="pics/l.png")
        home.read2 = tk.Button(r.second_frame,image=home.ln)
        home.read2.place(x=700,y=610,width=100,height=25)
        home.read2["command"] = lambda:[self.inc(),self.playe(name)]
        home.read4.place_forget()
        s="userdocs/"+r.username+"books.txt"
        try:
            file = open(s,"r")
            f=0
            for i in file:
                if i.strip()=="The Egg":
                    f=1
                    break
            if f!=1:
                file=open(s,"a")
                file.write("The Egg\n")
                file.close()

        except:
            file = open(s,"x")
            file=open(s,"a")
            file.write("The Egg\n")
            file.close()

    def book2ImageButton_command(self):
        home.read4=Button()
        name="They're made out of meat"
        home.ln = ImageTk.PhotoImage(file="pics/l.png")
        home.read4 = tk.Button(r.second_frame,image=home.ln)
        home.read4["command"] = lambda:[self.inc(),self.playe(name)]
        home.read4.place(x=700,y=1080,width=100,height=25)
        home.read2.place_forget()
        s="userdocs/"+r.username+"books.txt"
        try:
            file = open(s,"r")
            f=0
            for i in file:
                if i.strip()=="They're made out of meat":
                    f=1
                    break
            if f!=1:
                file=open(s,"a")
                file.write("They're made out of meat\n")
                file.close()

        except:
            file = open(s,"x")
            file=open(s,"a")
            file.write("They're made out of meat\n")
            file.close()




    def moreButton_command(self):

        lb=tk.Listbox(r.second_frame)
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
            r.root.destroy()
            call(["python","main.py"])
        elif selection[0]==1:
            r.root.destroy()
            de=(r.username)




class r:
    def __init__(self,username):
        r.username = username
        file = open("login_credentials.txt","r")
        flag=0
        r.coins=0
        for i,line in enumerate(file):
            if flag==0:
                if line.strip()==r.username:
                    flag=1
                    continue
            if flag==1:
                flag+=1
                continue
            if flag==2:
                r.coins = int(line.strip())
                break
                #r.coins=int(line.strip())
        file.close()
        r.root = tk.Tk()

        main_frame = Frame(r.root)
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
        r.second_frame = Frame(my_canvas)



        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0,0), window=r.second_frame, anchor="nw")
        h = home(r.second_frame)
        Label(r.second_frame).grid(row=0, column=0, pady=700, padx=1600)


        r.root.attributes('-fullscreen',True)
        r.root.mainloop()
