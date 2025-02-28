import google.generativeai as genai
from tkinter import *
from tkinter.ttk import Progressbar,LabelFrame,Combobox
from tkinter import messagebox
from datetime import datetime
import time


class ChatBot():
        def __init__(self):
           self.root = Tk()
           self.root.title("North America Fruit Price Query AI ChatBot")
           self.root.geometry("800x450")

           self.userNameLabel=Label(self.root,text="User Name : ",font=("Arial",15))
           self.userNameLabel.grid(row=0,column=0,padx=(150,0),pady=(150,0),sticky=E)
           self.userNameEntry = Entry(self.root, font=("Arial", 15))
           self.userNameEntry.grid(row=0, column=1,pady=(150,0),sticky=W)

           self.passWordLabel=Label(self.root,text="Passwords : ",font=("Arial",15))
           self.passWordLabel.grid(row=1,column=0,padx=(150,0),sticky=E)
           self.passWordEntry = Entry(self.root, font=("Arial", 15))
           self.passWordEntry.grid(row=1, column=1, padx=(0,100), pady=0,sticky=W)

           self.loginButton=Button(self.root,text="Login",font=("Arial",20),width=6,height=3,command=self.loginButton)
           self.loginButton.grid(row=1,column=2,pady=(0,100))

           self.checkButtonVar=IntVar()
           self.checkButton=Checkbutton(self.root,text="Visitor Mode(No password required)",variable=self.checkButtonVar)
           self.checkButton.grid(row=2,column=1,sticky=W)

           self.progressBar=Progressbar(self.root,orient="horizontal", length=300, mode="determinate")

           self.labelFrame=LabelFrame(self.root,text="Welcome to use the North America Fruit Price Query AI Chatbot")
           self.label1=Label(self.labelFrame,text="Countries include : Canada,United States,Mexico")
           self.label2=Label(self.labelFrame,text="Fruits include : Apple,Banana,Orange...")
           self.label3=Label(self.labelFrame,text="The Query could be classified by Month and Year")
           self.label4=Label(self.labelFrame,text="This effect is achieved by Label Frame")
           
           self.startToUseButton=Button(self.root,text="Start To Use",font=("Arial",10),width=20,height=3,command=self.startToUse)

           self.foreGroundColorLabel=Label(self.root,text="Foreground Colour : ",font=("Arial",15))
           self.foreGroundColorComboBox=Combobox(self.root,values=["blue", "black", "red"])
           self.foreGroundColorComboBox.set("black")
           self.foreGroundColorComboBox.bind("<<ComboboxSelected>>",self.changeForeGroundColor)

           # Create a menu bar
           self.menuBar=Menu(self.root)

           # Create the File menu
           self.fileMenu=Menu(self.menuBar,tearoff=0)
           self.fileMenu.add_command(label="Canvas Drafting", command=self.topLevelNewWindow)

           # Add the File menu to the menu bar
           self.menuBar.add_cascade(label="File",menu=self.fileMenu)

           # Configure the menu bar
           self.root.config(menu=self.menuBar) 


           self.root.protocol("WM_DELETE_WINDOW",self.on_window_close_request)

           self.queryResultTextWidget=Text(self.root,width=100,height=10,bg="lightyellow")


           self.countryVar=StringVar(value="Canada")
           self.radioCanada=Radiobutton(self.root, text="Canada", variable=self.countryVar, value="Canada")
           self.radioAmerica=Radiobutton(self.root, text="America", variable=self.countryVar, value="America")
           self.radioMexico=Radiobutton(self.root, text="Mexico", variable=self.countryVar, value="Mexico")
        
           self.fruitList=["Apple","Banana","Orange","Grapes","Strawberry","Watermelon","Pineapple","Mango","Blueberry","Peach"]
           self.fruitSelection=StringVar()
           self.fruitListBox=Listbox(self.root,width=10, height=5,listvariable=self.fruitSelection)
           self.fruitSelection.set(tuple(self.fruitList))
           
           self.spinBox_MonthValue=IntVar(value=1)
           self.spinBox=Spinbox(self.root,from_=1, to=12, textvariable=self.spinBox_MonthValue)

           self.scale_YearValue=IntVar(value=2000)
           self.scale=Scale(self.root,from_=2000, to=2025,orient=VERTICAL,variable=self.scale_YearValue)

           
           self.queryButtonFrame=Frame(self.root,width=8,height=5,bg="#e0e0e0")
           self.queryButtonFrame.pack_propagate(False)  # Disable auto-resizing based on content
           self.queryButton=Button(self.queryButtonFrame,text="QUERY",font=("Arial",20),width=6,height=3,bg="#4CAF50",fg="white",command=self.priceQuery)
           
           self.root.mainloop()


        def loginButton(self,event=None):
            if(not self.checkButtonVar.get()):
                if(  (self.userNameEntry.get()=="abc") and   (self.passWordEntry.get()=="123")      ):
                    self.userNameLabel.grid_forget()
                    self.userNameEntry.grid_forget()
                    self.passWordLabel.grid_forget()
                    self.passWordEntry.grid_forget()
                    self.loginButton.grid_forget()
                    self.checkButton.grid_forget()

                    self.progressBar.grid(row=3,column=3,padx=(180,0),pady=(350,0))
                    self.start_progress()
                    self.progressBar.grid_forget()

                    self.labelFrame.pack(expand='yes', fill='both',padx=(100,0),pady=(50,0))
                    self.label1.place(x=0,y=5)
                    self.label2.place(x=0,y=35)
                    self.label3.place(x=0,y=65)
                    self.label4.place(x=0,y=95)

                    self.startToUseButton.pack()
                else:
                    messagebox.showwarning("Warning","Wrong user name or password !!! ")
            else:
                 self.userNameLabel.grid_forget()
                 self.userNameEntry.grid_forget()
                 self.passWordLabel.grid_forget()
                 self.passWordEntry.grid_forget()
                 self.loginButton.grid_forget()
                 self.checkButton.grid_forget()

                 self.progressBar.grid(row=3,column=3,padx=(180,0),pady=(350,0))
                 self.start_progress()
                 self.progressBar.grid_forget()

                 self.labelFrame.pack(expand='yes', fill='both',padx=(100,0),pady=(50,0))
                 self.label1.place(x=0,y=5)
                 self.label2.place(x=0,y=35)
                 self.label3.place(x=0,y=65)
                 self.label4.place(x=0,y=95)

                 self.startToUseButton.pack()
                

    

        def start_progress(self):
              self.progressBar.start()

              # Simulate a task that takes time to complete
              for i in range(101):
                 # Simulate some work
                 time.sleep(0.05)  
                 self.progressBar['value'] = i
                 # Update the GUI
                 self.root.update_idletasks()  
              self.progressBar.stop()

        def startToUse(self):
            self.labelFrame.pack_forget()
            self.startToUseButton.pack_forget()

            self.foreGroundColorLabel.grid(row=0,column=0,padx=(0,0),sticky=W)
            self.foreGroundColorComboBox.grid(row=0,column=0,padx=(200,0),sticky=W)
            
            self.queryResultTextWidget.grid(row=1,pady=(10,0))

            self.radioCanada.grid(padx=(20,0),pady=(20,0),sticky=W)
            self.radioAmerica.grid(padx=(20,0),sticky=W)
            self.radioMexico.grid(padx=(20,0),sticky=W)

            self.fruitListBox.grid(row=3,padx=(0,10))

            self.spinBox.grid(row=3,padx=(230,0))

            self.scale.grid(row=3,padx=(430,0))

            self.queryButtonFrame.grid(pady=(0,0))
            self.queryButton.grid()

            


        def changeForeGroundColor(self,event=None):
                selected_item =self.foreGroundColorComboBox.get()
                self.foreGroundColorLabel.config(fg=selected_item)
                self.radioCanada.config(fg=selected_item)
                self.radioAmerica.config(fg=selected_item)
                self.radioMexico.config(fg=selected_item)
                self.fruitListBox.config(fg=selected_item)
                self.spinBox.config(fg=selected_item)
                self.scale.config(fg=selected_item)
                self.queryButton.config(fg=selected_item)
                self.queryResultTextWidget.config(fg=selected_item)

        def topLevelNewWindow(self,event=None):
                newWindow=Toplevel()
                newWindow.title("Canvas Drafting Board ( By Toplevel Window ) ")
                newWindow.geometry("450x480")

                # define function when mouse double click is enabled
                def paint( event ):
	
	                # Co-ordinates.
	                x1, y1, x2, y2 = ( event.x - 3 ),( event.y - 3 ), ( event.x + 3 ),( event.y + 3 ) 
	
	                # Colour
	                Colour = "#000fff000"
	
	                # specify type of display
	                canvasWidget.create_line( x1, y1, x2, y2, fill = Colour )

                

                # create canvas widget.
                canvasWidget=Canvas(newWindow,width=430,height=450)

                # call function when double click is enabled.
                canvasWidget.bind( "<B1-Motion>", paint )

                # create label.
                label = Label(newWindow, text = "Double Click and Drag to draw." )

                canvasWidget.pack()
                label.pack()

        def on_window_close_request(self,event=None):
                self.newWindow2=Toplevel(self.root)
                self.newWindow2.title("Closing Window ( By Message Widget )")
                self.newWindow2.geometry("400x150")

                displayMessage="Are you sure to close ? "
                messageVar = Message(self.newWindow2, text=displayMessage)
                messageVar.config(bg='lightgreen')
                messageVar.pack()

                yesButton=Button(self.newWindow2,text="Yes",command=self.rootWindowDestroy)
                yesButton.pack(side=LEFT,padx=(130,0))

                noButton=Button(self.newWindow2,text="No",command=self.subWindowDestroy)
                noButton.pack(side=RIGHT,padx=(0,130))


        def rootWindowDestroy(self,event=None):
                self.root.destroy()

        def subWindowDestroy(self,event=None):
                self.newWindow2.destroy()

        def listBoxSelectedItem(self):
                selected_index=self.fruitListBox.curselection()

                if selected_index:  # Check if an item is selected
                        return self.fruitListBox.get(selected_index)


        def priceQuery(self):
                question="Please make up the price of "+str(self.listBoxSelectedItem())+" on month of "+str(self.spinBox_MonthValue.get())+" in year of "+str(self.scale_YearValue.get())+" for the country of "+str(self.countryVar.get())+" ? I want a short,straightforward,precise and concise answer ."
                print(question)
                print()
                genai.configure(api_key="AIzaSyCYL38cpk6GHFo8dvmgYZOog_1W3Tmc1Sg")
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(question)

                self.queryResultTextWidget.delete(1.0, END)  # Deletes all content
                self.queryResultTextWidget.insert(END, str(response.text))
                



                



def main():
    C1=ChatBot()




main()
