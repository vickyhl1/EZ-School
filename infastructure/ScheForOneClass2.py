#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0
#  in conjunction with Tcl version 8.6
#    Dec 31, 2020 02:38:04 PM +0200  platform: Windows NT

import sys
import pymongo


sys.path.append('..')
from data import Schedule_db_init
Schedule_db_init()
client = pymongo.MongoClient()
mydb = client['EZSchooldb']
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import ScheForOneClass2_support
import classesSche

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = classes_Sche2 (root)
    ScheForOneClass2_support.init(root, top)
    root.mainloop()

w = None
def create_classes_Sche2(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_classes_Sche2(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = classes_Sche2 (w)
    ScheForOneClass2_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_classes_Sche2():
    global w
    w.destroy()
    w = None

class classes_Sche2:
    def Back(self):
        root.destroy()
        classesSche.vp_start_gui()
    def Lesson(self,nameday,index):
        global mydb
        userobj = mydb['ScheduleClasses'].find_one({'name':'class2'})
        msg= ((userobj[nameday][index]))
        return msg
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x443+385+120")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(0,  0)
        top.title("מערכת שעות כיתה ב")
        top.configure(background="#d9ffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.back = tk.Button(top)
        self.back.place(x=40, y=384, height=44, width=117)
        self.back.configure(activebackground="#ececec")
        self.back.configure(activeforeground="#000000")
        self.back.configure(background="#00eaea")
        self.back.configure(disabledforeground="#a3a3a3")
        self.back.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.back.configure(foreground="#000000")
        self.back.configure(highlightbackground="#d9d9d9")
        self.back.configure(highlightcolor="black")
        self.back.configure(pady="0")
        self.back.configure(text='''חזרה לכיתות''')
        self.back.configure(command=self.Back)

        self.Message1 = tk.Message(top)
        self.Message1.place(x=140, y=20, height=32, width=310)
        self.Message1.configure(background="#d9ffff")
        self.Message1.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''מערכת שעות כיתה ב''')
        self.Message1.configure(width=310)

        self.sunday1 = tk.Button(top)
        self.sunday1.place(x=450, y=90, height=34, width=77)
        self.sunday1.configure(activebackground="#ececec")
        self.sunday1.configure(activeforeground="#000000")
        self.sunday1.configure(background="#a6ffff")
        self.sunday1.configure(disabledforeground="#a3a3a3")
        self.sunday1.configure(foreground="#000000")
        self.sunday1.configure(highlightbackground="#d9d9d9")
        self.sunday1.configure(highlightcolor="black")
        self.sunday1.configure(pady="0")

        self.sunday2 = tk.Button(top)
        self.sunday2.place(x=450, y=140, height=34, width=77)
        self.sunday2.configure(activebackground="#ececec")
        self.sunday2.configure(activeforeground="#000000")
        self.sunday2.configure(background="#a6ffff")
        self.sunday2.configure(disabledforeground="#a3a3a3")
        self.sunday2.configure(foreground="#000000")
        self.sunday2.configure(highlightbackground="#d9d9d9")
        self.sunday2.configure(highlightcolor="black")
        self.sunday2.configure(pady="0")

        self.sunday5 = tk.Button(top)
        self.sunday5.place(x=450, y=290, height=34, width=77)
        self.sunday5.configure(activebackground="#ececec")
        self.sunday5.configure(activeforeground="#000000")
        self.sunday5.configure(background="#a6ffff")
        self.sunday5.configure(disabledforeground="#a3a3a3")
        self.sunday5.configure(foreground="#000000")
        self.sunday5.configure(highlightbackground="#d9d9d9")
        self.sunday5.configure(highlightcolor="black")
        self.sunday5.configure(pady="0")

        self.sunday3 = tk.Button(top)
        self.sunday3.place(x=450, y=190, height=34, width=77)
        self.sunday3.configure(activebackground="#ececec")
        self.sunday3.configure(activeforeground="#000000")
        self.sunday3.configure(background="#a6ffff")
        self.sunday3.configure(disabledforeground="#a3a3a3")
        self.sunday3.configure(foreground="#000000")
        self.sunday3.configure(highlightbackground="#d9d9d9")
        self.sunday3.configure(highlightcolor="black")
        self.sunday3.configure(pady="0")

        self.monday1 = tk.Button(top)
        self.monday1.place(x=330, y=90, height=34, width=77)
        self.monday1.configure(activebackground="#ececec")
        self.monday1.configure(activeforeground="#000000")
        self.monday1.configure(background="#a6ffff")
        self.monday1.configure(disabledforeground="#a3a3a3")
        self.monday1.configure(foreground="#000000")
        self.monday1.configure(highlightbackground="#d9d9d9")
        self.monday1.configure(highlightcolor="black")
        self.monday1.configure(pady="0")

        self.tuesday1 = tk.Button(top)
        self.tuesday1.place(x=230, y=90, height=34, width=77)
        self.tuesday1.configure(activebackground="#ececec")
        self.tuesday1.configure(activeforeground="#000000")
        self.tuesday1.configure(background="#a6ffff")
        self.tuesday1.configure(disabledforeground="#a3a3a3")
        self.tuesday1.configure(foreground="#000000")
        self.tuesday1.configure(highlightbackground="#d9d9d9")
        self.tuesday1.configure(highlightcolor="black")
        self.tuesday1.configure(pady="0")

        self.sunday4 = tk.Button(top)
        self.sunday4.place(x=450, y=240, height=34, width=77)
        self.sunday4.configure(activebackground="#ececec")
        self.sunday4.configure(activeforeground="#000000")
        self.sunday4.configure(background="#a6ffff")
        self.sunday4.configure(disabledforeground="#a3a3a3")
        self.sunday4.configure(foreground="#000000")
        self.sunday4.configure(highlightbackground="#d9d9d9")
        self.sunday4.configure(highlightcolor="black")
        self.sunday4.configure(pady="0")

        self.wednesday1 = tk.Button(top)
        self.wednesday1.place(x=120, y=90, height=34, width=77)
        self.wednesday1.configure(activebackground="#ececec")
        self.wednesday1.configure(activeforeground="#000000")
        self.wednesday1.configure(background="#a6ffff")
        self.wednesday1.configure(disabledforeground="#a3a3a3")
        self.wednesday1.configure(foreground="#000000")
        self.wednesday1.configure(highlightbackground="#d9d9d9")
        self.wednesday1.configure(highlightcolor="black")
        self.wednesday1.configure(pady="0")

        self.thursday1 = tk.Button(top)
        self.thursday1.place(x=20, y=90, height=34, width=77)
        self.thursday1.configure(activebackground="#ececec")
        self.thursday1.configure(activeforeground="#000000")
        self.thursday1.configure(background="#a6ffff")
        self.thursday1.configure(disabledforeground="#a3a3a3")
        self.thursday1.configure(foreground="#000000")
        self.thursday1.configure(highlightbackground="#d9d9d9")
        self.thursday1.configure(highlightcolor="black")
        self.thursday1.configure(pady="0")

        self.monday2 = tk.Button(top)
        self.monday2.place(x=330, y=140, height=34, width=77)
        self.monday2.configure(activebackground="#ececec")
        self.monday2.configure(activeforeground="#000000")
        self.monday2.configure(background="#a6ffff")
        self.monday2.configure(disabledforeground="#a3a3a3")
        self.monday2.configure(foreground="#000000")
        self.monday2.configure(highlightbackground="#d9d9d9")
        self.monday2.configure(highlightcolor="black")
        self.monday2.configure(pady="0")

        self.monday3 = tk.Button(top)
        self.monday3.place(x=330, y=190, height=34, width=77)
        self.monday3.configure(activebackground="#ececec")
        self.monday3.configure(activeforeground="#000000")
        self.monday3.configure(background="#a6ffff")
        self.monday3.configure(disabledforeground="#a3a3a3")
        self.monday3.configure(foreground="#000000")
        self.monday3.configure(highlightbackground="#d9d9d9")
        self.monday3.configure(highlightcolor="black")
        self.monday3.configure(pady="0")

        self.monday4 = tk.Button(top)
        self.monday4.place(x=330, y=240, height=34, width=77)
        self.monday4.configure(activebackground="#ececec")
        self.monday4.configure(activeforeground="#000000")
        self.monday4.configure(background="#a6ffff")
        self.monday4.configure(disabledforeground="#a3a3a3")
        self.monday4.configure(foreground="#000000")
        self.monday4.configure(highlightbackground="#d9d9d9")
        self.monday4.configure(highlightcolor="black")
        self.monday4.configure(pady="0")

        self.monday5 = tk.Button(top)
        self.monday5.place(x=330, y=290, height=34, width=77)
        self.monday5.configure(activebackground="#ececec")
        self.monday5.configure(activeforeground="#000000")
        self.monday5.configure(background="#a6ffff")
        self.monday5.configure(disabledforeground="#a3a3a3")
        self.monday5.configure(foreground="#000000")
        self.monday5.configure(highlightbackground="#d9d9d9")
        self.monday5.configure(highlightcolor="black")
        self.monday5.configure(pady="0")

        self.tuesday2 = tk.Button(top)
        self.tuesday2.place(x=230, y=140, height=34, width=77)
        self.tuesday2.configure(activebackground="#ececec")
        self.tuesday2.configure(activeforeground="#000000")
        self.tuesday2.configure(background="#a6ffff")
        self.tuesday2.configure(disabledforeground="#a3a3a3")
        self.tuesday2.configure(foreground="#000000")
        self.tuesday2.configure(highlightbackground="#d9d9d9")
        self.tuesday2.configure(highlightcolor="black")
        self.tuesday2.configure(pady="0")

        self.tuesday3 = tk.Button(top)
        self.tuesday3.place(x=230, y=190, height=34, width=77)
        self.tuesday3.configure(activebackground="#ececec")
        self.tuesday3.configure(activeforeground="#000000")
        self.tuesday3.configure(background="#a6ffff")
        self.tuesday3.configure(disabledforeground="#a3a3a3")
        self.tuesday3.configure(foreground="#000000")
        self.tuesday3.configure(highlightbackground="#d9d9d9")
        self.tuesday3.configure(highlightcolor="black")
        self.tuesday3.configure(pady="0")

        self.tuesday4 = tk.Button(top)
        self.tuesday4.place(x=230, y=240, height=34, width=77)
        self.tuesday4.configure(activebackground="#ececec")
        self.tuesday4.configure(activeforeground="#000000")
        self.tuesday4.configure(background="#a6ffff")
        self.tuesday4.configure(disabledforeground="#a3a3a3")
        self.tuesday4.configure(foreground="#000000")
        self.tuesday4.configure(highlightbackground="#d9d9d9")
        self.tuesday4.configure(highlightcolor="black")
        self.tuesday4.configure(pady="0")

        self.tuesday5 = tk.Button(top)
        self.tuesday5.place(x=230, y=290, height=34, width=77)
        self.tuesday5.configure(activebackground="#ececec")
        self.tuesday5.configure(activeforeground="#000000")
        self.tuesday5.configure(background="#a6ffff")
        self.tuesday5.configure(disabledforeground="#a3a3a3")
        self.tuesday5.configure(foreground="#000000")
        self.tuesday5.configure(highlightbackground="#d9d9d9")
        self.tuesday5.configure(highlightcolor="black")
        self.tuesday5.configure(pady="0")

        self.wednesday2 = tk.Button(top)
        self.wednesday2.place(x=120, y=140, height=34, width=77)
        self.wednesday2.configure(activebackground="#ececec")
        self.wednesday2.configure(activeforeground="#000000")
        self.wednesday2.configure(background="#a6ffff")
        self.wednesday2.configure(disabledforeground="#a3a3a3")
        self.wednesday2.configure(foreground="#000000")
        self.wednesday2.configure(highlightbackground="#d9d9d9")
        self.wednesday2.configure(highlightcolor="black")
        self.wednesday2.configure(pady="0")

        self.wednesday3 = tk.Button(top)
        self.wednesday3.place(x=120, y=190, height=34, width=77)
        self.wednesday3.configure(activebackground="#ececec")
        self.wednesday3.configure(activeforeground="#000000")
        self.wednesday3.configure(background="#a6ffff")
        self.wednesday3.configure(disabledforeground="#a3a3a3")
        self.wednesday3.configure(foreground="#000000")
        self.wednesday3.configure(highlightbackground="#d9d9d9")
        self.wednesday3.configure(highlightcolor="black")
        self.wednesday3.configure(pady="0")

        self.wednesday4 = tk.Button(top)
        self.wednesday4.place(x=120, y=240, height=34, width=77)
        self.wednesday4.configure(activebackground="#ececec")
        self.wednesday4.configure(activeforeground="#000000")
        self.wednesday4.configure(background="#a6ffff")
        self.wednesday4.configure(disabledforeground="#a3a3a3")
        self.wednesday4.configure(foreground="#000000")
        self.wednesday4.configure(highlightbackground="#d9d9d9")
        self.wednesday4.configure(highlightcolor="black")
        self.wednesday4.configure(pady="0")

        self.wednesday5 = tk.Button(top)
        self.wednesday5.place(x=120, y=290, height=34, width=77)
        self.wednesday5.configure(activebackground="#ececec")
        self.wednesday5.configure(activeforeground="#000000")
        self.wednesday5.configure(background="#a6ffff")
        self.wednesday5.configure(disabledforeground="#a3a3a3")
        self.wednesday5.configure(foreground="#000000")
        self.wednesday5.configure(highlightbackground="#d9d9d9")
        self.wednesday5.configure(highlightcolor="black")
        self.wednesday5.configure(pady="0")

        self.thursday2 = tk.Button(top)
        self.thursday2.place(x=20, y=140, height=34, width=77)
        self.thursday2.configure(activebackground="#ececec")
        self.thursday2.configure(activeforeground="#000000")
        self.thursday2.configure(background="#a6ffff")
        self.thursday2.configure(disabledforeground="#a3a3a3")
        self.thursday2.configure(foreground="#000000")
        self.thursday2.configure(highlightbackground="#d9d9d9")
        self.thursday2.configure(highlightcolor="black")
        self.thursday2.configure(pady="0")

        self.thursday3 = tk.Button(top)
        self.thursday3.place(x=20, y=190, height=34, width=77)
        self.thursday3.configure(activebackground="#ececec")
        self.thursday3.configure(activeforeground="#000000")
        self.thursday3.configure(background="#a6ffff")
        self.thursday3.configure(disabledforeground="#a3a3a3")
        self.thursday3.configure(foreground="#000000")
        self.thursday3.configure(highlightbackground="#d9d9d9")
        self.thursday3.configure(highlightcolor="black")
        self.thursday3.configure(pady="0")

        self.thursday4 = tk.Button(top)
        self.thursday4.place(x=20, y=240, height=34, width=77)
        self.thursday4.configure(activebackground="#ececec")
        self.thursday4.configure(activeforeground="#000000")
        self.thursday4.configure(background="#a6ffff")
        self.thursday4.configure(disabledforeground="#a3a3a3")
        self.thursday4.configure(foreground="#000000")
        self.thursday4.configure(highlightbackground="#d9d9d9")
        self.thursday4.configure(highlightcolor="black")
        self.thursday4.configure(pady="0")

        self.thursday5 = tk.Button(top)
        self.thursday5.place(x=20, y=290, height=34, width=77)
        self.thursday5.configure(activebackground="#ececec")
        self.thursday5.configure(activeforeground="#000000")
        self.thursday5.configure(background="#a6ffff")
        self.thursday5.configure(disabledforeground="#a3a3a3")
        self.thursday5.configure(foreground="#000000")
        self.thursday5.configure(highlightbackground="#d9d9d9")
        self.thursday5.configure(highlightcolor="black")
        self.thursday5.configure(pady="0")

        self.sunday1.configure(text=self.Lesson('sunday2',0))
        self.sunday2.configure(text=self.Lesson('sunday2',1))
        self.sunday3.configure(text=self.Lesson('sunday2',2))
        self.sunday4.configure(text=self.Lesson('sunday2',4))
        self.sunday5.configure(text=self.Lesson('sunday2',4))

        self.monday1.configure(text=self.Lesson('monday2',0))
        self.monday2.configure(text=self.Lesson('monday2',1))
        self.monday3.configure(text=self.Lesson('monday2',2))
        self.monday4.configure(text=self.Lesson('monday2',3))
        self.monday5.configure(text=self.Lesson('monday2',4))

        self.tuesday1.configure(text=self.Lesson('tuesday2',0))
        self.tuesday2.configure(text=self.Lesson('tuesday2',1))
        self.tuesday3.configure(text=self.Lesson('tuesday2',2))
        self.tuesday4.configure(text=self.Lesson('tuesday2',3))
        self.tuesday5.configure(text=self.Lesson('tuesday2',4))

        self.wednesday1.configure(text=self.Lesson('wednesday2',0))
        self.wednesday2.configure(text=self.Lesson('wednesday2',1))
        self.wednesday3.configure(text=self.Lesson('wednesday2',2))
        self.wednesday4.configure(text=self.Lesson('wednesday2',3))
        self.wednesday5.configure(text=self.Lesson('wednesday2',4))

        self.thursday1.configure(text=self.Lesson('thursday2',0))
        self.thursday2.configure(text=self.Lesson('thursday2',1))
        self.thursday3.configure(text=self.Lesson('thursday2',2))
        self.thursday4.configure(text=self.Lesson('thursday2',3))
        self.thursday5.configure(text=self.Lesson('thursday2',4))



        self.day1 = tk.Message(top)
        self.day1.place(x=460, y=60, height=25, width=50)
        self.day1.configure(background="#d9ffff")
        self.day1.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.day1.configure(foreground="#000000")
        self.day1.configure(highlightbackground="#d9d9d9")
        self.day1.configure(highlightcolor="black")
        self.day1.configure(text='''ראשון''')
        self.day1.configure(width=60)

        self.day2 = tk.Message(top)
        self.day2.place(x=350, y=60, height=25, width=35)
        self.day2.configure(background="#d9ffff")
        self.day2.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.day2.configure(foreground="#000000")
        self.day2.configure(highlightbackground="#d9d9d9")
        self.day2.configure(highlightcolor="black")
        self.day2.configure(text='''שני''')
        self.day2.configure(width=60)

        self.day3 = tk.Message(top)
        self.day3.place(x=240, y=60, height=25, width=52)
        self.day3.configure(background="#d9ffff")
        self.day3.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.day3.configure(foreground="#000000")
        self.day3.configure(highlightbackground="#d9d9d9")
        self.day3.configure(highlightcolor="black")
        self.day3.configure(text='''שלישי''')
        self.day3.configure(width=60)

        self.day4 = tk.Message(top)
        self.day4.place(x=130, y=60, height=25, width=46)
        self.day4.configure(background="#d9ffff")
        self.day4.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.day4.configure(foreground="#000000")
        self.day4.configure(highlightbackground="#d9d9d9")
        self.day4.configure(highlightcolor="black")
        self.day4.configure(text='''רביעי''')
        self.day4.configure(width=60)

        self.day5 = tk.Message(top)
        self.day5.place(x=30, y=60, height=25, width=51)
        self.day5.configure(background="#d9ffff")
        self.day5.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.day5.configure(foreground="#000000")
        self.day5.configure(highlightbackground="#d9d9d9")
        self.day5.configure(highlightcolor="black")
        self.day5.configure(text='''חמישי''')
        self.day5.configure(width=60)

    @staticmethod
    def popup1(event, *args, **kwargs):
        Popupmenu1 = tk.Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#ececec")
        Popupmenu1.configure(activeborderwidth="1")
        Popupmenu1.configure(activeforeground="#000000")
        Popupmenu1.configure(background="#d9d9d9")
        Popupmenu1.configure(borderwidth="1")
        Popupmenu1.configure(disabledforeground="#a3a3a3")
        Popupmenu1.configure(foreground="#000000")
        Popupmenu1.post(event.x_root, event.y_root)

if __name__ == '__main__':
    vp_start_gui()





