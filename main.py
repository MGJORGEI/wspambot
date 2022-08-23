from unittest import addModuleCleanup
import pyautogui, webbrowser
from time import sleep
import emoji

print('Seleccione una opcion\n1.-Boot personalizado con ciclo\n2.-Boot con Texto')
opc = int(input("Ingrese una opcion : "))

if opc == 1:
    vecs = int(input("Cuantas veces lo molestamos? : "))
    webbrowser.open('https://web.whatsapp.com/send?phone=+AQUI TU TELEFONO')
    sleep(10)
    
    for i in range(vecs):
        pyautogui.typewrite('Saludos Humano... Soy el Bot :-p de Jorge Montero :)\nEsto es una prueba \nde spam :-\ ')
        pyautogui.press("enter")
    

if opc ==2:
    webbrowser.open('https://web.whatsapp.com/send?phone=+AQUI TU TELEFONO')
    sleep(10)
    with open ("spam.txt", "r") as file:
        for line in file:
            pyautogui.typewrite(line)
            pyautogui.press("enter")