from tkinter import*
from stopwatch_final import *
def todolist():
    
    inp_list=[]
    n=int(input("Enter number of tasks to do today:"))
    print("Enter your to do's")
    for i in range(0,n):
        i= input()
        inp_list.append(i)
    print("End of list")
    def records():
        f=open("record2.txt",'r')
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
    def record1():
        f=open("record1.txt",'r')
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
        
        

    root=Tk()
    label2=Label(root,text="TO DO LIST",bg='black',fg='white')
    label2.pack()
    ch1=Checkbutton(root,text='Day1',command = record1)
    ch2=Checkbutton(root,text='Day1',command = record2)
    for j in inp_list:
        bu1=Checkbutton(root,text=j,command = stopwatch)
        bu1.pack()
    lb=Button(root,text="Previous records",bg='purple',fg='white',command=records)
    lb.pack()
    root.mainloop()
todolist()
