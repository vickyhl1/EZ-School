#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0
#  in conjunction with Tcl version 8.6
#    Dec 27, 2020 06:43:17 PM +0200  platform: Windows NT
#    Dec 31, 2020 11:27:31 AM +0200  platform: Windows NT

import sys
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

import GamesStudent_support
import webbrowser
import Studentmainmenu
from data import game_links_db_init
my_links_collec = game_links_db_init()
import webbrowser

import Studentmainmenu
import webbrowser

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)

    root =tk.Tk()
    top = Games(root)
    top = Toplevel1(root)
    GamesStudent_support.init(root, top)
    root.mainloop()

w = None
def create_Games(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Games(root, *args, **kwargs)' .'''
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Games (w)
    GamesStudent_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Games():
    top = Toplevel1 (w)
    GamesStudent_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Games:
    def open_Math(self):
        webbrowser.open("http://games.yo-yoo.co.il/games_play.php?game=6497")
    def open_English(self):
        webbrowser.open("http://games.yo-yoo.co.il/games_play.php?game=4444")
    def open_Memory(self):
        webbrowser.open("http://games.yo-yoo.co.il/games_play.php?game=5692")
    def open_Geography(self):
        webbrowser.open("http://games.yo-yoo.co.il/games_play.php?game=6459")
    def open_Art(self):
        webbrowser.open("https://www.yo-yoo.co.il/coloring/")

    def Back(self):
        root.destroy()
        Studentmainmenu.vp_start_gui()

class Toplevel1:
    def newLink(self):
        f=open("newGameLink.txt")
        txt = f.read()
        f.close()
        if txt:
            webbrowser.open(txt)
    def BackToMainMenu(self):
        root.destroy()
        Studentmainmenu.vp_start_gui()
    def OpenMath(self):
        webbrowser.open("http://games.yo-yoo.co.il/games_play.php?game=5419")
    def OpenMemory(self):
        webbrowser.open("http://games.yo-yoo.co.il/games_play.php?game=6431")
    def OpenEnglish(self):
        webbrowser.open("http://www.yo-yoo.co.il/ktantanim/games_play.php?game=252")
    def OpenArt(self):
        webbrowser.open("https://www.yo-yoo.co.il/coloring/")

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

        top.geometry("600x450+381+108")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("משחקים")
        top.configure(background="#ffd5ea")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg='#ff8080',fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Memory = tk.Button(top)
        self.Memory.place(relx=0.4, rely=0.422, height=34, width=77)
        self.Memory.configure(activebackground="#ececec")
        self.Memory.configure(activeforeground="#000000")
        self.Memory.configure(background="#f5bcf4")
        self.Memory.configure(disabledforeground="#a3a3a3")
        self.Memory.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Memory.configure(foreground="#000000")
        self.Memory.configure(highlightbackground="#d9d9d9")
        self.Memory.configure(cursor="hand2")
        self.Memory.configure(highlightcolor="black")
        self.Memory.configure(pady="0")
        self.Memory.configure(text='''זיכרון''')
        self.Memory.configure(command=self.OpenMemory)
        self.Memory.configure(text='''משחק זיכרון''')
        self.Memory.configure(command=self.open_Memory)

        self.Math = tk.Button(top)
        self.Math.place(relx=0.383, rely=0.333, height=44, width=107)
        self.Math.configure(activebackground="#ececec")
        self.Math.configure(activeforeground="#000000")
        self.Math.configure(background="#ff8080")
        self.Math.configure(cursor="hand2")
        self.Math.configure(disabledforeground="#a3a3a3")

        top.geometry("600x450+383+106")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("דף משחקים")
        top.configure(background="#ff8080")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg='#ff8080',fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.383, rely=0.044, height=41, width=94)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#ff8080")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''משחקים''')

        self.Math = tk.Button(top)
        self.Math.place(relx=0.4, rely=0.2, height=34, width=77)
        self.Math.configure(activebackground="#ececec")
        self.Math.configure(activeforeground="#000000")
        self.Math.configure(background="#efc1f0")
        self.Math.configure(disabledforeground="#a3a3a3")
        self.Math.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Math.configure(foreground="#000000")
        self.Math.configure(cursor="hand2")
        self.Math.configure(highlightbackground="#d9d9d9")
        self.Math.configure(highlightcolor="black")
        self.Math.configure(pady="0")
        self.Math.configure(text='''משחק חשבון''')

        self.Math.configure(command=self.open_Math)

        self.English = tk.Button(top)
        self.English.place(relx=0.383, rely=0.467, height=44, width=107)
        self.English.configure(activebackground="#ececec")
        self.English.configure(activeforeground="#000000")
        self.English.configure(background="#ff8080")
        self.English.configure(cursor="hand2")
        self.English.configure(disabledforeground="#a3a3a3")
        self.Math.configure(text='''חשבון''')
        self.Math.configure(command=self.OpenMath)

        self.English = tk.Button(top)
        self.English.place(relx=0.4, rely=0.311, height=34, width=77)
        self.English.configure(activebackground="#ececec")
        self.English.configure(activeforeground="#000000")
        self.English.configure(background="#e9c9df")
        self.English.configure(disabledforeground="#a3a3a3")
        self.English.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.English.configure(foreground="#000000")
        self.English.configure(cursor="hand2")
        self.English.configure(highlightbackground="#d9d9d9")
        self.English.configure(highlightcolor="black")
        self.English.configure(pady="0")

        self.English.configure(text='''משחק לימוד אנגלית''')
        self.English.configure(command=self.open_English)

        self.Geography = tk.Button(top)
        self.Geography.place(relx=0.383, rely=0.6, height=44, width=107)
        self.Geography.configure(activebackground="#ececec")
        self.Geography.configure(activeforeground="#000000")
        self.Geography.configure(background="#ff8080")
        self.Geography.configure(cursor="hand2")
        self.Geography.configure(disabledforeground="#a3a3a3")
        self.Geography.configure(foreground="#000000")
        self.Geography.configure(highlightbackground="#d9d9d9")
        self.Geography.configure(highlightcolor="black")
        self.Geography.configure(pady="0")
        self.Geography.configure(text='''משחק גיאוגרפיה''')
        self.Geography.configure(command=self.open_Geography)

        self.Art = tk.Button(top)
        self.Art.place(relx=0.383, rely=0.733, height=44, width=107)
        self.Art.configure(activebackground="#ececec")
        self.Art.configure(activeforeground="#000000")
        self.Art.configure(background="#ff8080")
        self.Art.configure(cursor="hand2")
        self.Art.configure(disabledforeground="#a3a3a3")
        self.English.configure(text='''אנגלית''')
        self.English.configure(command=self.OpenEnglish)

        self.Art = tk.Button(top)
        self.Art.place(relx=0.4, rely=0.533, height=34, width=77)
        self.Art.configure(activebackground="#ececec")
        self.Art.configure(activeforeground="#000000")
        self.Art.configure(background="#e6ccdd")
        self.Art.configure(disabledforeground="#a3a3a3")
        self.Art.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Art.configure(foreground="#000000")
        self.Art.configure(cursor="hand2")
        self.Art.configure(highlightbackground="#d9d9d9")
        self.Art.configure(highlightcolor="black")
        self.Art.configure(pady="0")

        self.Art.configure(text='''משחקי אומנות''')
        self.Art.configure(command=self.open_Art)

        self.BackToMenu = tk.Button(top)
        self.BackToMenu.place(relx=0.017, rely=0.889, height=44, width=137)
        self.BackToMenu.configure(activebackground="#ececec")
        self.BackToMenu.configure(activeforeground="#000000")
        self.BackToMenu.configure(background="#ff8080")
        self.BackToMenu.configure(cursor="hand2")
        self.BackToMenu.configure(disabledforeground="#a3a3a3")
        self.Art.configure(text='''אומנות''')
        self.Art.configure(command=self.OpenArt)

        self.AnotherGame = tk.Button(top)
        self.AnotherGame.place(relx=0.4, rely=0.644, height=34, width=77)
        self.AnotherGame.configure(activebackground="#ececec")
        self.AnotherGame.configure(activeforeground="#000000")
        self.AnotherGame.configure(background="#e4cddf")
        self.AnotherGame.configure(disabledforeground="#a3a3a3")
        self.AnotherGame.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.AnotherGame.configure(foreground="#000000")
        self.AnotherGame.configure(cursor="hand2")
        self.AnotherGame.configure(highlightbackground="#d9d9d9")
        self.AnotherGame.configure(highlightcolor="black")
        self.AnotherGame.configure(pady="0")
        self.AnotherGame.configure(text='''מחשק נוסף''')
        self.AnotherGame.configure(command=self.newLink)

        self.BackToMenu = tk.Button(top)
        self.BackToMenu.place(relx=0.033, rely=0.889, height=34, width=127)
        self.BackToMenu.configure(activebackground="#ececec")
        self.BackToMenu.configure(activeforeground="#000000")
        self.BackToMenu.configure(background="#e8cae7")
        self.BackToMenu.configure(disabledforeground="#a3a3a3")
        self.BackToMenu.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.BackToMenu.configure(foreground="#000000")
        self.BackToMenu.configure(cursor="hand2")
        self.BackToMenu.configure(highlightbackground="#d9d9d9")
        self.BackToMenu.configure(highlightcolor="black")
        self.BackToMenu.configure(pady="0")
        self.BackToMenu.configure(text='''חזרה לתפריט הראשי''')
        self.BackToMenu.configure(command=self.BackToMainMenu)

        self.BackToMenu.configure(command=self.Back)
        self.BackToMenu.configure(command=self.BackToMainMenu)

if __name__ == '__main__':
    vp_start_gui()




