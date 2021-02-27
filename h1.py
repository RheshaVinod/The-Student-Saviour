from tkinter import*
from stopwatch import *
def todolist():
    
    inp_list=[]
    n=int(input("Enter number of tasks to do today:"))
    print("Enter your to do's")
    for i in range(0,n):
        i= input()
        inp_list.append(i)
    print("End of list")
    def records():
        f=open("record.txt",'r')
        s=f.readlines()
        for line in s:
            line=line.strip()
            line=line.split()
        x=zip(inp_list,line)
        t=tuple(x)
        f.close()
        print("Time taken for each task:")
        for m in t:
            for o in m:
                print(o,end='   ')
            print()
    def records1():
        f1=open("record1.txt",'a')
        f1.write(t)
        f1.close()
    def records2():
        f2=open("record2.txt",'a')
        f1.write(t)
        f2.close()

        

    root=Tk()
    label2=Label(root,text="TO DO LIST",bg='black',fg='white')
    label2.pack()
    label3=Label(root,text="Select Day number")
    label2.pack()
    ch1=Checkbutton(root,text='1',command = records1)
    ch2=Checkbutton(root,text='2',command = records2)
    for j in inp_list:
        bu1=Checkbutton(root,text=j,command = stopwatch)
        bu1.pack()
    t=pass_s
    print(t)
    lb=Button(root,text="Previous records",bg='purple',fg='white',command=record)
    lb.pack()
    root.mainloop()
todolist()
