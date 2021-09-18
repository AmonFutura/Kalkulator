from tkinter import *
from tkinter import ttk

#funkcija addNumbers()
def calculate(*args):
    try:
        broj1 = int(a.get())
        broj2 = int(b.get())

        rezultat.set(broj1 + broj2)

    except ValueError:
        pass

    



root = Tk()
root.title("Add two numbers:")
mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))

root.columnconfigure(0,weight = 1)
root.rowconfigure(0,weight = 1)

a = StringVar()

a_entry = ttk.Entry(mainframe, width = 7, textvariable = a) 
a_entry.grid(column = 2, row = 1, sticky =(W, E))


b = StringVar()

b_entry = ttk.Entry(mainframe, width = 7, textvariable = b) 
b_entry.grid(column = 2, row = 2, sticky =(W, E))

ttk.Button(mainframe, text = "Calculate", command = calculate).grid(column = 2, row = 3, sticky = W) 

rezultat = StringVar()

ttk.Label(mainframe, textvariable = rezultat).grid(column = 2, row = 4, sticky = (W, E))

ttk.Label(mainframe, text = "A: ").grid(column = 1, row = 1, sticky = (W))
ttk.Label(mainframe, text = "B: ").grid(column = 1, row = 2, sticky = (W))
ttk.Label(mainframe, text = "A+B: ").grid(column = 1, row = 4, sticky = (W))

for child in mainframe.winfo_children():
    child.grid_configure(padx = 5, pady = 5)


a_entry.focus()

root.bind("<Return>", calculate)

root.mainloop()