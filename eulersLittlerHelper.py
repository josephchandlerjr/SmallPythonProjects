
import os, subprocess, glob
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


def solve(module):
    module = module[:module.find('.')]
    mod = __import__(module)
    #top = Toplevel()
    #Label(top, text='Solving, this may take a few seconds\n').pack()
    answer =mod.solve()
    print(answer)
    

def edit(module):
    editor = os.environ.get('EDITOR','vim')
    subprocess.call([editor, module])

def view(module):
    module = module[:module.find('.')]
    mod = __import__(module)
    top = Toplevel()
    Label(top, text=mod.__doc__).pack()


if __name__ == '__main__':
    root = Tk()
    root.title("Euler's little helper")
    Label(root,text='Solved Problems').pack()
    problems_found = glob.glob('p[0-9]*py')
    problems = []
    for p in problems_found:
        try:
            prob = int(p[1:p.find('.')])
            problems.append((prob, p)) # (number,file) 
        except ValueError:
            pass
    problems = sorted(problems)
    rowSize = 5 
    var = StringVar()
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
