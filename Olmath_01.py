from tkinter import *
from tkinter import ttk
import webbrowser

root = Tk()
root.title("Olmath_01")
root.resizable(False, False)
root.geometry("900x500")

header_frame = Frame(root, bg="#9b4ad9")
header_frame.pack(side="top", fill="x", padx=25, pady=10)

lbl = Label(header_frame, text="  Ресурсы олимпиад           ", font=("Arial", 15), bg="#9b4ad9", fg="#ffffff")
lbl.pack(side="left", padx=10)

lbl1 = Label(header_frame, text="    Ресурсы для подготовки       ", font=("Arial", 15), bg="#9b4ad9", fg="#ffffff")
lbl1.pack(side="left", padx=10)

header_frame1 = Frame(root)
header_frame1.pack(side="top", fill="x", anchor="n")

def open_webite_1():
    webbrowser.open("https://sesc.nsu.ru/olymp-vsesib/")
button1 = ttk.Button(header_frame1, text="Всесибирская открытая олимпиада школьников    ", command=open_webite_1)
button1.pack(side="left", anchor="nw", ipady=15, padx=30)

def open_web():
    webbrowser.open("https://os.mipt.ru/")
btn = ttk.Button(header_frame1,text = "     Физтех-регионам  ", command=open_web)
btn.pack(side="left", anchor="n", ipady=15, ipadx=10, padx=20)

header_frame2 = Frame(root)
header_frame2.pack(side="left", anchor="nw", pady=25)

def open_website():
    webbrowser.open("https://olymp-online.mipt.ru/")
button = ttk.Button(header_frame2, text=" Физтех ", command=open_website)
button.pack(side="left", anchor="nw", ipady=15, padx=30)

def open_web1():
    webbrowser.open("https://edu.sirius.online/#/")
btn1 = ttk.Button(header_frame2, text = " Сириус курсы ", command=open_web1)
btn1.pack(side="top", anchor="nw", ipady=15, ipadx=10, padx=234)

root.mainloop()