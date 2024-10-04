import pyautogui
import time

# Esperar 5 segundos antes de capturar as coordenadas, para dar tempo de mover o mouse
print("Mova o mouse para o local desejado nos próximos 5 segundos...")
time.sleep(5)

# Captura a posição atual do mouse
x, y = pyautogui.position()

print(f'As coordenadas do mouse são: X={x}, Y={y}')
