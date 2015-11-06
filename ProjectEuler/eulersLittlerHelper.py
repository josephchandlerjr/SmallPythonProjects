#!/usr/bin/env python3
"""
quick and dirty gui interface to view/solve my project euler solutions
"""

import os, subprocess, glob
import queue, threading
from tkinter import *
from lib.timer import best_time
from tkinter.messagebox import askokcancel

class Quitter(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Quit', command=self.quit)
        widget.pack(side=LEFT, expand=YES, fill=BOTH)

    def quit(self):
        ans = askokcancel('Verify exit', "Really quit?")
        if ans: Frame.quit(self)

class Helper(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.threadq = queue.Queue(maxsize=0)
        self.threadwatcher()
        self.title("Euler's little helper")
        Label(self, text='Solved Problems').pack()
        self.buildinter()
        
    def buildinter(self):
        rowSize = 5 
        self.var = StringVar()
        problems = self.find_euler_files()
        while problems:
            items, problems = problems[:rowSize], problems[rowSize:]
            row = Frame(self)
            row.pack(anchor=W)
            for p in items:
                Radiobutton(row,text=p[0], 
                                value=p[1], 
                                variable=self.var, 
                                width=5).pack(side=LEFT)
        self.var.set('p1.py')
        Button(self, text='View', command=lambda: self.view(self.var.get())).pack(side=LEFT)
        Button(self, text='Solve', command=lambda: self.solve(self.var.get())).pack(side=LEFT)
        Button(self, text='Edit/View', command= lambda: self.edit(self.var.get())).pack(side=LEFT)
        Quitter(self).pack(side=RIGHT)

    def find_euler_files(self):
        problems_found = glob.glob('p[0-9]*py')
        problems = []
        for p in problems_found:
            try:
                prob = int(p[1:p.find('.')])
                problems.append((prob, p)) # (number,file) 
            except ValueError:
                pass
        return sorted(problems)
              
    def solve(self, module):
        if askokcancel('About to solve', 'This will reveal the answer. Are you sure?'):
            top = Toplevel()
            self.lbl = Label(top, text='Solving. \n This may take a few seconds so hang in there.')
            self.lbl.pack()
            top.update()
            module = module[:module.find('.')]
            mod = __import__(module)
            thread = threading.Thread(target=self.solveinthread, args = (self.lbl, mod.solve))
            thread.start()

    def edit(self, module):
        editor = os.environ.get('EDITOR','vim')
        subprocess.call([editor, module])

    def view(self, module):
        module = module[:module.find('.')]
        mod = __import__(module)
        top = Toplevel()
        Label(top, text=mod.__doc__).pack()

    def threadwatcher(self):
        try:
            func = self.threadq.get(block=False)
        except queue.Empty:
            pass 
        else:
            func()

        self.after(1000, lambda: self.threadwatcher())

    def displayanswer(self, widget, answer):
        widget.config(text='Solving. \n This may take a few seconds so hang in there.\n'+answer)

    def solveinthread(self, widget, func):
        answer = best_time(func)
        print(answer)
        self.threadq.put(lambda:self.displayanswer(widget, answer))

if __name__ == '__main__':
    Helper().mainloop() 

