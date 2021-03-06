def stopwatch():
    import tkinter as Tkinter 
    from datetime import datetime   
    counter = 66600
    running = False
    string=''
    def counter_label(label): 
            def count(): 
                    if running: 
                            nonlocal counter
                            nonlocal string
	
			# To manage the intial delay. 
                            if counter==66600:			 
                                    display="Starting..."
                            else: 
                                    tt = datetime.fromtimestamp(counter) 
                                    string = tt.strftime("%H:%M:%S") 
                                    display=string
                                    
                                
	
                            label['text']=display # Or label.config(text=display) 
	
			 
                            label.after(1000, count) 
                            counter += 1
	 
            count()	 
    
# start function of the stopwatch 
    def Start(label): 
            nonlocal running 
            running=True
            counter_label(label) 
            start['state']='disabled'
            stop['state']='normal'
            reset['state']='normal'
	
# Stop function of the stopwatch 
    def Stop(): 
            nonlocal running 
            start['state']='normal'
            stop['state']='disabled'
            reset['state']='normal'
            running = False
            z=string+' '           
            f=open("record.txt",mode='a')
            f.write(z)        
            f.close()
	
# Reset function of the stopwatch 
    def Reset(label): 
            nonlocal counter 
            counter=66600
	
	# If rest is pressed after pressing stop. 
            if running==False:	 
                    reset['state']='disabled'
                    label['text']='Welcome!'
	
	# If reset is pressed while the stopwatch is running. 
            else:				 
                    label['text']='Starting...'
	
    master = Tkinter.Tk() 
    master.title("Stopwatch") 
	
# Fixing the window size. 
    master.minsize(width=250, height=70) 
    label = Tkinter.Label(master, text="Welcome!", fg="black", font="Verdana 30 bold") 
    label.pack() 
    f = Tkinter.Frame(master) 
    start = Tkinter.Button(f, text='Start', width=6, command=lambda:Start(label)) 
    stop = Tkinter.Button(f, text='Stop',width=6,state='disabled', command=Stop) 
    reset = Tkinter.Button(f, text='Reset',width=6, state='disabled', command=lambda:Reset(label)) 
    f.pack(anchor = 'center',pady=5) 
    start.pack(side="left") 
    stop.pack(side ="left") 
    reset.pack(side="left") 
    master.mainloop() 
