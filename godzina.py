from tkinter import Toplevel, PhotoImage, Canvas, Button, Entry, Label
import pandas as pd

class Poniedzialek():
    def __init__(self):
        window = Toplevel()

        window.title('Poniedziałek')
        window.geometry('1920x1080')

        bg2 = PhotoImage(file="bg.png")
        canvas3 = Canvas(window,width=1920, height=1080)
        canvas3.pack(fill="both",expand=True)
        canvas3.create_image(0,0, image=bg2, anchor="nw")

        zamknij = PhotoImage(file = "back.png")

        buttonZ = Button(window, image = zamknij, bg = "green", command = lambda: Poniedzialek.buttonDestoy(window))
        buttonZc = canvas3.create_window(1500, 30, window = buttonZ)

        canvas3.create_text(770, 200, font=("Times New Roman", 50), text="Poniedziałek", fill= "white")

        canvas3.create_text(770, 300, font=("Times New Roman", 30), text="Wpisz odpowiadającą ci godzinę", fill= "white")


        entry_godzina = Entry(window, font=("Times New Roman", 20))
        canvas3.create_window(770, 400, window = entry_godzina)

        buttonZ = Button(window, font=("Times New Roman", 12), text='Zatwierdź', height=3, width=20, bg = "red", command = lambda: Poniedzialek.show_info(entry_godzina, window))
        buttonZc = canvas3.create_window(770, 500, window = buttonZ)

        window.mainloop()

    def open_godzina():
        Poniedzialek()

    def buttonDestoy(window):
        window.destroy()

    def show_info(entry, window): 
        x = int(entry.get()) 

        label = Label(window, font=("Times New Roman", 20),  width = 50, height = 3)
        label.place(x = 400, y = 600)

        if x in [1, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]: 
            
            df = pd.read_excel("Tydzien.xlsx")

            df = df.loc[df["Dni"]=="Poniedziałek"]

            df = df.iloc[0, x + 1]
        
            df = str(df)
            
            text = "Na siłowni jest zajęte " + df + " sztuk sprzętu"
            label.config( text = text)

        elif x in [3, 4, 5, 6]:
            
            label.config(text = "Siłownia jest zamknięta, wybierz inną godzinę")

        else:
            label.config(text = "Nie ma takiej godziny, spróbuj ponownie")
              

class Wtorek():
    def __init__(self):
        window = Toplevel()

        window.title('Wtorek')
        window.geometry('1920x1080')

        bg2 = PhotoImage(file="bg.png")
        canvas3 = Canvas(window,width=1920, height=1080)
        canvas3.pack(fill="both",expand=True)
        canvas3.create_image(0,0, image=bg2, anchor="nw")

        zamknij = PhotoImage(file = "back.png")

        buttonZ = Button(window, image = zamknij, bg = "green", command = lambda: Wtorek.buttonDestoy(window))
        buttonZc = canvas3.create_window(1500, 30, window = buttonZ)

        canvas3.create_text(770, 200, font=("Times New Roman", 50), text="Wtorek", fill= "white")

        canvas3.create_text(770, 300, font=("Times New Roman", 30), text="Wpisz odpowiadającą ci godzinę", fill= "white")

        entry_godzina = Entry(window, font=("Times New Roman", 20))
        canvas3.create_window(770, 400, window = entry_godzina)

        buttonZ = Button(window, font=("Times New Roman", 12), text='Zatwierdź', height=3, width=20, bg = "red", command = lambda: Wtorek.show_info(entry_godzina, window))
        buttonZc = canvas3.create_window(770, 500, window = buttonZ)

        window.mainloop()

    def open_godzina():
        Wtorek()

    def buttonDestoy(window):
        window.destroy()

    def show_info(entry, window): 
        x = int(entry.get()) 

        label = Label(window, font=("Times New Roman", 20),  width = 50, height = 3)
        label.place(x = 400, y = 600)

        if x in [1, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]: 
            
            df = pd.read_excel("Tydzien.xlsx")

            df = df.loc[df["Dni"]=="Wtorek"]

            df = df.iloc[0, x + 1]
        
            df = str(df)
            
            text = "Na siłowni jest zajęte " + df + " sztuk sprzętu"
            label.config( text = text)

        elif x in [3, 4, 5, 6]:
            
            label.config(text = "Siłownia jest zamknięta, wybierz inną godzinę")

        else:
            label.config(text = "Nie ma takiej godziny, spróbuj ponownie")
    

