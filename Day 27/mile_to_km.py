import tkinter

def converter():
    result.config(text=f"{round(float(entry.get()) / 0.621371, 3)}")


window = tkinter.Tk()
window.minsize(height=200, width=200)
window.title("Mile to Km Converter")
window.config(padx=50, pady=50)

entry = tkinter.Entry(width=10)

calculate = tkinter.Button(text="Calculate", command=converter)

miles = tkinter.Label(text="Miles")
is_equal_to = tkinter.Label(text="is equal to")
result = tkinter.Label(text="0")
km = tkinter.Label(text="Km")

entry.grid(row=0, column=1)
miles.grid(row=0, column=2)
is_equal_to.grid(row=1, column=0)
result.grid(row=1, column=1)
km.grid(row=1, column=2)
calculate.grid(row=2, column=1)

window.mainloop()
