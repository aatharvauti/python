import tkinter as tk

window = tk.Tk()

tk.Label(window, text="Enter your email-id: ", font = ('Helvetica Neue', 15), justify=tk.LEFT).pack(anchor='w', pady=15, padx=20)
email_en = tk.Entry(window, fg="black", bg="white", width = 50)
email_en.pack(anchor='w', padx=20)

tk.Label(window, text="Enter password: ", font = ('Helvetica Neue', 15), justify=tk.LEFT).pack(anchor='w', pady=15, padx=20)
tk.Entry(window, fg="black", bg="white", width = 50, show="*").pack(anchor='w', padx=20)

radio_btn = tk.StringVar()

def ch_branch():
    branch = radio_btn.get()
    return branch

tk.Label(window, text="Enter your branch: ", font = ('Helvetica Neue', 15), justify=tk.LEFT).pack(anchor='w', pady=10, padx=20)
tk.Radiobutton(window, text="Computer Science", font = ('Helvetica Neue', 10), variable=radio_btn, command=ch_branch, value="Computer Science").pack(pady=5,anchor=tk.W, padx=20)
tk.Radiobutton(window, text="AI Data Science", font = ('Helvetica Neue', 10), variable=radio_btn, command=ch_branch, value="AI Data Science").pack(pady=5,anchor=tk.W, padx=20)
tk.Radiobutton(window, text="Cyber Security", font = ('Helvetica Neue', 10), variable=radio_btn, command=ch_branch, value="Cyber Security").pack(pady=5,anchor=tk.W, padx=20)

checkbx_math = tk.BooleanVar()
checkbx_pyp = tk.BooleanVar()
checkbx_java = tk.BooleanVar()

def ch_subject_math():
    subject = checkbx_math.get()
    return subject

def ch_subject_python():
    subject = checkbx_pyp.get()
    return subject

def ch_subject_java():
    subject = checkbx_java.get()
    return subject

tk.Label(window, text="Enter your branch: ", font = ('Helvetica Neue', 15), justify=tk.LEFT).pack(anchor='w', pady=10, padx=20)
tk.Checkbutton(window, text="Maths", font = ('Helvetica Neue', 10), variable=checkbx_math, command=ch_subject_math).pack(pady=5,anchor=tk.W, padx=20)
tk.Checkbutton(window, text="Python", font = ('Helvetica Neue', 10), variable=checkbx_pyp, command=ch_subject_python).pack(pady=5,anchor=tk.W, padx=20)
tk.Checkbutton(window, text="Java", font = ('Helvetica Neue', 10), variable=checkbx_java, command=ch_subject_java).pack(pady=5,anchor=tk.W, padx=20)

def cbfx():
    print(f"""
    Email: {email_en.get()}
    Branch: {ch_branch()}""")
    list = []
    if ch_subject_math():
        list.append("Maths")
    if ch_subject_python():
        list.append("Python")
    if ch_subject_java():
        list.append("Java")

    s = ","

    # joins elements of list1 by '-'
    # and stores in sting s
    s = s.join(list)
    print(f"\tSubjects: {list}")

button = tk.Button(
    text = "Submit",
    fg = "black",
    bg = "yellow",
    width = 10,
    height = 1,
    font = ('Helvetica Neue', 10),
    command = cbfx
)
button.pack(pady = 20)



window.mainloop()