class Sroda():
    def __init__(self):
        window = Toplevel()

        window.title('Środa')
        window.geometry('1920x1080')

        bg2 = PhotoImage(file="bg.png")
        canvas3 = Canvas(window,width=1920, height=1080)
        canvas3.pack(fill="both",expand=True)
        canvas3.create_image(0,0, image=bg2, anchor="nw")

        zamknij = PhotoImage(file = "back.png")

        buttonZ = Button(window, image = zamknij, bg = "green", command = lambda: Sroda.buttonDestoy(window))
        buttonZc = canvas3.create_window(1500, 30, window = buttonZ)

        canvas3.create_text(770, 200, font=("Times New Roman", 50), text="Środa", fill= "white")

        canvas3.create_text(770, 300, font=("Times New Roman", 30), text="Wpisz odpowiadającą ci godzinę", fill= "white")

        entry_godzina = Entry(window, font=("Times New Roman", 20))
        canvas3.create_window(770, 400, window = entry_godzina)

        buttonZ = Button(window, font=("Times New Roman", 12), text='Zatwierdź', height=3, width=20, bg = "red", command = lambda: Sroda.show_info(entry_godzina, window))
        buttonZc = canvas3.create_window(770, 500, window = buttonZ)

        window.mainloop()

    def open_godzina():
        Sroda()

    def buttonDestoy(window):
        window.destroy()  

    def show_info(entry, window): 
        x = int(entry.get()) 

        label = Label(window, font=("Times New Roman", 20),  width = 50, height = 3)
        label.place(x = 400, y = 600)

        if x in [1, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]: 
            
            df = pd.read_excel("Tydzien.xlsx")

            df = df.loc[df["Dni"]=="Środa"]

            df = df.iloc[0, x + 1]
        
            df = str(df)
            
            text = "Na siłowni jest zajęte " + df + " sztuk sprzętu"
            label.config( text = text)

        elif x in [3, 4, 5, 6]:
            
            label.config(text = "Siłownia jest zamknięta, wybierz inną godzinę")

        else:
            label.config(text = "Nie ma takiej godziny, spróbuj ponownie")      


class Czwartek():
    def __init__(self):
        window = Toplevel()

        window.title('Czwartek')
        window.geometry('1920x1080')

        bg2 = PhotoImage(file="bg.png")
        canvas3 = Canvas(window,width=1920, height=1080)
        canvas3.pack(fill="both",expand=True)
        canvas3.create_image(0,0, image=bg2, anchor="nw")

        zamknij = PhotoImage(file = "back.png")

        buttonZ = Button(window, image = zamknij, bg = "green", command = lambda: Czwartek.buttonDestoy(window))
        buttonZc = canvas3.create_window(1500, 30, window = buttonZ)

        canvas3.create_text(770, 200, font=("Times New Roman", 50), text="Czwartek", fill= "white")

        canvas3.create_text(770, 300, font=("Times New Roman", 30), text="Wpisz odpowiadającą ci godzinę", fill= "white")

        entry_godzina = Entry(window, font=("Times New Roman", 20))
        canvas3.create_window(770, 400, window = entry_godzina)

        buttonZ = Button(window, font=("Times New Roman", 12), text='Zatwierdź', height=3, width=20, bg = "red", command = lambda: Czwartek.show_info(entry_godzina, window))
        buttonZc = canvas3.create_window(770, 500, window = buttonZ)

        window.mainloop()

    def open_godzina():
        Czwartek()

    def buttonDestoy(window):
        window.destroy()

    def show_info(entry, window): 
        x = int(entry.get()) 

        label = Label(window, font=("Times New Roman", 20),  width = 50, height = 3)
        label.place(x = 400, y = 600)

        if x in [1, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]: 
            
            df = pd.read_excel("Tydzien.xlsx")

            df = df.loc[df["Dni"]=="Czwartek"]

            df = df.iloc[0, x + 1]
        
            df = str(df)
            
            text = "Na siłowni jest zajęte " + df + " sztuk sprzętu"
            label.config( text = text)

        elif x in [3, 4, 5, 6]:
            
            label.config(text = "Siłownia jest zamknięta, wybierz inną godzinę")

        else:
            label.config(text = "Nie ma takiej godziny, spróbuj ponownie")

class Piatek():
    def __init__(self):
        window = Toplevel()

        window.title('Piątek')
        window.geometry('1920x1080')

        bg2 = PhotoImage(file="bg.png")
        canvas3 = Canvas(window,width=1920, height=1080)
        canvas3.pack(fill="both",expand=True)
        canvas3.create_image(0,0, image=bg2, anchor="nw")

        zamknij = PhotoImage(file = "back.png")

        buttonZ = Button(window, image = zamknij, bg = "green", command = lambda: Piatek.buttonDestoy(window))
        buttonZc = canvas3.create_window(1500, 30, window = buttonZ)

        canvas3.create_text(770, 200, font=("Times New Roman", 50), text="Piątek", fill= "white")

        canvas3.create_text(770, 300, font=("Times New Roman", 30), text="Wpisz odpowiadającą ci godzinę", fill= "white")

        entry_godzina = Entry(window, font=("Times New Roman", 20))
        canvas3.create_window(770, 400, window = entry_godzina)

        buttonZ = Button(window, font=("Times New Roman", 12), text='Zatwierdź', height=3, width=20, bg = "red", command = lambda: Piatek.show_info(entry_godzina, window))
        buttonZc = canvas3.create_window(770, 500, window = buttonZ)

        window.mainloop()

    def open_godzina():
        Piatek()

    def buttonDestoy(window):
        window.destroy()

    def show_info(entry, window): 
        x = int(entry.get()) 

        label = Label(window, font=("Times New Roman", 20),  width = 50, height = 3)
        label.place(x = 400, y = 600)

        if x in [1, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]: 
            
            df = pd.read_excel("Tydzien.xlsx")

            df = df.loc[df["Dni"]=="Piątek"]

            df = df.iloc[0, x + 1]
        
            df = str(df)
            
            text = "Na siłowni jest zajęte " + df + " sztuk sprzętu"
            label.config( text = text)

        elif x in [3, 4, 5, 6]:
            
            label.config(text = "Siłownia jest zamknięta, wybierz inną godzinę")

        else:
            label.config(text = "Nie ma takiej godziny, spróbuj ponownie")


