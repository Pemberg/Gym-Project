from ctypes import resize
from tkinter import Tk, PhotoImage, Canvas, Button
from tkinter.font import BOLD
from tkinter.messagebox import showinfo
import dni, cennik


class App():
    def __init__(self):
        window = Tk()

        window.title('Silownia')
        window.geometry('1920x1080')
       
        bg = PhotoImage(file="bg.png")
        canvas1 = Canvas(window,width=1920, height=1080)
        canvas1.pack(fill="both",expand=True)
        canvas1.create_image(0,0, image=bg, anchor="nw")

        buttonH = Button(window, text='Informacja', command = lambda: App.buttonHelp_clicked())
        buttonHc = canvas1.create_window(60, 30, window = buttonH)

        zamknij = PhotoImage(file = "zam.png")


        buttonZ = Button(window,  image = zamknij, bg = "red", command = lambda: App.buttonDestoy(window))
        buttonZc = canvas1.create_window(1500, 30, window = buttonZ)


        button1 = Button(window, font=("Times New Roman", 15, BOLD), text = 'Wybierz termin', height=3, width=30, command = lambda: dni.Dni.open_dni())
        button1c = canvas1.create_window(360, 530, window = button1)

        button2 = Button(window, font=("Times New Roman", 15, BOLD), text='Cennik', height=3, width=30, command = lambda: cennik.Cennik.open_cennik())
        button2c = canvas1.create_window(1160, 530, window = button2)
    

        canvas1.create_text(775, 200, font=("Times New Roman", 50), text="Witaj na siłowni", fill= "black")
        canvas1.create_text(770, 200, font=("Times New Roman", 50), text="Witaj na siłowni", fill= "white")

        window.mainloop()

    def buttonHelp_clicked():
        showinfo(title='Informacja', message='Ten program pozwoli ci wybrać odpowiedni dzień na trening')

    def buttonDestoy(window):
        window.destroy()


App()