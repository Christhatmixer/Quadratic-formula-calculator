import math

try:
    from tkinter import *
except ImportError:
    from Tkinter import *
from math import *


def quadratic(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    discRoot = math.sqrt((b * b) - 4 * a * c)
    answer = (-b + discRoot) / (2 * a) # solving positive
    answer2 = (-b - discRoot) / (2 * a) # solving negative
    return (answer,answer2)




root =   Tk()
root.title("Quadratic Calculator")
Header = Label(root,text="Input the corresponding variables")
Header.grid(row=0,column=2)
root.resizable(width=False,height=False)

#Variables
answer=StringVar(root)
answer2=StringVar(root)
A_variable = StringVar(root)
B_variable = StringVar(root)
C_variable = StringVar(root)


#-------------variable entry ------------------

#labels
A_label = Label(root,text="A")
B_label = Label(root,text="B")
C_label = Label(root,text="C")
A_label.grid(row=1,column=1)
B_label.grid(row=2,column=1)
C_label.grid(row=3,column=1)



#entry boxes
A = Entry(root,textvariable=A_variable)
B = Entry(root,textvariable=B_variable)
C = Entry(root,textvariable=C_variable)
A.grid(row=1,column=2)
B.grid(row=2,column=2)
C.grid(row=3,column=2)


#-----------Answer Box--------------

#answer box
Answer_box = Label(root, textvariable=answer)
Answer_box.grid(row=4,column=2)
answer_box2 = Label(root, textvariable=answer2)
answer_box2.grid(row=5,column=2)


#----------Calculate Button-----------
def show_answer():
    answer.set(0)
    answer2.set(0)
    try:
        final_answer = quadratic(A_variable.get(),B_variable.get(),C_variable.get())
        answer.set(final_answer[0])
        answer2.set(final_answer[1])
        return final_answer
    except:
        answer.set("Negative Squareroot")
        answer2.set("negative Squareroot")
        return final_answer


Calculate = Button(root,text="Calculate",command=show_answer)
Calculate.grid(row=6,column=2)

root.update()

root.mainloop()
