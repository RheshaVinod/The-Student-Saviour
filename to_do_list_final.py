
from tkinter import*
from stopwatch_final import *
def todolist():
    inp_list=[]
    #n=int(input("Enter number of tasks to do today:"))
    #print("Enter your to do's")
    root=Tk()
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
    
            #lb4 = Label(root, text = n)
            #lb4.pack()
            #inp_list.append(n)
            bt2 = Button(root, text = "Click Me2!", command = myClick2 ,bg = "blue",fg = "white")#callback
            bt2.pack()  
       print("End of list")
    bt1 = Button(root, text = "Click Me!", command = myClick ,bg = "blue",fg = "white")#callback
    bt1.pack()
     
    
##    def records():
##        f=open("record.txt",'r')
##        s=f.readlines()
##        for line in s:
##            line=line.strip()
##            line=line.split()
##        x=zip(inp_list,line)
##        t=tuple(x)
##        print("Time taken for each task:")
##        for m in t:
##            for o in m:
##                print(o,end='   ')
##            print()   
##        

    label2=Label(root,text="TO DO LIST",bg='black',fg='white')
    label2.pack()
    #lb=Button(root,text="Previous records",bg='purple',fg='white',command=records)
    #lb.pack()
    
    root.mainloop()
todolist()
