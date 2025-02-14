from tkinter import *
from datetime import datetime
from tkinter import messagebox
import time

class Counter1():

    def __init__(self):
        self._root = Tk()
        self._root.title("Counter")
        self._root.geometry("800x250")

        self._counter = 0
        
        self.displayLabel='0'

        self._label = Label(self._root, text=self.displayLabel, font=("Arial",35,"bold"))
        self._label.pack(pady=(50,20))

        self.promptLabel=Label(self._root,text='Press "+" to increment time.Press "go" to start timer',font=("Arial",9))
        self.promptLabel.pack(pady=(50,0))

        self._button = Button(self._root, text="+", font=("Arial", 24),width=8, height=1)
        self._button.pack(side=LEFT, padx=15)
        #self._button = Button(self._root, text="+", font=("Arial", 24), command=self.increment)
        self._button.bind("<Button-1>", self.increment)
        self._button.pack(pady=5)

        self.go_button=Button(self._root,text="go",font=("Arial",24),width=8, height=1)
        self.go_button.pack(side=RIGHT,padx=15,pady=5)

        self.go_button.bind("<Button-1>",self.go)
        self.go_button.pack()

        self._root.mainloop()



    def increment(self,event=None):
        self._counter += 1
        self.displayLabel=str(self._counter)
        self._label.config(text=self.displayLabel)

    def go(self,event=None):
        if self._counter>=0:
            self.displayLabel=str(self._counter)
            self._label.config(text=self.displayLabel)
            self._counter -= 1
            self._label.after(1000, self.go)
        




class Counter2():

    def __init__(self):
        self._root = Tk()
        self._root.title("Counter")
        self._root.geometry("400x350")

        self._counter = 0
        self.userInput=0
        self.running = False 
        self.stopWatchTime=0
        self.stopWatchRunning=False
        
        self.displayLabel='0'

        self.topLabel = Label(self._root, text=self.displayLabel, font=("Arial",50,"bold"))  
        self.topLabel.pack(pady=(50,20))

        self.stopWatchLabel=Label(self._root,text="00:00:00", font=("Helvetica", 48))
        self.stopWatchLabel.pack()

        self.instructionLabel=Label(self._root,text="Enter a time : ",font=("Arial",15))   
        self.instructionLabel.pack(side=LEFT,padx=55,pady=(30,25))

        self.entry=Entry(self._root,width=10,font=("Arial",15))
        self.entry.pack(side=LEFT,pady=(30,25))

        self._root.bind("<Return>",self.getEntry)

        self.stopWatchButton=Button(self._root,text="Stop Watch",font=("Arial",24),width=8, height=1,command=self.start_stop)
        self.stopWatchButton.pack()
       
        self.update_clock()

        self.stopButton=Button(self._root,text="Stop",font=("Arial",24),width=8, height=1)
        self.stopButton.pack_forget()

        self.stopButton.bind("<Button-1>",self.exitProgram)
        self.stopButton.pack_forget()

        self.moreButton=Button(self._root,text="More",font=("Arial",24),width=8, height=1)
        self.moreButton.pack_forget()

        self.moreButton.bind("<Button-1>",self.moreButtonFunction)
        self.moreButton.pack_forget()

        self.resetButton=Button(self._root,text="Reset",font=("Arial",24),width=8, height=1)
        self.resetButton.pack_forget()

        self.resetButton.bind("<Button-1>",self.reset)
        self.resetButton.pack_forget()

        self.pauseButton=Button(self._root,text="Pause",font=("Arial",24),width=8, height=1)
        self.pauseButton.pack_forget()

        self.pauseButton.bind("<Button-1>",self.pause)
        self.pauseButton.pack_forget()


        self._root.mainloop()


    def getEntry(self,event=None):
        if(  (self.entry.get()).isdigit()  and int(self.entry.get())>=0  ):           
            self.userInput=int(self.entry.get())
            self.entry.delete(0,END)
            self.running=True
            self.start()
        else:
            messagebox.showwarning("Warning","Please enter a valid number")
            self.entry.delete(0,END)

    def reset(self,event=None): 
        self.running=False
        self.userInput=0
        self.topLabel.config(text='0')
        self.stopWatchLabel.config(text="00:00:00")

    def pause(self,event=None):
        if(self.running):
            self.running=False
        else:
            self.running=True
            self.start()
      



    def start(self,event=None):     
        if(  self.userInput >= 0 and self.running  ):
                self.displayLabel=str(self.userInput)
                self.topLabel.config(text=self.displayLabel)
                self.userInput -= 1
                self.topLabel.after(1000,self.start)
        self.instructionLabel.pack_forget()
        self.entry.pack_forget()
        self.stopWatchButton.pack_forget()
        
        self.stopButton.pack(side=LEFT,padx=50,pady=(30,25))
        self.moreButton.pack(side=RIGHT,padx=15,pady=(30,25))
        self.resetButton.pack(side=LEFT,padx=15,pady=(30,25))
        self.pauseButton.pack(side=RIGHT,padx=15,pady=(30,25))

    def exitProgram(self,event=None):
        self._root.destroy()

    def moreButtonFunction(self,event=None):
        self.stopButton.pack_forget()
        self.moreButton.pack_forget()
        self.resetButton.pack_forget()
        self.pauseButton.pack_forget()

        self.instructionLabel.pack(side=LEFT,padx=55,pady=(30,25))
        self.entry.pack(side=LEFT,pady=(30,25))
        self.stopWatchButton.pack(side=LEFT,padx=55,pady=(30,25))

    def start_stop(self):  
        if self.stopWatchRunning:  
            self.stopWatchRunning = False   
        else:  
            self.stopWatchRunning = True      


    def update_clock(self):
        if (self.stopWatchRunning):
             self.stopWatchTime+=1
             hours, remainder = divmod(self.stopWatchTime, 3600)
             minutes, seconds = divmod(remainder, 60)
             self.stopWatchLabel.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        self._root.after(1000, self.update_clock)




def main():
    c1=Counter1()
   #c2=Counter2()





main()
