#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0
#  in conjunction with Tcl version 8.6
#    Dec 19, 2020 01:32:41 PM +0200  platform: Windows NT

import sys
import pymongo

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

import HealthPage_support
from datetime import date
from tkinter import messagebox
import Studentmainmenu
import Teachermainmenu
import Secretarymainmenu

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    HealthPage_support.set_Tk_var()
    top = Toplevel1 (root)
    HealthPage_support.init(root, top)
    root.mainloop()
flag = 0
w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    HealthPage_support.set_Tk_var()
    top = Toplevel1 (w)
    HealthPage_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def submit(self):
        global flag
        if flag:
            tk.messagebox._show('Health page', 'ההצהרה הוגשה')
            flag=0
            f = open("Current_user.txt")
            txt = str(date.today()) + "\n" + f.read() + "\n\n"
            f.close()
            f = open("Health_statements.txt", "a")
            f.write(txt + "\n\n")
            f.close()

        else:
            tk.messagebox.showwarning('Health page', 'לא אישרת את ההצהרה, נסה שוב מאוחר יותר')
        root.destroy()
        Studentmainmenu.vp_start_gui()
    def checkbox(self):
        global flag
        if flag==1:
            flag=0
        elif flag==0:
            flag=1
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("843x567+248+117")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("Health Statement")
        top.configure(background="#d1d1d1")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.107, rely=0.123, relheight=0.57
                , relwidth=0.76)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''
        
                :טופס הצהרת בריאות                         

אני כתלמיד/ה מצהיר/ה כי ערכתי היום בדיקה למדידת חום גוף בה נמצא כי 
                            חום גופי אינו עולה על 38 מעלות

אני מצהיר/ה כי איני משתעל/ת וכן כי אין לי קשיים בנשימה    

נא הכנס/י מספר תעודת זהנת ואשר/י את ההצהרה לפני ההגשה ''')

        self.Message1.configure(width=641)

        self.style.map('TCheckbutton',background=
            [('selected', _bgcolor), ('active', _ana2color)])
        self.checkboxhealth = ttk.Checkbutton(top)
        self.checkboxhealth.place(relx=0.368, rely=0.723, relwidth=0.19
                , relheight=0.0, height=21)
        self.checkboxhealth.configure(variable=HealthPage_support.tch51)
        self.checkboxhealth.configure(takefocus="")
        self.checkboxhealth.configure(text='''מאשר\ת''')
        self.checkboxhealth.configure(compound='bottom')
        self.checkboxhealth.configure(command= self.checkbox)


        self.submithealth = tk.Button(top)
        self.submithealth.place(relx=0.38, rely=0.811, height=44, width=127)
        self.submithealth.configure(activebackground="#ececec")
        self.submithealth.configure(activeforeground="#000000")
        self.submithealth.configure(background="#d9d9d9")
        self.submithealth.configure(disabledforeground="#a3a3a3")
        self.submithealth.configure(foreground="#000000")
        self.submithealth.configure(highlightbackground="#d9d9d9")
        self.submithealth.configure(highlightcolor="black")
        self.submithealth.configure(pady="0")
        self.submithealth.configure(text='''הגשה''')
        self.submithealth.configure(command= self.submit)

        self.dateanduser = tk.Message(top)
        self.dateanduser.place(relx=0.178, rely=0.035, relheight=0.076
                , relwidth=0.641)
        self.dateanduser.configure(background="#d9d9d9")
        self.dateanduser.configure(foreground="#000000")
        self.dateanduser.configure(highlightbackground="#d9d9d9")
        self.dateanduser.configure(highlightcolor="black")
        f = open("Current_user.txt")
        txt = str(date.today()) + "\n" + f.read()
        f.close()
        self.dateanduser.configure(text= txt)
        self.dateanduser.configure(width=540)

if __name__ == '__main__':
    vp_start_gui()




