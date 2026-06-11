import tkinter as tk
from tkinter import ttk, messagebox


from tkinter import messagebox
import tkinter as tk

messagebox.showinfo("Info", "Probando messagebox")
messagebox.showwarning("Aviso", "probando ventana de emergencia!!")
messagebox.showerror("Error", "oh no hubo un error")


respuesta = messagebox.askyesno("Pregunta", "¿aprobe el trabajo?")
print(respuesta)  