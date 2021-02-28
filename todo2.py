from tkinter import*
from stopwatch_final import *

def todolist():
    root=Tk()
    inp_list=[]
    lb1=Label(root,text="Enter the number of tasks to do today")
    lb1.pack()
    e1=Entry(root,width=15)
    e1.pack()
    e1.insert(0,'3')
    def myClick():
        n=e1.get()
        for i in range(0,int(n)):
          e2=Entry(root,width=25)
          e2.insert(0,'kfj')
          def myClick2():
            for i in range(0,n):
              message = e2.get()
              lb4 = Checkbox(root, text = message)
              lb4.pack()
        bt2 = Button(root, text = "Click Me!", command = myClick2,bg = "blue",fg = "white")#callback
        bt2.pack()
        
    bt1 = Button(root, text = "Click Me!", command = myClick,bg = "blue",fg = "white")#callback
    bt1.pack()
    lb2=Label(root,text="End of list")
    lb2.pack()
    def records():
        f=open("record.txt",'r')
        s=f.readlines()
        for line in s:
            line=line.strip()
            line=line.split()
        x=zip(inp_list,line)
        t=tuple(x)
        print("Time taken for each task:")
        for m in t:
            for o in m:
                print(o,end='   ')
            print()   
        

    label2=Label(root,text="TO DO LIST",bg='black',fg='white')
    label2.pack()
    for j in inp_list:
        bu1=Checkbutton(root,text=j,command = stopwatch)
        bu1.pack()
    lb=Button(root,text="Previous records",bg='purple',fg='white',command=records)
    lb.pack()
    root.mainloop()

todolist()
