#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.25.1
#  in conjunction with Tcl version 8.6
#    Sep 03, 2019 12:52:14 AM CST  platform: Windows NT

import sys

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

import pdt_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    pdt_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    pdt_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("924x193")
        top.title("Docx tools")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.011, rely=0.181, height=23, width=134)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {System} -size 12 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''docx file''')

        self.Text1 = tk.Entry(top)
        self.Text1.place(relx=0.162, rely=0.155, relheight=0.166, relwidth=0.719)

        self.Text1.configure(background="white")
        self.Text1.configure(font="-family {Microsoft YaHei UI} -size 9")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")

        self.ButtonOpen = tk.Button(top)
        self.ButtonOpen.place(relx=0.898, rely=0.181, height=28, width=49)
        self.ButtonOpen.configure(activebackground="#ececec")
        self.ButtonOpen.configure(activeforeground="#000000")
        self.ButtonOpen.configure(background="#d9d9d9")
        self.ButtonOpen.configure(disabledforeground="#a3a3a3")
        self.ButtonOpen.configure(foreground="#000000")
        self.ButtonOpen.configure(highlightbackground="#d9d9d9")
        self.ButtonOpen.configure(highlightcolor="black")
        self.ButtonOpen.configure(pady="0")
        self.ButtonOpen.configure(text='''...''')
        self.ButtonOpen.configure(command=pdt_support.btnOpenClick)

        self.ButtonStart = tk.Button(top)
        self.ButtonStart.place(relx=0.076, rely=0.57, height=58, width=169)
        self.ButtonStart.configure(activebackground="#ececec")
        self.ButtonStart.configure(activeforeground="#000000")
        self.ButtonStart.configure(background="#d9d9d9")
        self.ButtonStart.configure(disabledforeground="#a3a3a3")
        self.ButtonStart.configure(font="-family {System} -size 12 -weight bold")
        self.ButtonStart.configure(foreground="#000000")
        self.ButtonStart.configure(highlightbackground="#d9d9d9")
        self.ButtonStart.configure(highlightcolor="black")
        self.ButtonStart.configure(pady="0")
        self.ButtonStart.configure(text='''Start''')
        self.ButtonStart.configure(command=pdt_support.btnStartClick)

        self.ButtonExit = tk.Button(top)
        self.ButtonExit.place(relx=0.736, rely=0.57, height=58, width=169)
        self.ButtonExit.configure(activebackground="#ececec")
        self.ButtonExit.configure(activeforeground="#000000")
        self.ButtonExit.configure(background="#d9d9d9")
        self.ButtonExit.configure(command=pdt_support.btnExitClick)
        self.ButtonExit.configure(disabledforeground="#a3a3a3")
        self.ButtonExit.configure(font="-family {System} -size 12 -weight bold")
        self.ButtonExit.configure(foreground="#000000")
        self.ButtonExit.configure(highlightbackground="#d9d9d9")
        self.ButtonExit.configure(highlightcolor="black")
        self.ButtonExit.configure(pady="0")
        self.ButtonExit.configure(text='''Exit''')

if __name__ == '__main__':
    vp_start_gui()





