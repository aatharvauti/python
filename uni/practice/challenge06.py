import tkinter as tk

window = tk.Tk()
window.geometry('600x300')
greeting = tk.Label(
    master = window,
    text = "Login",
    width = 100,
    height = 2,
    font = ('Helvetica Neue', 25)
)
greeting.pack(pady = 50)

username = tk.Label(
    master = window,
    text = "Username",
    width = 20,
    height = 2,
    font = ('Helvetica Neue', 15)
)
username.pack()

username_entry = tk.Entry(
    window,
    fg="black",
    bg="white",
    width = 50
)
username_entry.pack(pady = 20)
# username_entry.insert(0, "Username")

password = tk.Label(
    master = window,
    text = "Password",
    width = 20,
    height = 2,
    font = ('Helvetica Neue', 15)
)
password.pack()

password_entry = tk.Entry(
    window,
    fg="black",
    bg="white",
    width = 50
)
password_entry.pack(pady = 20)
# password_entry.insert(0, "Password")


def cbfx():
    print("Logged in!")

button = tk.Button(
    text = "Click Me!",
    fg = "black",
    bg = "yellow",
    width = 10,
    height = 1,
    font = ('Helvetica Neue', 10),
    command = cbfx
)
button.pack(pady = 20)

window.mainloop()
print("Window is closed!")

