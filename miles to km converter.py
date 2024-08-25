import tkinter


def calculation():
    miles = int(tk_entry.get())
    label0.config(text=miles * 1.6093)


window = tkinter.Tk()
window.geometry('250x100')
window.title('Mile to Km Converter')
window.config(pady=20, padx=45)

label1 = tkinter.Label(text='Miles')
label1.grid(column=3, row=0)

label2 = tkinter.Label(text='is equal to')
label2.grid(column=0, row=1)

label0 = tkinter.Label(text=0)
label0.grid(column=1, row=1)

label3 = tkinter.Label(text='Km')
label3.grid(column=3, row=1)

button = tkinter.Button(text='Calculate', command=calculation)
button.grid(column=1, row=3)

tk_entry = tkinter.Entry(window, width=10)
tk_entry.grid(column=1, row=0)
window.mainloop()
