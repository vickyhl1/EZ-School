#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0
#  in conjunction with Tcl version 8.6
#    Jan 05, 2021 12:30:45 PM +0200  platform: Windows NT

import sys
import pymongo
sys.path.append('..')
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

import SubjectSelectPage_support
import Teachermainmenu
import Studentmainmenu
from data import getUser,setSubject
import MathPageTeacher
import HistoryPageTeacher
import HebrewPageTeacher
import TanachPageTeacher
import MathPageStud
import HistoryPageStud
import HebrewPageStud
import TanachPageStud
import GradeReportStud
import GradeReportTeacher




def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = SubjectSelectPage (root)
    SubjectSelectPage_support.init(root, top)
    root.mainloop()

w = None
def create_SubjectSelectPage(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_SubjectSelectPage(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = SubjectSelectPage (w)
    SubjectSelectPage_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_SubjectSelectPage():
    global w
    w.destroy()
    w = None

class SubjectSelectPage:
    def openReport(self):
        if self.currentUser['Usertype'] == 3:
            GradeReportStud.vp_start_gui()
        elif self.currentUser['Usertype'] == 2:
            GradeReportTeacher.vp_start_gui()

    def openMainmenue(self):
        if self.currentUser['Usertype'] == 2:
            root.destroy()
            Teachermainmenu.vp_start_gui()
        elif self.currentUser['Usertype'] == 3:
            root.destroy()
            Studentmainmenu.vp_start_gui()

    def openMathPage(self):
        setSubject('Math')
        if self.currentUser['Usertype'] == 2:
            root.destroy()
            MathPageTeacher.vp_start_gui()
        elif self.currentUser['Usertype'] == 3:
            root.destroy()
            MathPageStud.vp_start_gui()

    def openHebrewPage(self):
        setSubject('Hebrew')
        if self.currentUser['Usertype'] == 2:
            root.destroy()
            HebrewPageTeacher.vp_start_gui()
        elif self.currentUser['Usertype'] == 3:
            root.destroy()
            HebrewPageStud.vp_start_gui()

    def openHistoryPage(self):
        setSubject('History')
        if self.currentUser['Usertype'] == 2:
            root.destroy()
            HistoryPageTeacher.vp_start_gui()
        elif self.currentUser['Usertype'] == 3:
            root.destroy()
            HistoryPageStud.vp_start_gui()

    def openTanchPage(self):
        setSubject('Tanach')
        if self.currentUser['Usertype'] == 2:
            root.destroy()
            TanachPageTeacher.vp_start_gui()
        elif self.currentUser['Usertype'] == 3:
            root.destroy()
            TanachPageStud.vp_start_gui()

    def __init__(self, top=None):
        self.currentUser = getUser()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+660+210")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("???? ??????????????")
        top.configure(background="#ccfdd5")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Mainmenuebtn = tk.Button(top)
        self.Mainmenuebtn.place(relx=0.05, rely=0.844, height=54, width=127)
        self.Mainmenuebtn.configure(activebackground="#ececec")
        self.Mainmenuebtn.configure(activeforeground="#000000")
        self.Mainmenuebtn.configure(background="#ffffff")
        self.Mainmenuebtn.configure(disabledforeground="#a3a3a3")
        self.Mainmenuebtn.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Mainmenuebtn.configure(foreground="#000000")
        self.Mainmenuebtn.configure(highlightbackground="#d9d9d9")
        self.Mainmenuebtn.configure(highlightcolor="black")
        self.Mainmenuebtn.configure(pady="0")
        self.Mainmenuebtn.configure(text='''?????????? ????????''')
        self.Mainmenuebtn.configure(command=self.openMainmenue)

        self.Mathbtn = tk.Button(top)
        self.Mathbtn.place(relx=0.4, rely=0.2, height=44, width=97)
        self.Mathbtn.configure(activebackground="#ececec")
        self.Mathbtn.configure(activeforeground="#000000")
        self.Mathbtn.configure(background="#ffa275")
        self.Mathbtn.configure(disabledforeground="#a3a3a3")
        self.Mathbtn.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Mathbtn.configure(foreground="#000000")
        self.Mathbtn.configure(highlightbackground="#d9d9d9")
        self.Mathbtn.configure(highlightcolor="black")
        self.Mathbtn.configure(pady="0")
        self.Mathbtn.configure(text='''??????????''')
        self.Mathbtn.configure(command=self.openMathPage)

        self.Hebrewbtn = tk.Button(top)
        self.Hebrewbtn.place(relx=0.4, rely=0.356, height=44, width=97)
        self.Hebrewbtn.configure(activebackground="#ececec")
        self.Hebrewbtn.configure(activeforeground="#000000")
        self.Hebrewbtn.configure(background="#66b3ff")
        self.Hebrewbtn.configure(disabledforeground="#a3a3a3")
        self.Hebrewbtn.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Hebrewbtn.configure(foreground="#000000")
        self.Hebrewbtn.configure(highlightbackground="#d9d9d9")
        self.Hebrewbtn.configure(highlightcolor="black")
        self.Hebrewbtn.configure(pady="0")
        self.Hebrewbtn.configure(text='''??????????''')
        self.Hebrewbtn.configure(command=self.openHebrewPage)

        self.Historybtn = tk.Button(top)
        self.Historybtn.place(relx=0.4, rely=0.511, height=44, width=97)
        self.Historybtn.configure(activebackground="#ececec")
        self.Historybtn.configure(activeforeground="#000000")
        self.Historybtn.configure(background="#ffff6a")
        self.Historybtn.configure(disabledforeground="#a3a3a3")
        self.Historybtn.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Historybtn.configure(foreground="#000000")
        self.Historybtn.configure(highlightbackground="#d9d9d9")
        self.Historybtn.configure(highlightcolor="black")
        self.Historybtn.configure(pady="0")
        self.Historybtn.configure(text='''??????????????????''')
        self.Historybtn.configure(command=self.openHistoryPage)

        self.Tanachbtn = tk.Button(top)
        self.Tanachbtn.place(relx=0.4, rely=0.667, height=44, width=97)
        self.Tanachbtn.configure(activebackground="#ececec")
        self.Tanachbtn.configure(activeforeground="#000000")
        self.Tanachbtn.configure(background="#707070")
        self.Tanachbtn.configure(disabledforeground="#a3a3a3")
        self.Tanachbtn.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Tanachbtn.configure(foreground="#000000")
        self.Tanachbtn.configure(highlightbackground="#d9d9d9")
        self.Tanachbtn.configure(highlightcolor="black")
        self.Tanachbtn.configure(pady="0")
        self.Tanachbtn.configure(text='''????"??''')
        self.Tanachbtn.configure(command=self.openTanchPage)

        self.TitleL = tk.Label(top)
        self.TitleL.place(relx=0.267, rely=0.044, height=41, width=264)
        self.TitleL.configure(background="#ccfdd5")
        self.TitleL.configure(disabledforeground="#a3a3a3")
        self.TitleL.configure(font="-family {Segoe UI} -size 14 -weight bold -underline 1")
        self.TitleL.configure(foreground="#000000")
        self.TitleL.configure(text='''???? ?????????? ??????????''')

        self.ReportBtn = tk.Button(top)
        self.ReportBtn.place(relx=0.1, rely=0.2, height=44, width=97)
        self.ReportBtn.configure(activebackground="#ececec")
        self.ReportBtn.configure(activeforeground="#000000")
        self.ReportBtn.configure(background="#707070")
        self.ReportBtn.configure(disabledforeground="#a3a3a3")
        self.ReportBtn.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.ReportBtn.configure(foreground="#000000")
        self.ReportBtn.configure(highlightbackground="#d9d9d9")
        self.ReportBtn.configure(highlightcolor="black")
        self.ReportBtn.configure(pady="0")
        self.ReportBtn.configure(text='''????"?? ????????????''')
        self.ReportBtn.configure(command=self.openReport)

if __name__ == '__main__':
    vp_start_gui()





