from tkinter import *
from tkinter import font as f
import random
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image


class LandingPage(Frame):
    def __init__(self, master):
        super(LandingPage, self).__init__(master)
        self.master=master
        self.grid()
        self.font1=f.Font(family='Yu Gothic UI Light', size=40, weight='normal')
        self.font2 = f.Font(family='Yu Gothic UI Light', size=11, weight='normal')
        self.font3 = f.Font(family='Yu Gothic UI Light', size=18)
        self.font4 = f.Font(family='Yu Gothic UI Light', size=16)
        self.font5 = f.Font(family='Yu Gothic UI Light', size=11, weight='bold')
        self.blackcolor = '#080808'
        self.darkredcolor='#ED4B3A'
        self.redcolor = '#E50914'
        self.greycolor = '#242124'
        self.whitecolor = 'white'
        self.darkgreycolor = '#221F1F'
        self.lightgreycolor = '#8B8D97'
        self.nums={
            7: (0, 0), 8: (0, 1), 9: (0, 2),
            4: (1, 0), 5: (1, 1), 6: (1, 2),
            1: (2, 0), 2: (2, 1), 3: (2, 2),
            'AC': (3, 0), 0: (3, 1), 'x': (3, 2)
        }
        self.btn_num=list(self.nums)
        self.create_widgets()
        self.colorbind()

    def create_widgets(self):
        self.titlebar=Frame(self.master,bg=self.darkgreycolor)
        self.titlebar.grid(row=0,column=0)
        self.img = ImageTk.PhotoImage(Image.open("skull (1).png"))
        self.img1 = ImageTk.PhotoImage(Image.open("skull2.png"))
        self.img2 = ImageTk.PhotoImage(Image.open("close.png"))
        self.img3 = ImageTk.PhotoImage(Image.open("bones.png"))
        self.close=Button(self.titlebar,text='Q U I T',font=self.font2,cursor='hand2',border=0,bg=self.darkgreycolor,
                          fg=self.whitecolor,command=self.master.destroy)
        self.close.grid(row=0,column=2,padx=(640,5),pady=5)
        Frame(self.titlebar,height=30,width=3,bg=self.redcolor).grid(row=0,column=3)


        self.home=Frame(self.master,bg=self.darkgreycolor,width=700,height=400)
        self.home.grid(row=1,column=0)
        self.title = Label(self.home, text='D E A D  &  I N J U R E D', font=self.font1, fg=self.redcolor, bg=self.darkgreycolor)
        self.title.grid(row=0, column=0, sticky=NW, padx=69,columnspan=5,pady=(15,25))
        Label(self.home, image=self.img1, bg=self.darkgreycolor).grid(row=1, column=1, sticky=NE)
        Label(self.home, image=self.img2, bg=self.darkgreycolor).grid(row=1, column=2, sticky=N)
        Label(self.home, image=self.img3, bg=self.darkgreycolor).grid(row=1, column=3, sticky=NW)
        self.play=Button(self.home,text='P L A Y  N O W',font=self.font3,cursor='hand2',border=0,bg=self.darkgreycolor,
                          fg=self.redcolor,command=self.show_game)
        self.play.grid(row=2,column=2,sticky=N,pady=(25,0))
        Frame(self.home, height=3, width=145, bg=self.redcolor).grid(row=3, column=2, sticky=N)
        self.how=Button(self.home,text='H O W  T O  P L A Y ?',font=self.font2,cursor='hand2',border=0,bg=self.darkgreycolor,
                          fg=self.whitecolor,command=self.howtoplay)
        self.how.grid(row=3,column=2,sticky=N,pady=(40,0))
        Frame(self.home, height=1, width=100, bg=self.whitecolor).grid(row=4, column=2, sticky=N)


        self.game=Frame(self.master,bg=self.darkgreycolor,width=700,height=400)
        # self.game.grid(row=1,column=0)
        Label(self.game,text='E N T E R  G U E S S : ', font=self.font2, fg=self.whitecolor,
              bg=self.darkgreycolor).grid(row=0,column=0,pady=(10,0),padx=10,sticky=NW,columnspan=3)
        self.guess_ent=Entry(self.game,width=16,fg=self.whitecolor,bg=self.redcolor,font=self.font4,border=0)
        self.guess_ent.grid(row=1,column=0,padx=10,sticky=NW,pady=10,columnspan=3)

        line = 2
        self.bind_class("keystag", "<Enter>", self.keypadenter)
        self.bind_class("keystag", "<Leave>", self.keypadleave)
        for digit,val in self.nums.items():
            self.btns= Button(self.game, text=str(digit), width=5, pady=5, font=self.font2,
                                         cursor='hand2', bg=self.greycolor, fg=self.whitecolor,border=0,
                              command=lambda x=digit: self.keypad(x))
            new_tags = self.btns.bindtags() + ("keystag",)
            self.btns.bindtags(new_tags)
            self.btns.grid(row=line + val[0], column=val[1], sticky=W, padx=(10, 0), pady=5)

        self.submit_btn=Button(self.game,text='S U B M I T',font=self.font2,padx=51,pady=2,cursor='hand2',border=0,bg=self.redcolor,
                          fg=self.whitecolor,command=lambda: self.submit())
        self.submit_btn.grid(row=6,column=0,columnspan=3,sticky=NW,pady=(10,0),padx=10)

        Frame(self.game, height=330, width=1, bg=self.redcolor).grid(row=0, column=4,rowspan=7,pady=(10,0),padx=(50,65), sticky=N)

        self.table=Frame(self.game, height=330, width=300, bg=self.darkgreycolor)
        self.table.grid(row=0, column=5, rowspan=7, pady=(10,0),padx=(0,133), sticky=NW)
        Label(self.table, text='N U M B E R', font=self.font2, fg=self.whitecolor,
              bg=self.darkgreycolor).grid(row=0, column=0, padx=5, sticky=NW)
        Label(self.table, text='D E A D', font=self.font2, fg=self.redcolor,
              bg=self.darkgreycolor).grid(row=0, column=1, padx=5, sticky=NW)
        Label(self.table, text='I N J U R E D', font=self.font2, fg=self.whitecolor,
              bg=self.darkgreycolor).grid(row=0, column=2, padx=5, sticky=NW)
        self.tablerow=1
        Frame(self.game, height=310, width=1, bg=self.redcolor).place(x=407,y=10)
        Frame(self.game, height=310, width=1, bg=self.redcolor).place(x=474, y=10)
        Frame(self.game, height=1, width=248, bg=self.redcolor).place(x=320, y=37)

        self.go_home = Button(self.titlebar, text='H O M E', font=self.font2, cursor='hand2', border=0,
                              bg=self.darkgreycolor,
                              fg=self.whitecolor, command=lambda: self.show_home())
        self.newgame = Button(self.titlebar, text='N E W  G A M E', font=self.font2, cursor='hand2', border=0,
                              bg=self.redcolor,
                              fg=self.whitecolor, command=lambda: self.cleartable())

        self.tries=0
        self.keycount=0
        self.alpha=0

    def colorbind(self):
        self.bind_class("whitetag", "<Enter>", self.on_enter)
        self.bind_class("whitetag", "<Leave>", self.on_leave)
        self.bind_class("redtag", "<Enter>", self.red_enter)
        self.bind_class("redtag", "<Leave>", self.red_leave)
        self.play.bind('<Enter>',lambda e: self.playenter())
        self.play.bind('<Leave>', lambda e: self.playleave())
        whitewidget=[self.close,self.how,self.go_home]
        redwidget=[self.submit_btn,self.newgame]
        for i in whitewidget:
            new_tags = i.bindtags() + ("whitetag",)
            i.bindtags(new_tags)
        for i in redwidget:
            new_tags = i.bindtags() + ("redtag",)
            i.bindtags(new_tags)

    def on_enter(self,event):
        event.widget.config(fg=self.redcolor)

    def on_leave(self,event):
        event.widget.config(fg=self.whitecolor)

    def red_enter(self,event):
        event.widget.config(bg='#FF6863')

    def red_leave(self,event):
        event.widget.config(bg=self.redcolor)

    def playenter(self):
        self.play.config(fg=self.whitecolor)
    def playleave(self):
        self.play.config(fg=self.redcolor)

    def keypadenter(self,event):
        event.widget.config(bg=self.lightgreycolor)

    def keypadleave(self,event):
        event.widget.config(bg=self.greycolor)

    def keypad(self, n):
        if n=='AC':
            self.guess_ent.delete(0,END)
            self.keycount=0
        elif n=='x':
            if self.keycount==0:
                pass
            else:
                self.guess_ent.delete(self.keycount-1,END)
                self.keycount-=1
        else:
            if self.keycount<4:
                self.guess_ent.insert(END, n)
                self.keycount+=1
            else:
                messagebox.showerror('Error','Max numbers reached')

    def validate(self,guess):
        for i in guess:
            if i.isalpha()==True:
                self.alpha+=1
        if self.alpha>0:
            messagebox.showerror('Error', 'Invalid input\nPlease input a 4-digit number')
            self.alpha=0
        if len(guess)!=4:
            messagebox.showerror('Error','Invalid number\nPlease input a 4-digit number')
        else:
            if not len(set(guess))==len(guess):
                messagebox.showerror('Error','a number has been repeated')
            else:
                return True
    def cleartable(self):
        self.table.destroy()
        self.randnum = random.sample(range(10), 4)
        int((''.join([str(x) for x in self.randnum])))
        print(self.randnum)
        self.table = Frame(self.game, height=330, width=300, bg=self.darkgreycolor)
        self.table.grid(row=0, column=5, rowspan=7, pady=10, padx=(0, 133), sticky=NW)
        Label(self.table, text='N U M B E R', font=self.font2, fg=self.whitecolor,
              bg=self.darkgreycolor).grid(row=0, column=0, padx=5, sticky=NW)
        Label(self.table, text='D E A D', font=self.font2, fg=self.redcolor,
              bg=self.darkgreycolor).grid(row=0, column=1, padx=5, sticky=NW)
        Label(self.table, text='I N J U R E D', font=self.font2, fg=self.whitecolor,
              bg=self.darkgreycolor).grid(row=0, column=2, padx=5, sticky=NW)
        self.tablerow = 1
        Frame(self.game, height=310, width=1, bg=self.redcolor).place(x=407, y=10)
        Frame(self.game, height=310, width=1, bg=self.redcolor).place(x=474, y=10)
        Frame(self.game, height=1, width=248, bg=self.redcolor).place(x=320, y=37)


    def compare(self,guess):
        count=0
        count2=0
        for i in range(len(self.randnum)):
            if str(self.randnum[i])==guess[i]:
                count+=1

        for x in str(self.randnum):
            for y in guess:
                if x==y:
                    count2+=1
        val=[count,count2-count]
        print(val)
        return val

    def results(self,guess,val):
        Label(self.table, text=guess, font=self.font2, fg=self.whitecolor,
              bg=self.darkgreycolor).grid(row=self.tablerow, column=0, padx=5,pady=5, sticky=NW)
        Label(self.table, text=str(val[0]), font=self.font2, fg=self.redcolor,
              bg=self.darkgreycolor).grid(row=self.tablerow, column=1, padx=5,pady=5,  sticky=NW)
        Label(self.table, text=str(val[1]), font=self.font2, fg=self.whitecolor,
              bg=self.darkgreycolor).grid(row=self.tablerow, column=2, padx=5,pady=5,  sticky=NW)
        self.tablerow+=1

    def submit(self):
        guess=self.guess_ent.get()
        validate=self.validate(guess)
        if validate:
            value=self.compare(guess)
            self.results(guess,value)
            self.keypad('AC')
            self.tries+=1
            if value[0]!=4 and self.tries==6:
                messagebox.showerror('YOU LOSE!', f'YOU LOSE!\nWinning number: {guess}')
                self.tries = 0
            if value[0]==4:
                messagebox.showinfo('YOU WIN!!!', f'YOU WIN!!!\nWinning number: {guess}')
                self.tries=0


    def show_game(self):
        self.home.grid_forget()
        self.game.grid(row=1,column=0)
        self.cleartable()
        self.go_home.grid(row=0,column=0,sticky=NW,pady=5,padx=(10,5))
        self.newgame.grid(row=0,column=1,sticky=NW,pady=5,padx=(0,455))
        self.close.grid_configure(padx=(0, 5))

    def show_home(self):
        self.game.grid_forget()
        self.home.grid(row=1,column=0)
        self.go_home.grid_forget()
        self.newgame.grid_forget()
        self.close.grid_configure(padx=(640,5))

    def howtoplay(self):
        self.howto = Toplevel(self.master)
        self.howto.resizable(0, 0)
        app_width = 332
        app_height = 300
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.howto.title("H O W  T O  P L A Y ?")
        self.howto.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        apk = Howto(self.howto)

class Howto(Frame):
    def __init__(self, main):
        super(Howto, self).__init__(main)
        self.main = main
        self.font1=f.Font(family='Yu Gothic UI Light', size=14, weight='normal')
        self.whitecolor = 'white'
        self.darkgreycolor = '#221F1F'
        self.grid()
        self.text='Dead and injured is a guessing game,\nthe goal is to guess a 4-digit number\n in six or less attempts. ' \
                  '\nThe number must not contain repetitions\n of the same digits, and must be 4-digits,\nno more,no less.' \
                  '\nWhen any of the digits in your guess\n is in the number and are in the\n correct position, the AI returns "dead",' \
                  '\nelse, if any digit is in the number\n but not in the correct position,\n the AI returns "Injured", Good Luck. '
        Label(self.main, text=self.text,font=self.font1, bg=self.darkgreycolor,fg=self.whitecolor).grid(row=0,column=0)



def land():
    root = Tk()
    root.resizable(0, 0)
    root.configure(bg='#221F1F')
    root.geometry('700x400+333+184')
    root.overrideredirect(1)
    apk = LandingPage(root)
    apk.mainloop()
# land()