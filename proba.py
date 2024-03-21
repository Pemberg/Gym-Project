import tkinter as tk

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("Nowe okno")
    new_window.geometry("200x200")
    new_window.mainloop()

root = tk.Tk()
root.title("Główne okno")
root.geometry("300x200")

button = tk.Button(root, text="Otwórz nowe okno", command=open_new_window)
button.pack(pady=10)

root.mainloop()