class Sobota():
    def __init__(self):
        window = Toplevel()

        window.title('Sobota')
        window.geometry('1920x1080')

        bg2 = PhotoImage(file="bg.png")
        canvas3 = Canvas(window,width=1920, height=1080)
        canvas3.pack(fill="both",expand=True)
        canvas3.create_image(0,0, image=bg2, anchor="nw")

        zamknij = PhotoImage(file = "back.png")

        buttonZ = Button(window, image = zamknij, bg = "green", command = lambda: Sobota.buttonDestoy(window))
        buttonZc = canvas3.create_window(1500, 30, window = buttonZ)

        canvas3.create_text(770, 200, font=("Times New Roman", 50), text="Sobota", fill= "white")

        canvas3.create_text(770, 300, font=("Times New Roman", 30), text="Wpisz odpowiadającą ci godzinę", fill= "white")

        entry_godzina = Entry(window, font=("Times New Roman", 20))
        canvas3.create_window(770, 400, window = entry_godzina)

        buttonZ = Button(window, font=("Times New Roman", 12), text='Zatwierdź', height=3, width=20, bg = "red", command = lambda: Sobota.show_info(entry_godzina, window))
        buttonZc = canvas3.create_window(770, 500, window = buttonZ)

        window.mainloop()

    def open_godzina():
        Sobota()

    def buttonDestoy(window):
        window.destroy()

    def show_info(entry, window): 
        x = int(entry.get()) 

        label = Label(window, font=("Times New Roman", 20),  width = 50, height = 3)
        label.place(x = 400, y = 600)

        if x in [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]: 
            
            df = pd.read_excel("Tydzien.xlsx")

            df = df.loc[df["Dni"]=="Sobota"]

            df = df.iloc[0, x + 1]
        
            df = str(df)
            
            text = "Na siłowni jest zajęte " + df + " sztuk sprzętu"
            label.config( text = text)

        elif x in [1, 2, 3, 4, 5, 6, 23, 24]:
            
            label.config(text = "Siłownia jest zamknięta, wybierz inną godzinę")

        else:
            label.config(text = "Nie ma takiej godziny, spróbuj ponownie")

class Niedziela():
    def __init__(self):
        window = Toplevel()

        window.title('Niedziela')
        window.geometry('1920x1080')

        bg2 = PhotoImage(file="bg.png")
        canvas3 = Canvas(window,width=1920, height=1080)
        canvas3.pack(fill="both",expand=True)
        canvas3.create_image(0,0, image=bg2, anchor="nw")

        zamknij = PhotoImage(file = "back.png")

        buttonZ = Button(window, image = zamknij, bg = "green", command = lambda: Niedziela.buttonDestoy(window))
        buttonZc = canvas3.create_window(1500, 30, window = buttonZ)

        canvas3.create_text(770, 200, font=("Times New Roman", 50), text="Niedziela", fill= "white")

        canvas3.create_text(770, 300, font=("Times New Roman", 30), text="Wpisz odpowiadającą ci godzinę", fill= "white")

        entry_godzina = Entry(window, font=("Times New Roman", 20))
        canvas3.create_window(770, 400, window = entry_godzina)

        buttonZ = Button(window, font=("Times New Roman", 12), text='Zatwierdź', height=3, width=20, bg = "red", command = lambda: Niedziela.show_info(entry_godzina, window))
        buttonZc = canvas3.create_window(770, 500, window = buttonZ)

        window.mainloop()

    def open_godzina():
        Niedziela()

    def buttonDestoy(window):
        window.destroy()

    def show_info(entry, window): 
        x = int(entry.get()) 

        label = Label(window, font=("Times New Roman", 20),  width = 50, height = 3)
        label.place(x = 400, y = 600)

        if x in [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]: 
            
            df = pd.read_excel("Tydzien.xlsx")

            df = df.loc[df["Dni"]=="Niedziela"]

            df = df.iloc[0, x + 1]
        
            df = str(df)
            
            text = "Na siłowni jest zajęte " + df + " sztuk sprzętu"
            label.config( text = text)

        elif x in [1, 2, 3, 4, 5, 6, 23, 24]:
            
            label.config(text = "Siłownia jest zamknięta, wybierz inną godzinę")

        else:
            label.config(text = "Nie ma takiej godziny, spróbuj ponownie")