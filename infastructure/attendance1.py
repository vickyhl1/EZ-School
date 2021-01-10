#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.6
#  in conjunction with Tcl version 8.6
#    Dec 31, 2020 04:32:10 PM +0200  platform: Windows NT

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

sys.path.append('..')
from data import user_db_init
user_db_init()


client = pymongo.MongoClient()
mydb = client['EZSchooldb']
Users=mydb['Users']
import attendance1_support
import Teachermainmenu
import AbsenceReport
from tkinter import messagebox


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    attendance1_support.set_Tk_var()
    top = Toplevel1 (root)
    attendance1_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    attendance1_support.set_Tk_var()
    top = Toplevel1 (w)
    attendance1_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def report(self):
        AbsenceReport.vp_start_gui()

    def Back(self):
        root.destroy()
        Teachermainmenu.vp_start_gui()

    def add_absence(self, student_id):
        global Users
        user = Users.find_one({'id': student_id})
        Users.update_one({'id': user['id']}, {'$set': {'attendance': user['attendance'] + 1}})

    def Changebox1(self):
            self.CheckVar1=not self.CheckVar1
    def Changebox2(self):
            self.CheckVar2=not self.CheckVar2
    def Changebox3(self):
            self.CheckVar3=not self.CheckVar3
    def Changebox4(self):
            self.CheckVar4=not self.CheckVar4
    def Changebox5(self):
            self.CheckVar5=not self.CheckVar5
    def Changebox6(self):
            self.CheckVar6=not self.CheckVar6
    def Changebox7(self):
            self.CheckVar7=not self.CheckVar7
    def Changebox8(self):
            self.CheckVar8=not self.CheckVar8
    def Changebox9(self):
            self.CheckVar9=not self.CheckVar9
    def Changebox10(self):
            self.CheckVar10=not self.CheckVar10


    def Submit(self):
        if not self.CheckVar1:
            self.add_absence('123456789')
        if not self.CheckVar2:
            self.add_absence('123456788')
        if not self.CheckVar3:
            self.add_absence('987654321')
        if not self.CheckVar4:
            self.add_absence('123412341')
        if not self.CheckVar5:
            self.add_absence('123458769')
        if not self.CheckVar6:
            self.add_absence('123477688')
        if not self.CheckVar7:
            self.add_absence('121212121')
        if not self.CheckVar8:
            self.add_absence('111111111')
        if not self.CheckVar9:
            self.add_absence('320755481')
        if not self.CheckVar10:
            self.add_absence('309044071')

        tk.messagebox.showinfo('Successful', f'''דוח הוגש''')

        root.destroy()
        Teachermainmenu.vp_start_gui()

    def __init__(self, top=None):
        self.CheckVar1 = 0
        self.CheckVar2 = 0
        self.CheckVar3 = 0
        self.CheckVar4 = 0
        self.CheckVar5 = 0
        self.CheckVar6 = 0
        self.CheckVar7 = 0
        self.CheckVar8 = 0
        self.CheckVar9 = 0
        self.CheckVar10 = 0
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("1920x1051+-9+-9")
        top.minsize(148, 1)
        top.maxsize(1550, 750)
        top.resizable(1,  1)
        top.title("נוכחות כיתה א")
        top.configure(background="#fef1b4")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.submit = tk.Button(top)
        self.submit.place(relx=0.385, rely=0.879, height=93, width=456)
        self.submit.configure(activebackground="#ececec")
        self.submit.configure(activeforeground="#000000")
        self.submit.configure(background="#f5cb03")
        self.submit.configure(cursor="hand2")
        self.submit.configure(disabledforeground="#a3a3a3")
        self.submit.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.submit.configure(foreground="#000000")
        self.submit.configure(highlightbackground="#d9d9d9")
        self.submit.configure(highlightcolor="black")
        self.submit.configure(pady="0")
        self.submit.configure(text='''הגשת נוכחות''')
        self.submit.configure(command=self.Submit)

        self.stud1 = tk.Checkbutton(top)
        self.stud1.place(relx=0.385, rely=0.13, relheight=0.061, relwidth=0.181)
        self.stud1.configure(activebackground="#ececec")
        self.stud1.configure(activeforeground="#000000")
        self.stud1.configure(background="#fef1b4")
        self.stud1.configure(disabledforeground="#a3a3a3")
        self.stud1.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.stud1.configure(foreground="#000000")
        self.stud1.configure(highlightbackground="#d9d9d9")
        self.stud1.configure(highlightcolor="black")
        self.stud1.configure(justify='left')
        self.stud1.configure(text='''עדי כהן 123456789''')

        self.stud2 = tk.Checkbutton(top)
        self.stud2.place(relx=0.406, rely=0.18, relheight=0.061, relwidth=0.164)
        self.stud2.configure(activebackground="#ececec")
        self.stud2.configure(activeforeground="#000000")
        self.stud2.configure(background="#fef1b4")
        self.stud2.configure(disabledforeground="#a3a3a3")
        self.stud2.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.stud2.configure(foreground="#000000")
        self.stud2.configure(highlightbackground="#d9d9d9")
        self.stud2.configure(highlightcolor="black")
        self.stud2.configure(justify='left')
        self.stud2.configure(text='''רפול עזריאייב 123456788''')

        self.stud3 = tk.Checkbutton(top)
        self.stud3.place(relx=0.385, rely=0.24, relheight=0.061, relwidth=0.186)
        self.stud3.configure(activebackground="#ececec")
        self.stud3.configure(activeforeground="#000000")
        self.stud3.configure(background="#fef1b4")
        self.stud3.configure(disabledforeground="#a3a3a3")
        self.stud3.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.stud3.configure(foreground="#000000")
        self.stud3.configure(highlightbackground="#d9d9d9")
        self.stud3.configure(highlightcolor="black")
        self.stud3.configure(justify='left')
        self.stud3.configure(text='''אתי בלון 987654321''')

        self.stud4 = tk.Checkbutton(top)
        self.stud4.place(relx=0.385, rely=0.3, relheight=0.061, relwidth=0.186)
        self.stud4.configure(activebackground="#ececec")
        self.stud4.configure(activeforeground="#000000")
        self.stud4.configure(background="#fef1b4")
        self.stud4.configure(disabledforeground="#a3a3a3")
        self.stud4.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.stud4.configure(foreground="#000000")
        self.stud4.configure(highlightbackground="#d9d9d9")
        self.stud4.configure(highlightcolor="black")
        self.stud4.configure(justify='left')
        self.stud4.configure(text='''יובל קטן 123412341''')

        self.stud5 = tk.Checkbutton(top)
        self.stud5.place(relx=0.38, rely=0.36, relheight=0.051, relwidth=0.192)
        self.stud5.configure(activebackground="#ececec")
        self.stud5.configure(activeforeground="#000000")
        self.stud5.configure(background="#fef1b4")
        self.stud5.configure(disabledforeground="#a3a3a3")
        self.stud5.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.stud5.configure(foreground="#000000")
        self.stud5.configure(highlightbackground="#d9d9d9")
        self.stud5.configure(highlightcolor="black")
        self.stud5.configure(justify='left')
        self.stud5.configure(text='''עדי כהן 123458769''')

        self.stud6 = tk.Checkbutton(top)
        self.stud6.place(relx=0.391, rely=0.41, relheight=0.061, relwidth=0.181)
        self.stud6.configure(activebackground="#ececec")
        self.stud6.configure(activeforeground="#000000")
        self.stud6.configure(background="#fef1b4")
        self.stud6.configure(disabledforeground="#a3a3a3")
        self.stud6.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.stud6.configure(foreground="#000000")
        self.stud6.configure(highlightbackground="#d9d9d9")
        self.stud6.configure(highlightcolor="black")
        self.stud6.configure(justify='left')
        self.stud6.configure(text='''רפי קולדקי 123477688''')

        self.stud7 = tk.Checkbutton(top)
        self.stud7.place(relx=0.396, rely=0.47, relheight=0.052, relwidth=0.175)
        self.stud7.configure(activebackground="#ececec")
        self.stud7.configure(activeforeground="#000000")
        self.stud7.configure(background="#fef1b4")
        self.stud7.configure(disabledforeground="#a3a3a3")
        self.stud7.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.stud7.configure(foreground="#000000")
        self.stud7.configure(highlightbackground="#d9d9d9")
        self.stud7.configure(highlightcolor="black")
        self.stud7.configure(justify='left')
        self.stud7.configure(text='''שקד בולטק 121212121''')

        self.stud8 = tk.Checkbutton(top)
        self.stud8.place(relx=0.385, rely=0.519, relheight=0.062, relwidth=0.185)
        self.stud8.configure(activebackground="#ececec")
        self.stud8.configure(activeforeground="#000000")
        self.stud8.configure(background="#fef1b4")
        self.stud8.configure(disabledforeground="#a3a3a3")
        self.stud8.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.stud8.configure(foreground="#000000")
        self.stud8.configure(highlightbackground="#d9d9d9")
        self.stud8.configure(highlightcolor="black")
        self.stud8.configure(justify='left')
        self.stud8.configure(text='''זיאד חמד 111111111''')

        self.stud9 = tk.Checkbutton(top)
        self.stud9.place(relx=0.401, rely=0.589, relheight=0.051, relwidth=0.17)
        self.stud9.configure(activebackground="#ececec")
        self.stud9.configure(activeforeground="#000000")
        self.stud9.configure(background="#fef1b4")
        self.stud9.configure(disabledforeground="#a3a3a3")
        self.stud9.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.stud9.configure(foreground="#000000")
        self.stud9.configure(highlightbackground="#d9d9d9")
        self.stud9.configure(highlightcolor="black")
        self.stud9.configure(justify='left')
        self.stud9.configure(text='''ויקי חליוסטוב 320755481''')

        self.stud10 = tk.Checkbutton(top)
        self.stud10.place(relx=0.406, rely=0.659, relheight=0.05, relwidth=0.166)
        self.stud10.configure(activebackground="#ececec")
        self.stud10.configure(activeforeground="#000000")
        self.stud10.configure(background="#fef1b4")
        self.stud10.configure(disabledforeground="#a3a3a3")
        self.stud10.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.stud10.configure(foreground="#000000")
        self.stud10.configure(highlightbackground="#d9d9d9")
        self.stud10.configure(highlightcolor="black")
        self.stud10.configure(justify='left')
        self.stud10.configure(text='''רפאל עזריאייב 309044071''')

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.333, rely=0.02, relheight=0.1, relwidth=0.311)
        self.Message1.configure(background="#fef1b4")
        self.Message1.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''אנא סמנו את התלמידים הנוכחים''')
        self.Message1.configure(width=597)

        self.mainmenu = tk.Button(top)
        self.mainmenu.place(relx=0.005, rely=0.923, height=63, width=176)
        self.mainmenu.configure(activebackground="#ececec")
        self.mainmenu.configure(activeforeground="#000000")
        self.mainmenu.configure(background="#f5cb03")
        self.mainmenu.configure(cursor="hand2")
        self.mainmenu.configure(disabledforeground="#a3a3a3")
        self.mainmenu.configure(foreground="#000000")
        self.mainmenu.configure(highlightbackground="#d9d9d9")
        self.mainmenu.configure(highlightcolor="black")
        self.mainmenu.configure(pady="0")
        self.mainmenu.configure(text='''תפריט ראשי''')
        self.mainmenu.configure(command=self.Back)

        self.attendancereport = tk.Button(top)
        self.attendancereport.place(relx=0.005, rely=0.837, height=63, width=176)
        self.attendancereport.configure(activebackground="#ececec")
        self.attendancereport.configure(activeforeground="#000000")
        self.attendancereport.configure(background="#f5cb03")
        self.attendancereport.configure(cursor="hand2")
        self.attendancereport.configure(disabledforeground="#a3a3a3")
        self.attendancereport.configure(foreground="#000000")
        self.attendancereport.configure(highlightbackground="#d9d9d9")
        self.attendancereport.configure(highlightcolor="black")
        self.attendancereport.configure(pady="0")
        self.attendancereport.configure(text='''דוח נוכחות''')
        self.attendancereport.configure(command=self.report)

        self.stud1.configure(command=self.Changebox1)
        self.stud2.configure(command=self.Changebox2)
        self.stud3.configure(command=self.Changebox3)
        self.stud4.configure(command=self.Changebox4)
        self.stud5.configure(command=self.Changebox5)
        self.stud6.configure(command=self.Changebox6)
        self.stud7.configure(command=self.Changebox7)
        self.stud8.configure(command=self.Changebox8)
        self.stud9.configure(command=self.Changebox9)
        self.stud10.configure(command=self.Changebox10)

if __name__ == '__main__':
    vp_start_gui()





