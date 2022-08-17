import cv2 as cv
import numpy as np
import pyautogui
import win32gui, win32ui, win32con
from time import sleep, time
import  os
from datetime import datetime

class Robotnik:

    plik_txt = open('lista.txt')
    nazwa_celu = plik_txt.readlines()
    plik_txt.close()
    window_offset = (0, 0)
    WLACZ_HANDEL = False
    WLACZ_POZYCJONOWANIE_MAPY = False
    WYSYLANIE_SUREK_PROMERIUM = False
    WYSYLANIE_SUREK_DUR_i_PROMETID = False
    analizowany_zrzut_ekranu = None
    ilosc_PROMERIUM = None
    ilosc_duranium = None
    ilosc_prometid = None
    numer_celu_do_skrina = None

    w = 0
    h = 0
    hwnd = None
    cropped_x = 0
    cropped_y = 0
    offset_x = 0
    offset_y = 0
    screen_x = None
    screen_y = None

    def wykryj_i_kliknij(self, numer_celu, threshold=0.8):


        ############# zrzut ekranu poczatek

        self.hwnd = win32gui.GetDesktopWindow()

        window_rect = win32gui.GetWindowRect(self.hwnd)
        self.w = window_rect[2] - window_rect[0]
        self.h = window_rect[3] - window_rect[1]

        border_pixels = 0
        titlebar_pixels = 0
        self.w = self.w - (border_pixels * 2)
        self.h = self.h - titlebar_pixels - border_pixels

        self.cropped_x = border_pixels
        self.cropped_y = titlebar_pixels

        self.offset_x = window_rect[0] + self.cropped_x
        self.offset_y = window_rect[1] + self.cropped_y

        #

        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (self.cropped_x, self.cropped_y), win32con.SRCCOPY)

        # dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')

        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.h, self.w, 4)

        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        img = img[..., :3]

        self.analizowany_zrzut_ekranu = np.ascontiguousarray(img)

        ############## zrzut ekranu koniec


        # run the OpenCV algorithm
        szukany_obrazek = cv.imread('img/' + self.nazwa_celu[numer_celu].rstrip('\n'), cv.IMREAD_UNCHANGED) #dodanie rstrip('\n') usuwa znak następnej linii i dzieki temu dziala
        result = cv.matchTemplate(self.analizowany_zrzut_ekranu, szukany_obrazek, cv.TM_CCOEFF_NORMED)

        # Get the all the positions from the match result that exceed our threshold
        szukany_obrazek_w = szukany_obrazek.shape[1]
        szukany_obrazek_h = szukany_obrazek.shape[0]

        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))
        # print(locations)

        # You'll notice a lot of overlapping rectangles get drawn. We can eliminate those redundant
        # locations by using groupRectangles().
        # First we need to create the list of [x, y, w, h] rectangles
        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), szukany_obrazek_w, szukany_obrazek_h]
            # Add every box to the list twice in order to retain single (non-overlapping) boxes
            rectangles.append(rect)
            rectangles.append(rect)
        # Apply group rectangles.
        # The groupThreshold parameter should usually be 1. If you put it at 0 then no grouping is
        # done. If you put it at 2 then an object needs at least 3 overlapping rectangles to appear
        # in the result. I've set eps to 0.5, which is:
        # "Relative difference between sides of the rectangles to merge them into a group."
        rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)
        # print(rectangles)

        points = []

        # Loop over all the rectangles
        for (x, y, w, h) in rectangles:
            # Determine the center position
            center_x = x + int(w / 2)
            center_y = y + int(h / 2)
            # Save the points
            self.screen_x = center_x + self.window_offset[0]
            self.screen_y = center_y + self.window_offset[1]

        if self.screen_x and self.screen_y:
            pyautogui.moveTo(x=self.screen_x, y=self.screen_y)
            sleep(0.5)
            pyautogui.click()
            print("Przesunieto kursor myszy na wspolrzedne: ", f"[ {self.screen_x}]", f"[ {self.screen_y},]")

            #aktualny czas
            now = datetime.now()
            aktualny_czas = now.strftime("%H:%M:%S")

            #spisywanie czynności
            obiekt = self.nazwa_celu[numer_celu].rstrip('\n')
            # It is strongly advised to use a context manager. As an advantage, it is made sure the file is always closed, no matter what:
            with open("Raport.txt", "a") as text_file:
                text_file.writelines( f"-[{aktualny_czas}]- "+"Wykonano przesuniecie kursora na pozycje: " + obiekt.rstrip('.JPG') + f" o wspolrzednych: {self.screen_x , self.screen_y}"+'\n')


            if self.WLACZ_HANDEL:
                sleep(0.5)
                pyautogui.click(self.screen_x - 32, self.screen_y + 166)
                sleep(1)

                pyautogui.click(self.screen_x + 53, self.screen_y + 166)
                sleep(1)

                pyautogui.click(self.screen_x + 125, self.screen_y + 166)
                sleep(1)

                pyautogui.click(self.screen_x + 205, self.screen_y + 166)
                sleep(1)

                pyautogui.click(self.screen_x + 288, self.screen_y + 166)
                sleep(1)

                pyautogui.click(self.screen_x + 372, self.screen_y + 166)
                sleep(1)

                pyautogui.click(self.screen_x + 449, self.screen_y + 166)
                sleep(1)

                pyautogui.click(self.screen_x + 602, self.screen_y + 166)
                sleep(1)

                print("sekwencja handlowa skonczona")

            if self.WLACZ_POZYCJONOWANIE_MAPY:
                sleep(0.5)
                pyautogui.moveTo(self.screen_x + 142, self.screen_y + 139)
                sleep(0.5)
                pyautogui.click()
                sleep(0.5)

                print("sekwencja pozycjonowania na mapie skonczona")

            if self.WYSYLANIE_SUREK_PROMERIUM:
                sleep(1)
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab') #prometid
                pyautogui.press('tab') #duranium
                pyautogui.press('tab') # xeno
                pyautogui.press('tab') # promerium
                sleep(0.5)
                pyautogui.write(self.ilosc_PROMERIUM)
                sleep(0.5)
                pyautogui.press('tab') #seprom

            if self.WYSYLANIE_SUREK_DUR_i_PROMETID:
                sleep(1)
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab')
                pyautogui.press('tab') #prometid
                sleep(0.5)
                pyautogui.write(self.ilosc_prometid)
                sleep(0.5)
                pyautogui.press('tab') #duranium
                sleep(0.5)
                pyautogui.write(self.ilosc_duranium)
                sleep(0.5)
                pyautogui.press('tab') # xeno
                pyautogui.press('tab') # promerium
                pyautogui.press('tab') #seprom

            self.screen_x = None
            self.screen_y = None
            return True

        else:
            # aktualny czas
            now = datetime.now()
            aktualny_czas = now.strftime("%H:%M:%S")

            print("Nie znaleziono obiektu")
            obiekt = self.nazwa_celu[numer_celu].rstrip('\n')
            obiekt2 = obiekt.rstrip('.JPG')
            with open("Raport.txt", "a") as text_file:
                text_file.writelines( f"-[{aktualny_czas}]- "+"Nie znaleziono obiektu z pozycji: " + obiekt.rstrip('.JPG') + '\n')

            if numer_celu != self.numer_celu_do_skrina:
                cv.imwrite(f'skriny/{obiekt2, time()}.jpg', self.analizowany_zrzut_ekranu) #zapisanie skrina

            self.numer_celu_do_skrina = numer_celu
            self.screen_x = None
            self.screen_y = None
            return False






    def wlaczanie_darkorbit(self):
        pyautogui.press('win')
        sleep(0.5)
        pyautogui.write('darkorbit')
        sleep(0.5)
        pyautogui.press('enter')

    def wylaczanie_darkorbit(self):
        pyautogui.hotkey('alt', 'f4')
        # aktualny czas
        now = datetime.now()
        aktualny_czas = now.strftime("%H:%M:%S")
        with open("Raport.txt", "a") as text_file:
            text_file.writelines(f"-[{aktualny_czas}]- " + "Zamknieto gre!!! "+ '\n')

    def login(self, login):
        sleep(1)
        pyautogui.write(f"{login}")
        sleep(0.5)
        pyautogui.press('tab')
        sleep(0.5)
        # pyautogui.write(f"{haslo}")
        # sleep(0.5)
        pyautogui.press('enter')
        sleep(1)

    # def poruszaj(self):

    def wykryj(self, numer_celu, threshold=0.8):

        ############# zrzut ekranu poczatek

        self.hwnd = win32gui.GetDesktopWindow()

        window_rect = win32gui.GetWindowRect(self.hwnd)
        self.w = window_rect[2] - window_rect[0]
        self.h = window_rect[3] - window_rect[1]

        border_pixels = 0
        titlebar_pixels = 0
        self.w = self.w - (border_pixels * 2)
        self.h = self.h - titlebar_pixels - border_pixels

        self.cropped_x = border_pixels
        self.cropped_y = titlebar_pixels

        self.offset_x = window_rect[0] + self.cropped_x
        self.offset_y = window_rect[1] + self.cropped_y

        #

        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (self.cropped_x, self.cropped_y), win32con.SRCCOPY)

        # dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')

        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.h, self.w, 4)

        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        img = img[..., :3]

        self.analizowany_zrzut_ekranu = np.ascontiguousarray(img)

        # run the OpenCV algorithm
        szukany_obrazek = cv.imread('img/' + self.nazwa_celu[numer_celu].rstrip('\n'),
                                    cv.IMREAD_UNCHANGED)  # dodanie rstrip('\n') usuwa znak następnej linii i dzieki temu dziala
        result = cv.matchTemplate(self.analizowany_zrzut_ekranu, szukany_obrazek, cv.TM_CCOEFF_NORMED)

        # Get the all the positions from the match result that exceed our threshold
        szukany_obrazek_w = szukany_obrazek.shape[1]
        szukany_obrazek_h = szukany_obrazek.shape[0]

        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))
        # print(locations)

        # You'll notice a lot of overlapping rectangles get drawn. We can eliminate those redundant
        # locations by using groupRectangles().
        # First we need to create the list of [x, y, w, h] rectangles
        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), szukany_obrazek_w, szukany_obrazek_h]
            # Add every box to the list twice in order to retain single (non-overlapping) boxes
            rectangles.append(rect)
            rectangles.append(rect)
        # Apply group rectangles.
        # The groupThreshold parameter should usually be 1. If you put it at 0 then no grouping is
        # done. If you put it at 2 then an object needs at least 3 overlapping rectangles to appear
        # in the result. I've set eps to 0.5, which is:
        # "Relative difference between sides of the rectangles to merge them into a group."
        rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)
        # print(rectangles)

        points = []

        # Loop over all the rectangles
        for (x, y, w, h) in rectangles:
            # Determine the center position
            center_x = x + int(w / 2)
            center_y = y + int(h / 2)
            # Save the points
            self.screen_x = center_x + self.window_offset[0]
            self.screen_y = center_y + self.window_offset[1]

        if self.screen_x and self.screen_y:
            print("znaleziono obiekt i zwrocono prawde")
            self.screen_x = None
            self.screen_y = None
            return True
        else:
            print(" nie znaleziono obiektu i zwrocono falsz")
            self.screen_x = None
            self.screen_y = None
            return False

