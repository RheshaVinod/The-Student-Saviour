from tkinter import *
import webbrowser
root=Tk()
lb1=Label(root,text='Music Playlist')
lb1.grid(row=0,column=0)
lb2=Label(root,text="Do you want to view the spotify playlist?")
lb2.grid(row=1,column=0)
def onclick():
    webbrowser.open('https://open.spotify.com/playlist/471N195f5jAVs086lzYglw?si=4RT6cvK_RkGt7TvxnZ_u-g&utm_source=copy-link')
def no():
    pass
bt1=Button(root,text="YES",command=onclick)
bt2=Button(root,text="NO",command=no)
bt1.grid()
bt2.grid()
root.mainloop()
    
