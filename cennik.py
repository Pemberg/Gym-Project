from cProfile import label
from msilib.schema import ListBox
from tkinter import ANCHOR, Toplevel, PhotoImage, Canvas, Button, StringVar, Listbox, Label

class Cennik():
    def __init__(self):
        window = Toplevel()

        window.title('Cennik')
        window.geometry('1920x1080')

        bg2 = PhotoImage(file="bg.png")
        canvas3 = Canvas(window,width=1920, height=1080)
        canvas3.pack(fill="both",expand=True)
        canvas3.create_image(0,0, image=bg2, anchor="nw")

        listbox = Listbox(window, font = ("Times New Roman", 20), selectmode = "extended")

        ofert = ["Normalny", "Studenci", "Emeryci", "Młodzież do 18 lat", "PROMOCJA"]

        ofert = StringVar(value = ofert)

        listbox.config(listvariable = ofert)
        listbox.place(x = 900, y = 300, anchor= "ne")

        buttonW = Button(window, font = ("Times New Roman", 20), text="Wybierz", borderwidth = 3, bg = "green", command = lambda: Cennik.listbox(listbox, window))
        buttonWc = canvas3.create_window(1050, 330, window = buttonW)
    

        zamknij = PhotoImage(file = "back.png")

        buttonZ = Button(window, image = zamknij, bg = "green", command = lambda: Cennik.buttonDestoy(window))
        buttonZc = canvas3.create_window(1500, 30, window = buttonZ)

        canvas3.create_text(770, 200, font=("Times New Roman", 50), text = "Cennik", fill = "white")

        window.mainloop()

    def open_cennik():
        Cennik()

    def buttonDestoy(window):
        window.destroy()

    def listbox(listbox, window):
        oferta = listbox.get(ANCHOR)

        informacja = Label(window,  font = ("Times New Roman", 20), bg = "white", width = 30, height = 3)
        informacja.place(x = 920, y = 400)

        if oferta == "Studenci":

            
            #  status = pandas.
            #  spret = ...

            #  textinfo = "hueahgufegufe " + str(0)

            informacja.config( text = "Ta oferta kosztuje: 80 złoty na miesiąc")

        if oferta == "Normalny":
            informacja.config( text = "Ta oferta kosztuje: 120 złoty na miesiąc")

        if oferta == "Emeryci":
            informacja.config( text = "Ta oferta kosztuje: 100 złoty na miesiąc")

        if oferta == "Młodzież do 18 lat":
            informacja.config( text = "Ta oferta kosztuje: 90 złoty na miesiąc")

        if oferta == "PROMOCJA":
            informacja.config( text = "Kup karnet na 3 miesiące, zapłać za 2")

        