import pyautogui
from time import sleep
import winsound

sleep(5)
print(pyautogui.position())
winsound.Beep(440, 500)

# winsound.Beep(440, 500)
# sleep(0.1)
# winsound.Beep(440, 500)
# sleep(0.1)
# winsound.Beep(440, 500)
#
#
# for x in range(9):
#     winsound.Beep(440, 500)
#     sleep(2)
#     with open("spis.txt", "a") as text_file:
#         text_file.writelines("1: " + str(pyautogui.position()) + '\n')


