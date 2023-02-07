from tkinter import *

window = Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="This is a label", font=("Arial", 24, "bold"))
my_label.pack()

def button_clicked():
    my_label["text"]= "Button got clicked!"
    # or 
    my_label.config(text="Button got clicke!")
    
button = Button(text="Click here", command=button_clicked)
button.pack()

window.mainloop()