from tkinter import*
from stopwatch import *
root=Tk()
inp_list=[]
n=int(input("Enter limit"))
print("Enter you to dos")
for i in range(0,n+1):
    i= input()
    inp_list.append(i)
print(inp_list)
label2=Label(root,text="TO DO LIST",bg='black',fg='white')
label2.pack()
for j in inp_list:
    bu1=Button(root,text=j,command = stopwatch)
    bu1.pack()
root.mainloop()
