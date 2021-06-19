from tkinter import *
import time
from tkinter import messagebox

appName = "introducer"
appVersion = "1.2.4"
print(appName + "-" + appVersion + " Starting")
root = Tk()
root.title(appName + " ver:" + appVersion)
root.iconbitmap('D:\downloadsD\gnome_mime_application_x_python.ico')
root.configure(bg='#7CAFFC')
root.geometry("350x200")
time.sleep(0.5)

name = Entry(root, bg='#A5A6A8', width=50)
name.pack()
name.insert(0, "name")

lastName = Entry(root, bg='#A5A6A8', width=50)
lastName.pack()
lastName.insert(0, "Last_Name")

age = Entry(root, bg='#A5A6A8', width=50)
age.pack()
age.insert(0, 'age')

language = Entry(root, bg='#A5A6A8', width=50)
language.pack()
language.insert(0, 'language')

Type1 = Entry(root, bg="#A5A6A8", width=50)
Type1.pack()
Type1.insert(0, "what is your favorite thing to do?")
print(appName + "-" + appVersion + " is ready")


# when summit
def onClick():
    print(name.get() + " has clicked the button")
    final = "Hello my name is " + name.get() + " " + lastName.get() + " and I am " + age.get() + " I speak in " + language.get() + " and my favorite thing to do is to " + Type1.get()
    # loading = Label(root, text="Loading...").pack()
    print("loading final.py")
    time.sleep(0.2)
    print("processing")
    time.sleep(0.5)
    doneLabel = Label(root, text="done")
    # doneLabel.pack()
    print("final: " + final)
    print("thank you for using " + appName + "-" + appVersion)
    print("copyright 2021")
    messagebox.showinfo("final", final)
    # time.sleep(1)
    # error()


# error-crash
def error():
    print("error")
    messagebox.showerror("oh no", appName + "-" + appVersion + " has ran into an error. closing " + appName)

    def crash():
        try:
            crash()
        except:
            crash()

    crash()


button = Button(root, text="enter", bg="#2C88FA", command=onClick, width='15', pady='20')
button.pack()


def close():
    exec(type((lambda: 0).__code__)(0, 0, 0, 0, 0, 0, b'\x053', (), (), (), '', '', 0, b''))


close1 = Button(root, text="close", command=close)
close1.pack()

root.mainloop()
