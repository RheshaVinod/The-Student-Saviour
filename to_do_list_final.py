
from tkinter import*
from stopwatch_final import *
def todolist():
    inp_list=[]
    root=Tk()
    label2=Label(root,text="TO DO LIST",bg='black',fg='white')
    label2.pack()
    inp_list=[]
    lb1=Label(root,text="Enter the number of tasks to do today")
    lb1.pack()
    e1= Entry (root)
    e1.pack()
    
    def myClick():
       
       message = e1.get()
       for i in range(0,int(message)):
            e2=Entry(root,width=25)
            e2.pack()
            
            def myClick2():
            
                
                n = e2.get()
                
                z="start stopwatch " 
                bu1=Button(root,text=z,command = stopwatch)
                bu1.pack()
    
            bt2 = Button(root, text = "Click Me2!", command = myClick2 ,bg = "blue",fg = "white")#callback
            bt2.pack()  
    bt1 = Button(root, text = "Click Me!", command = myClick ,bg = "blue",fg = "white")#callback
    bt1.pack()
    
    
    root.mainloop()
    
todolist()

