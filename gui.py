import tkinter

windows = tkinter.Tk()
windows.title("My window")
windows.minsize(width=500, height=300)

# label
myLabel = tkinter.Label(text="My first label", font=("Courier New", 15, "bold"))
myLabel.grid(column=0, row=0)
myLabel.config(text="New Text")


def change_label():
    myLabel.config(text=userInput.get())


# entry

userInput = tkinter.Entry()
userInput.grid(column=3, row=2)

# button
myButton = tkinter.Button(text="click here", command=change_label)
myButton.grid(column=1, row=1)

def enter_anything():
    print("Tkinter is really good")

newButton = tkinter.Button(text="New Button", command=enter_anything)
newButton.grid(column=2, row=0)

windows.mainloop()
