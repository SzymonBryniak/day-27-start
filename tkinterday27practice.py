import tkinter


window = tkinter.Tk()
window.geometry('600x400')
window.config(padx=100, pady=100)


def button_clicked():
    print("I got clicked")


def edit_label():
    button.config(text="clicked")


def edit_from_input():
    display_text.config(text=tk_input.get())
    print(tk_input.get())


display_text = tkinter.Label(text="New Text", font="Calibri 18 bold")
display_text.grid(column=0, row=0)

button = tkinter.Button(text="Click Me", command=edit_from_input)
button.grid(column=1, row=1)

button2 = tkinter.Button(text="New Button")
button2.grid(column=3, row=0)

tk_input = tkinter.Entry(window, width=10)
tk_input.grid(column=5, row=5)


window.mainloop()
