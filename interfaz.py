import tkinter as tk
from tkinter import messagebox


def login():
    usuario = entry_user.get()
    clave = entry_pass.get()

    if usuario == "admin" and clave == "1234":
        messagebox.showinfo("Login", "Ingreso exitoso")
    else:
        messagebox.showerror("Login", "Usuario o clave incorrectos")




root = tk.Tk()
root.title("Interfaz con Tkinter")
root.geometry("400x300")


menu_bar = tk.Menu(root)

menu_archivo = tk.Menu(menu_bar, tearoff=0)
menu_archivo.add_command(label="Salir", command=root.quit)
menu_bar.add_cascade(label="Archivo", menu=menu_archivo)

menu_editar = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Editar", menu=menu_editar)

menu_ayuda = tk.Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label="Ayuda", menu=menu_ayuda)

root.config(menu=menu_bar)


login_frame = tk.LabelFrame(root, text="Login", padx=20, pady=20)
login_frame.pack(pady=30)

tk.Label(login_frame, text="Usuario").grid(row=0, column=0)
entry_user = tk.Entry(login_frame)
entry_user.grid(row=0, column=1)

tk.Label(login_frame, text="Clave").grid(row=1, column=0)
entry_pass = tk.Entry(login_frame, show="*")
entry_pass.grid(row=1, column=1)

tk.Button(login_frame, text="Ingresar", command=login).grid(row=2, column=0, columnspan=2, pady=10)


root.mainloop()