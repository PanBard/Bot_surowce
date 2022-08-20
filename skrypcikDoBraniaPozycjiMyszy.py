import pyautogui
from time import sleep
import winsound

sleep(1)
print(pyautogui.position())


winsound.Beep(440, 500)
sleep(0.1)
winsound.Beep(440, 500)
sleep(0.1)
winsound.Beep(440,3000)
sleep(2)

lista = ["dzwiek", "niska1", "niska2", "niska3", "ptaszek" ]

for x in range(len(lista)):
    winsound.Beep(440, 500)
    sleep(3)
    with open("spis.txt", "a") as text_file:
        text_file.writelines(f"{x} {lista[x]}: " + str(pyautogui.position()) + '\n')


