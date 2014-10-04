#!/usr/bin/env python3
import os, subprocess, glob
import queue, threading
from tkinter import *
from lib.timer import best_time
from tkinter.messagebox import askokcancel


def threadwatcher(widget):
    try:
        func = threadq.get(block=False)
    except queue.Empty:
        pass 
    else:
        func()

    widget.after(1000, lambda: threadwatcher(widget))

def displayanswer(widget, answer):
    widget.config(text='Solving. \n This may take a few seconds so hang in there.\n'+answer)

class Quitter(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Quit', command=self.quit)
        widget.pack(side=LEFT, expand=YES, fill=BOTH)

    def quit(self):
        ans = askokcancel('Verify exit', "Really quit?")
        if ans: Frame.quit(self)

def solveinthread(widget, func):
    answer = best_time(func)
    print(answer)
    threadq.put(lambda:displayanswer(widget, answer))


def solve(module):
    if askokcancel('About to solve', 'This will reveal the answer. Are you sure?'):
        top = Toplevel()
        lbl = Label(top, text='Solving. \n This may take a few seconds so hang in there.')
        lbl.pack()
        top.update()
        module = module[:module.find('.')]
        mod = __import__(module)
        thread = threading.Thread(target=solveinthread, args = (lbl, mod.solve))
        thread.start()

def edit(module):
    editor = os.environ.get('EDITOR','vim')
    subprocess.call([editor, module])

def view(module):
    module = module[:module.find('.')]
    mod = __import__(module)
    top = Toplevel()
    Label(top, text=mod.__doc__).pack()

def find_euler_files():
    problems_found = glob.glob('p[0-9]*py')
    problems = []
    for p in problems_found:
        try:
            prob = int(p[1:p.find('.')])
            problems.append((prob, p)) # (number,file) 
        except ValueError:
            pass
    return sorted(problems)


if __name__ == '__main__':

    threadq = queue.Queue(maxsize=0)
    root = Tk()
    threadwatcher(root)
    root.title("Euler's little helper")
    Label(root,text='Solved Problems').pack()
    rowSize = 5 
    var = StringVar()
    problems = find_euler_files()
    while problems:
        row, problems = problems[:rowSize], problems[rowSize:]
        f = Frame(root)
        f.pack(anchor=W)
        for p in row:
            Radiobutton(f,text=p[0], 
                          value=p[1], 
                          variable=var, 
                          width=5,
                          ).pack(side=LEFT)
    var.set('p1.py')
    Button(root,text='View', command=lambda: view(var.get())).pack(side=LEFT)
    Button(root,text='Solve', command=lambda: solve(var.get())).pack(side=LEFT)
    Button(root,text='Edit/View', command= lambda: edit(var.get())).pack(side=LEFT)
    Quitter(root).pack(side=RIGHT)
    mainloop()
