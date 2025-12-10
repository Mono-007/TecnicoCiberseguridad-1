import tkinter as tk

# 1. Ventana básica con mensaje de bienvenida
def ventana_bienvenida():
    root = tk.Tk()
    root.title("Bienvenida")

    tk.Label(root, text="¡Bienvenido a la aplicación Tkinter!", font=("Arial", 14)).pack(pady=20)

    root.mainloop()


# 2. Entry + Button que muestra el texto en un Label
def ventana_entry_label():
    root = tk.Tk()
    root.title("Entrada de texto")

    entry = tk.Entry(root)
    entry.pack(pady=10)

    label_mensaje = tk.Label(root, text="")
    label_mensaje.pack(pady=10)

    def mostrar():
        label_mensaje.config(text=entry.get())

    tk.Button(root, text="Mostrar", command=mostrar).pack()
    root.mainloop()


# 3. Calculadora simple (suma)
def ventana_calculadora():
    root = tk.Tk()
    root.title("Calculadora")

    tk.Label(root, text="Número 1:").pack()
    n1 = tk.Entry(root)
    n1.pack()

    tk.Label(root, text="Número 2:").pack()
    n2 = tk.Entry(root)
    n2.pack()

    label_resultado = tk.Label(root, text="Resultado:")
    label_resultado.pack(pady=10)

    def sumar():
        try:
            r = float(n1.get()) + float(n2.get())
            label_resultado.config(text=f"Resultado: {r}")
        except:
            label_resultado.config(text="Error: ingresa números válidos")

    tk.Button(root, text="Sumar", command=sumar).pack()
    root.mainloop()


# 4. Listbox que permite agregar elementos
def ventana_listbox():
    root = tk.Tk()
    root.title("Lista de elementos")

    lista = tk.Listbox(root)
    lista.pack(pady=10)

    entry = tk.Entry(root)
    entry.pack()

    def agregar():
        texto = entry.get()
        if texto:
            lista.insert(tk.END, texto)
            entry.delete(0, tk.END)

    tk.Button(root, text="Agregar", command=agregar).pack(pady=5)
    root.mainloop()


# 5. Canvas donde se pueda dibujar líneas presionando el mouse
def ventana_canvas_dibujo():
    root = tk.Tk()
    root.title("Canvas - Dibujar")

    canvas = tk.Canvas(root, width=500, height=300, bg="white")
    canvas.pack()

    def dibujar(event):
        x, y = event.x, event.y
        canvas.create_oval(x, y, x+3, y+3, fill="black")

    canvas.bind("<B1-Motion>", dibujar)

    root.mainloop()


# ➤ Ejecuta la función que quieras probar:
if __name__ == "__main__":
    print("Ejecuta la ventana que necesites:")
    print("ventana_bienvenida()")
    print("ventana_entry_label()")
    print("ventana_calculadora()")
    print("ventana_listbox()")
    print("ventana_canvas_dibujo()")

