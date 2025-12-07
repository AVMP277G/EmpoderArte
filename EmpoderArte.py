import tkinter as tk
import random

def main():
    #Parte Lógica 
    nombre = input("Ingresa tu nombre: ")
    meta = input("Ingresa tu meta: ")

    frases_base = [
        f"{nombre}, estás más cerca de {meta} de lo que imaginas.",
        f"No olvides, {nombre}: {meta} también te está buscando a ti.",
        f"Cada paso que das, {nombre}, te acerca inevitablemente a {meta}.",
        f"El mundo espera verte lograr {meta}, {nombre}.",
        f"{nombre}, hoy es el día perfecto para avanzar hacia {meta}."
    ]

    fondos = ["#FF5733", "#FF8D1A", "#FFC300", "#FF6F61", "#F39C12", "#D35400"]
    colores_texto = ["#FFFFFF", "#000000", "#2C2C54", "#4A235A", "#1B4F72", "#7D3C98"]
    fuentes = ["Arial", "Comic Sans MS", "Georgia", "Verdana", "Helvetica", "Times New Roman"]
    tamanos = [18, 22, 26, 30, 34, 38]

    #Parte Gráfica
    ventana = tk.Tk()
    ventana.title("Generador de frases motivadoras")
    ventana.geometry("800x500")

    etiqueta = tk.Label(
        ventana,
        text="Haz clic en cualquier parte para generar tu frase",
        wraplength=700,
        justify="center"
    )
    etiqueta.pack(expand=True)

    def cambiar_frase(event=None):
        nueva_frase = random.choice(frases_base)
        nuevo_fondo = random.choice(fondos)
        nuevo_color = random.choice(colores_texto)
        nueva_fuente = random.choice(fuentes)
        nuevo_tamano = random.choice(tamanos)

        ventana.config(bg=nuevo_fondo)

        etiqueta.config(
            text=nueva_frase,
            bg=nuevo_fondo,
            fg=nuevo_color,
            font=(nueva_fuente, nuevo_tamano, "bold")
        )

        print(nueva_frase)

    ventana.bind("<Button-1>", cambiar_frase)
    ventana.bind("<Return>", cambiar_frase)

    ventana.mainloop()


if __name__ == "__main__":
    main()
