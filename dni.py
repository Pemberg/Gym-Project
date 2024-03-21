from tkinter import Toplevel, PhotoImage, Canvas, Button 
import godzina

class Dni():
    def __init__(self):
        window = Toplevel()

        window.title('Dni tygodnia')
        window.geometry('1920x1080')

        bg2 = PhotoImage(file="bg.png")
        canvas2 = Canvas(window, width=1920, height=1080)
        canvas2.pack(fill="both", expand=True)
        canvas2.create_image(0,0, image=bg2, anchor = "nw")

        zamknij = PhotoImage(file = "back.png")

        buttonZ = Button(window, image = zamknij, bg = "green", command = lambda: Dni.buttonDestoy(window))
        buttonZc = canvas2.create_window(1500, 30, window = buttonZ)

        dodatek = PhotoImage(file="bieznia.png")
        canvas2.create_image(120,500, image = dodatek, anchor = "nw")

        dodatek1 = PhotoImage(file="silny.png")
        canvas2.create_image(1120,500, image = dodatek1, anchor = "nw")

        canvas2.create_text(770, 200, font=("Times New Roman", 50), text="Wybierz dzień, który ci odpowiada", fill= "white")

        buttonM = Button(window, font=("Times New Roman", 12), text='Poniedziałek', height=3, width=20, bg = "lightblue", command = lambda: godzina.Poniedzialek.open_godzina())
        buttonMc = canvas2.create_window(150, 400, window = buttonM)

        buttonWt = Button(window, font=("Times New Roman", 12), text='Wtorek', height=3, width=20, bg = "lightblue", command = lambda: godzina.Wtorek.open_godzina())
        buttonWtc = canvas2.create_window(450, 400, window = buttonWt)

        buttonSr = Button(window, font=("Times New Roman", 12), text='Środa', height=3, width=20, bg = "lightblue", command = lambda: godzina.Sroda.open_godzina())
        buttonSrc = canvas2.create_window(750, 400, window = buttonSr)

        buttonC = Button(window, font=("Times New Roman", 12), text='Czwartek', height=3, width=20, bg = "lightblue", command = lambda: godzina.Czwartek.open_godzina())
        buttonCc = canvas2.create_window(1050, 400, window = buttonC)

        buttonP = Button(window, font=("Times New Roman", 12), text='Piątek', height=3, width=20, bg = "lightblue", command = lambda: godzina.Piatek.open_godzina())
        buttonPc = canvas2.create_window(1350, 400, window = buttonP)

        buttonSo = Button(window, font=("Times New Roman", 12), text='Sobota', height=3, width=20, bg = "grey", command = lambda: godzina.Sobota.open_godzina())
        buttonSoc = canvas2.create_window(600, 550, window = buttonSo)

        buttonN = Button(window, font=("Times New Roman", 12), text='Niedziela', height=3, width=20, bg = "grey", command = lambda: godzina.Niedziela.open_godzina())
        buttonNc = canvas2.create_window(900, 550, window = buttonN)

        
        window.mainloop()


    def open_dni():
        Dni()

    def buttonDestoy(window):
        window.destroy()