from tkinter import *
from datetime import datetime
import time

root=None

def timer_a():
    start=datetime.now()
    input("Please press the Enter button")

    end=datetime.now()

    difference=end-start
    print(difference.total_seconds())


def pause(delay):
    start = datetime.now()
    
    while True:
      diff = (datetime.now() - start)
      diff = diff.total_seconds()*1000 #convert to milliseconds
      if (diff > delay):
        break


def timer_b():
    userInput=int(input("Please input a time in SECOND : "))
       
    while(userInput>0):
        pause(1000)
        userInput-=1
        print(userInput)

def timer_c():
    userInput_global=int(input("Please input a time in SECOND : "))
       
    while(userInput_global>0):
        time.sleep(1)
        userInput_global-=1
        print(userInput_global)

def timer_c2(userInput):    
    while(userInput>0):
        time.sleep(1)
        userInput-=1
        print(userInput)

def timer_task3(root,label, userInput):  
    if userInput >= 0:  
        print(userInput)   
        label.config(text=str(userInput)) 
        root.after(1000, timer_task3,root, label, userInput - 1)  # Schedule the next call after 1 second  
    else:  
        label.config(text="0")  





def main():
    #timer_a()
    #timer_b()
    #timer_c()

  
    userInputM=int(input("Please input a time in SECOND : "))
    
    root = Tk()
    root.title("Counter")
    root.geometry("300x300")
    label = Label(root, text=str(userInputM), font=('comic sans', 50), pady="100")
    label.pack()

    timer_task3(root,label, userInputM)
    
    root.mainloop()

    #timer_c2(userInputM)

    
    



main()
