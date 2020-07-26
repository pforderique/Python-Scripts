from tkinter import Tk, Button

def start():
    window = Tk()
    window.title('COVID-19 Tracker')
    window.geometry('600x370')
    # window.protocol("WM_DELETE_WINDOW", closeApp)
    def nextWindow():
        window.destroy()
        nextPage()
    btn = Button(window,text="button",command=nextWindow)
    btn.pack()
    window.mainloop()

def nextPage():
    win = Tk()
    win.title('heu')
    win.geometry('200x500')

start()