import tkinter as tk
window=tk.Tk()

for i in range(3):
    for j in range(3):
        frame=tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i,column=j,padx=5,pady=5)
        tempText="row"+str(i)+"column"+str(j)
        label=tk.Label(master=frame,text=tempText)
        label.pack()
window.mainloop()
