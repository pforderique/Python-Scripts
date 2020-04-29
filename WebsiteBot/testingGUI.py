from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import *
from time import sleep
import pandas as pd

def firstExample():
    #creates our window
    window=Tk()

    #titles it and shapes it
    window.title('Mercury Main Window')
    window.geometry('450x200')

    #let's give our window a label#
    titleLabel = Label(window, text="Project Mercury", font=("Calibri", 20)) #create object
    titleLabel.grid(column=1, row=0) #set it's position

    lbl = Label(window,text = "Not signed in.")
    lbl.grid(column=0,row=2)

    #TEXTBOX User Input:
    txt = Entry(window,width=10)
    txt.grid(column=1,row=2)
    txt.focus() #this puts the cursor in this textbox immediately as you start the program!  
    # state='disabled' to disable button

    #add a button - Dont forget to add functionality! dont add ()
    def signInClicked():
        result = "Signing you in " + txt.get() + "!" #gets what the user typed in !
        lbl.configure(text=result) #changes label name

    btn = Button(window, text="Sign In", command = signInClicked) 
    btn.grid(column=1, row=1) 

    # #SCROLLED TEXT 
    scroll = scrolledtext.ScrolledText(window,width=10,height=8)
    scroll.grid(column=2,row=0)
    scroll.insert(INSERT,'Your text goes here')
    #txt.delete(1.0,END) to delete contents

    #MESSAGE BOX
    # messagebox.showinfo('Message title','Message content') #or showwarning, showerror
    # messagebox.askretrycancel("you sure?") #askquestion, askyesno, etc.

    #spinbox - go down or up a number
    spin = Spinbox(window, from_=0, to=100, width=5)
    # spin = Spinbox(window, values=(3, 8, 11), width=5)
    spin.grid(column=0,row=4)

    #Progress bar:
    bar = Progressbar(window, length=200)
    bar.grid(column=1,row=4)
    bar['value'] = 30

    #ask for file loc 
    #file = filedialog.askopenfilename()
    #dir = filedialog.askdirectory()
    #messagebox.showinfo("Directory Chosen:",dir)

    #menu (file down)
    menu = Menu(window)
    new_item = Menu(menu)
    new_item.add_command(label='New')
    menu.add_cascade(label='File', menu=new_item)
    window.config(menu=menu)

    window.mainloop() #needs to be called at end

def secondExample():
    window = Tk()
    window.title("Project Mercury")
    window.geometry('350x200')

    #making a combo box
    combo = Combobox(window)
    combo['values']= [1, 2, 3, 4, 5, "Text"]
    combo.current(1) #set the selected item
    combo.grid(column=0, row=0)
    
    #label
    lbl = Label(text=combo.get()) #combo.get() to get value
    lbl.grid(column=1,row=0)

    #Check Button
    chk_state = BooleanVar() #or chk_state = IntVar() to set to 0 or 1
    chk_state.set(False) #set check state
    chk = Checkbutton(window, text='Choose', var=chk_state)
    chk.grid(column=2, row=0)

    window.mainloop()

# firstExample()
import matplotlib.pyplot as plt
df = pd.read_csv("C:/Users/fabri/OneDrive/Documents/DasText/csvFiles/myPortofilo.csv")
df['Last Price'] = df['Last Price'].map(lambda x: x.replace(",",""))
df["Last Price"] = pd.to_numeric(df["Last Price"], downcast="float")
df.plot(kind='bar',x='Ticker',y='Last Price')

print("plotted.")