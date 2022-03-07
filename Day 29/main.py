from tkinter import messagebox
import tkinter
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    entry_password.delete(0, tkinter.END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    if len(entry_website.get()) == 0 or len(entry_password.get()) == 0:
        messagebox.showinfo(title="Oops, something went wrong...", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=entry_website.get(),
                                       message=f"These are the details entered: \nE-mail: {entry_user.get()}"
                                               f"\nPassword: {entry_password.get()}\nIs it ok to save?")

        if is_ok:
            with open("./data.txt", "a") as data:
                data.write(f"{entry_website.get()} | {entry_user.get()} | {entry_password.get()}\n")

            entry_website.delete(0, tkinter.END)
            entry_password.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, width=300, height=300)

logo = tkinter.PhotoImage(file="logo.png")

canvas = tkinter.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

button_gen_pass = tkinter.Button(text="Generate Password", command=generate_password)
button_gen_pass.grid(row=3, column=2)

button_add = tkinter.Button(text="Add", command=add, width=42)
button_add.grid(row=4, column=1, columnspan=2)

label_website = tkinter.Label(text="Website:")
label_website.grid(row=1, column=0)
label_user = tkinter.Label(text="E-mail/Username:")
label_user.grid(row=2, column=0)
label_password = tkinter.Label(text="Password:")
label_password.grid(row=3, column=0)

entry_website = tkinter.Entry(width=50)
entry_website.grid(row=1, column=1, columnspan=2)
entry_website.focus()
entry_user = tkinter.Entry(width=50)
entry_user.grid(row=2, column=1, columnspan=2)
entry_user.insert(0, "kesleyraimundo@gmail.com")
entry_password = tkinter.Entry(width=32)
entry_password.grid(row=3, column=1)

window.mainloop()
