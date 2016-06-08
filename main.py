from tkinter import *
from math import *


def quadratic(a,b,c):
    answer = (-float(b))-(sqrt((float(b)**2)-(4*float(a)*float(c))/(2*float(a))))
    return answer



root =   Tk()
root.title("Quadratic Calculator")
Header = Label(root,text="Input the corresponding variables")
Header.grid(row=0,column=2)
root.resizable(width=False,height=False)

#Variables
answer=StringVar(root)
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


#----------Calculate Button-----------
def show_answer():
    answer.set(0)
    try:
        final_answer = quadratic(A_variable.get(),B_variable.get(),C_variable.get())
        answer.set(final_answer)
    except:
        answer.set("Negative Squareroot")
    return final_answer

Calculate = Button(root,text="Calculate",command=show_answer)
Calculate.grid(row=5,column=2)

root.update()

root.mainloop()
