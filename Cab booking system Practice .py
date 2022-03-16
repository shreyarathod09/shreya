from tkinter import*
from tkinter.font import Font
root=Tk()
root.geometry('800x600')
root.title("Booking System")
root.configure(bg="#d5eef0") 

tl=('Arial', 15, 'bold')
title_label=Label(root, text="ARYA's Cab Booking System")
title_label.configure(font=tl)
title_label.configure(bg="#d5eef0")
title_label.pack(side=TOP, pady=10)

frame1 = Frame(root, bg="#1d666c")
frame1.pack(fill=BOTH, expand=YES, padx=150, pady=50)

frame1.columnconfigure(0, weight=2)
frame1.columnconfigure(1, weight=1)
frame1.columnconfigure(2, weight=1)
frame1.columnconfigure(3, weight=2)

name=StringVar()
label1=Label(frame1, text="Customer name", bg='#1d666c', fg="white").grid(row=0, column=1, ipady=10)
Entry(frame1, textvariable=name).grid(row=0, column=2, sticky=EW, ipady=3)




root.mainloop()