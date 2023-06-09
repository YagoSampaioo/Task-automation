import pyautogui #permite automatizar o movimento do mouse, teclado e digitação.
import time
from time import sleep #permite que a execução seja pausado por alguns segundos.as
import schedule #usada para agendar a execução de tarefas em horários específicos
from datetime import datetime

# Clicar na seguinte coordenada usei o "pyautogui.click(000,000)";
# Para determinar a duração para clicar usei o "duration=0".
pyautogui.click(1244,1079,duration=4)
pyautogui.click(733,479,duration=4)
pyautogui.click(166,704,duration=2)
pyautogui.click(432,977,duration=2)
# Para escrever no último elemento clicado usei o "pyautogui.write('texto')".
pyautogui.write('Isso é um teste')
pyautogui.click(1838,1024,duration=1)