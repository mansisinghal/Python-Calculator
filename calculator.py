#from Tkinter import *
#for python-3 it should be written as tkinter and for other version it should be camel case
#import everything from tkinter module
from tkinter import *
# create a GUI window 
root=Tk()
# set the title of GUI window
root.title('mycalci')
# create the text entry box for 
# showing the expression 
e=Entry(root,font="Arial 25 bold ",width=16,bd=5,bg='light grey',justify='right')
# grid method is used for placing 
# the widgets at respective positions 
# in table like structure .
e.grid(row=0,column=0,columnspan=4)
def add(x):
e.insert(16,x)
def result():
 r=eval(e.get())
 e.delete(0,END)
 e.insert(16,r)
 # create a Buttons and place at a particular 
 # location inside the root window . 
 # when user press the button, the command or 
 # function affiliated to that button is executed . 
Button(root,text='7',command=lambda:add(7),width=5,height=2).grid(row=1,column=0,sticky=N+S+E+W)
Button(root,text='8',command=lambda:add(8),width=5,height=2).grid(row=1,column=1,sticky=N+S+E+W)
Button(root,text='9',command=lambda:add(9),width=5,height=2).grid(row=1,column=2,sticky=N+S+E+W)
Button(root,text='+',command=lambda:add('+'),width=5,height=2).grid(row=1,column=3,sticky=N+S+E+W)
Button(root,text='4',command=lambda:add(4),width=5,height=2).grid(row=2,column=0,sticky=N+S+E+W)
Button(root,text='5',command=lambda:add(5),width=5,height=2).grid(row=2,column=1,sticky=N+S+E+W)
Button(root,text='6',command=lambda:add(6),width=5,height=2).grid(row=2,column=2,sticky=N+S+E+W)
Button(root,text='-',command=lambda:add('-'),width=5,height=2).grid(row=2,column=3,sticky=N+S+E+W)
Button(root,text='1',command=lambda:add(1),width=5,height=2).grid(row=3,column=0,sticky=N+S+E+W)
Button(root,text='2',command=lambda:add(2),width=5,height=2).grid(row=3,column=1,sticky=N+S+E+W)
Button(root,text='3',command=lambda:add(3),width=5,height=2).grid(row=3,column=2,sticky=N+S+E+W)
Button(root,text='*',command=lambda:add('*'),width=5,height=2).grid(row=3,column=3,sticky=N+S+E+W)
Button(root,text='0',command=lambda:add(0),width=5,height=2).grid(row=4,column=0,sticky=N+S+E+W)
Button(root,text='/',command=lambda:add('/'),width=5,height=2).grid(row=4,column=1,sticky=N+S+E+W)
Button(root,text='=',command=result,width=5,height=2).grid(row=4,column=2,sticky=N+S+E+W)
Button(root,text='c',width=5,height=2).grid(row=4,column=3,sticky=N+S+E+W)

root.mainloop()
