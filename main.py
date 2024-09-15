from tkinter import *
window=Tk()
window.title("Tkinter window")
window.geometry("500x500")
# label
greeting=Label(bg="yellow",fg="pink",text="hello user")
greeting.pack()
# button
button=Button(text="click me",bg="blue",fg="black")
button.pack()
# entry
entry=Entry(width=40,fg="blue",bg="red")
entry.pack()
# frame
frame=Frame(master=window,relief=RAISED,borderwidth=10)
frame.pack()
label=Label(master=frame,text="helo")
label.pack()
textbox=Text(fg="green",bg="yellow")
textbox.pack()
window.mainloop()