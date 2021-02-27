from tkinter import*
from to_do_list_final.py import*
from music_playlist.py import *
from website_blocker.py import *

root=Tk()
lb=Label(root,text="The Student Saviour")
lb.grid(row=0,column=0)
lb2=Label(root,text="Choose")
lb2.grid(row=1,column=0)
bt1=Button(root,text="Website Blocker",command=webBlock)
bt2=Button(root,text="To-Do-List",command=todolist)
bt3=Button(root,text="Study Music",command=music_playlist)
bt1.grid()
bt2.grid()
bt3.grid()
root.mainloop()





