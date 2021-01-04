#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0
#  in conjunction with Tcl version 8.6
#    Jan 03, 2021 05:01:41 PM +0200  platform: Windows NT

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

import AbsenceReport5_support
sys.path.append('..')
from data import user_db_init
user_db_init()


client = pymongo.MongoClient()
mydb = client['EZSchooldb']


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    AbsenceReport5_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    AbsenceReport5_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#e0cce3'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("994x696+152+0")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("דוח חיסורים כיתה ה")
        top.configure(background="#e0cce3")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.392, rely=0.043, height=48, width=189)
        self.Label1.configure(background="#e0cce3")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''דוח חיסורים''')

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.091, rely=0.144, relheight=0.823, relwidth=0.818)
        self.Message1.configure(anchor='nw')
        self.Message1.configure(background="#ffffff")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='teeeeeeext')
        self.Message1.configure(width=810)

if __name__ == '__main__':
    vp_start_gui()





