import pyautogui
import time

# Pequeno delay para posicionar o mouse antes de capturar as coordenadas
time.sleep(5)

# Exibe a posição atual do cursor (x, y) — útil para mapear cliques
print(pyautogui.position())