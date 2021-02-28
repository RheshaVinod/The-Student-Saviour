from tkinter import*
import to_do_list_final as td
import music_playlist as mp
import website_blocker as wb
import graph as g

root=Tk()
lb=Label(root,text="The Student Saviour")
lb.grid(row=0,column=0)
lb2=Label(root,text="Choose")
lb2.grid(row=1,column=0)
bt1=Button(root,text="Website Blocker",command=wb.webBlock)
bt2=Button(root,text="To-Do-List",command=td.todolist)
bt3=Button(root,text="Study Music",command=mp.music_playlist)
bt4=Button(root,text="Statistical analysis",command=g.graph)
bt1.grid()
bt2.grid()
bt3.grid()
bt4.grid()
root.mainloop()











