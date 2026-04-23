import keyboard

with open("ejercicio.txt", "a") as archivo:
    def entrar(event):
        archivo.write(event.name + "\n")
    
    keyboard.on_press(entrar)
    keyboard.wait("esc")  