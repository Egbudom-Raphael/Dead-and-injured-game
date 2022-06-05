from tkinter.ttk import Progressbar
from tkinter import *
from tkinter import font as f
from tkinter import ttk
import time
from main import *

class Splashscreen(Frame):
    def __init__(self, master):
        super(Splashscreen, self).__init__(master)
        self.grid()
        self.slide = 0
        self.font1 = f.Font(family='Yu Gothic UI Light', size=20, weight='normal')
        self.font2 = f.Font(family='Yu Gothic UI Light', size=11, weight='normal')
        self.font3 = f.Font(family='Yu Gothic UI Light', size=18)
        self.font4 = f.Font(family='Yu Gothic UI Light', size=16)
        self.font5 = f.Font(family='Yu Gothic UI Light', size=11, weight='bold')
        self.blackcolor = '#080808'
        self.darkredcolor = '#ED4B3A'
        self.redcolor = '#E50914'
        self.greycolor = '#242124'
        self.whitecolor = 'white'
        self.darkgreycolor = '#221F1F'
        self.lightgreycolor = '#8B8D97'
        self.s=ttk.Style()
        self.create_widgets()



    def create_widgets(self):
        self.img1 = ImageTk.PhotoImage(Image.open("skull2.png"))
        self.img2 = ImageTk.PhotoImage(Image.open("close.png"))
        self.img3 = ImageTk.PhotoImage(Image.open("bones.png"))
        self.f1=Frame(self,bg=self.darkgreycolor)
        self.f1.grid(row=0,column=0)
        self.title = Label(self.f1, text='D E A D  &  I N J U R E D', font=self.font1, fg=self.redcolor,
                           bg=self.darkgreycolor)
        self.title.grid(row=0, column=0, sticky=NW, padx=20, columnspan=5, pady=(15, 25))
        Label(self.f1, image=self.img1, bg=self.darkgreycolor).grid(row=1, column=1, sticky=NE)
        Label(self.f1, image=self.img2, bg=self.darkgreycolor).grid(row=1, column=2, sticky=N)
        Label(self.f1, image=self.img3, bg=self.darkgreycolor).grid(row=1, column=3, sticky=NW)
        self.s.theme_use('clam')
        self.s.configure("red.Horizontal.TProgressbar", foreground=self.darkgreycolor, background=self.redcolor,relief='flat')
        self.progress = Progressbar(self, style="red.Horizontal.TProgressbar", orient=HORIZONTAL, length=322,mode='determinate')
        self.progress.grid(row=1,column=0)
        self.load=Label(self.f1, text='', bg=self.darkgreycolor,font=self.font2, fg=self.whitecolor)
        self.load.grid(row=3, column=2, pady=20)
        self.after(2000, self.bar)

    def bar(self):
        self.timer=0
        for i in range(110):
            self.progress['value']=self.timer
            self.update_idletasks()
            time.sleep(0.03)
            self.timer+=1
        self.master.destroy()
        land()


if __name__=="__main__":
    root = Tk()
    root.resizable(0, 0)
    app_width=322
    app_height=233
    screen_width=root.winfo_screenwidth()
    screen_height=root.winfo_screenheight()
    x= (screen_width/2) - (app_width/2)
    y= (screen_height/2) - (app_height/2)
    root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    root.overrideredirect(1)
    app = Splashscreen(root)
    app.mainloop()