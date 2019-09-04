#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.25.1
#  in conjunction with Tcl version 8.6
#    Sep 03, 2019 12:52:40 AM CST  platform: Windows NT

import sys
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import POTmainfunc
import os
import os.path
import time

py3 = True


def btnExitClick():
    root.quit()


def btnOpenClick():
    filenames = tk.filedialog.askopenfilename(filetypes=[("docx file", "*.docx")])
    if len(filenames) != 0:
        w.Text1.insert(0, filenames)


def btnStartClick():
    sfile = w.Text1.get()
    if len(sfile) < 0:
        tk.messagebox.showinfo('Error','Please input filename')
        return
    if not (os.path.exists(sfile)):
        tk.messagebox.showinfo('Error','File is not Exist')
        return
    spath = os.path.dirname(sfile)
    sout = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))+'.docx'
    sout = os.path.join(spath, sout)
    i = POTmainfunc.AutoDocxNumber(sfile, sout)
    if (i != 0):
        tk.messagebox.showinfo('Error','Operate file fail')
    else:
        tk.messagebox.showinfo('OK','Operate file success')


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import POT

    POT.vp_start_gui()
