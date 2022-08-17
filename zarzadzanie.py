from robotnik import Robotnik
import pyautogui
from zapisywator_zdjec import Lista_zdjec
from time import time, sleep
from datetime import datetime, timedelta

class Kierownik():
    bocik = Robotnik()
    login = None
    stan_misji = None
    ilosc_surek = None

    def rozpocznij_sekwencje_zarabiania(self, login, rodzaj_surek, ilosc_surek):
        self.login = login
        self.ilosc_surek = ilosc_surek

        self.wpis_do_raportu(f"Rozpoczeto sekwencje - {login}")
        self.wlonczanie_darkorbit()
        self.czekaj(2,16,5) #czekaj az pojawi sie przycisk logowania lub do zatwierdzenia prywatnosci lub ikona minimapy
        self.prewencja_przed_wyskakujacymi_oknami("zgoda_prywatnosci")
        self.logowanie(login)
        self.czekaj(18,15,5) #czekaj az pojawi sie przycisk zamkniecia okna lub startu lub ikona minimapy
        self.prewencja_przed_wyskakujacymi_oknami("zamykanie_okna")
        self.odebranie_surek()
        self.wlonczanie_gry_do_mapy()
        self.prewencja_przed_wyskakujacymi_oknami("zamykanie_okna")
        self.autopozycjonowanie_do_bazy_handlu_surkami()
        self.sprzedaz_surek()
        self.wysylanie_surek(rodzaj_surek, ilosc_surek)
        self.wylonczanie_darkorbit()
        self.wpis_do_raportu(f"Zakonczono sekwencje - {login}")
        self.wypisz_do_raportu_godzine_przeznaczenia(login)
        self.napisz_sprawozdanie(login, rodzaj_surek, ilosc_surek)








    def wlonczanie_darkorbit(self):
        self.bocik.wlaczanie_darkorbit()

    def czekaj(self, na_obiekt1, na_obiekt2, na_obiekt3):
        czas = time()
        while True:
            if self.bocik.wykryj(na_obiekt1) or self.bocik.wykryj(na_obiekt2) or self.bocik.wykryj(na_obiekt3):
                czas2 = time() - czas
                self.wpis_do_raportu(f"Zakonczono czekanie po {czas2} sekundach.")
                break
            else: sleep(2)

            if time()-czas >= 120:
                self.wpis_do_raportu("Przerwano procedure czekania bo nie znaleziono obiektu")
                break
        sleep(2)



    def logowanie(self, login):
        sleep(1)
        self.bocik.wykryj_i_kliknij(0)
        sleep(1)
        self.bocik.login(login)



    def prewencja_przed_wyskakujacymi_oknami(self, tryb):
        if tryb == "zamykanie_okna":
            while True:
                sleep(2)
                if self.bocik.wykryj_i_kliknij(18):
                    sleep(1)
                else: break


        if tryb == "zgoda_prywatnosci":
            while True:
                sleep(2)
                if self.bocik.wykryj_i_kliknij(16):
                    sleep(1)
                else: break


    def odebranie_surek(self):
        sleep(2)
        self.bocik.wykryj_i_kliknij(13)  # otwieranie skylabu
        sleep(5)
        self.bocik.wykryj_i_kliknij(12)  # sprawdzenie czy transfer sie zakonczyl
        sleep(5)

    def wlonczanie_gry_do_mapy(self):
        sleep(3)
        self.bocik.wykryj_i_kliknij(15)  # start mapy gry
        self.czekaj(15,10,5) #czekaj az pojawi sie przycisk startu lub odbioru
        self.bocik.wykryj_i_kliknij(15)  # klik na ikone start mapy gry
        self.bocik.wykryj_i_kliknij(10)  # klik na ikone odbierz
        self.czekaj(5,5,5)#czekaj az pojawi sie przycisk minimapy lub handlu surkami
        sleep(3)

    def autopozycjonowanie_do_bazy_handlu_surkami(self):
        sleep(2)
        self.bocik.WLACZ_POZYCJONOWANIE_MAPY = True
        self.bocik.wykryj_i_kliknij(5)  # pozycjonowanie mapy i ruszanie statkiem do bazy
        self.bocik.WLACZ_POZYCJONOWANIE_MAPY = False
        sleep(2)

    def sprzedaz_surek(self):
        self.bocik.wykryj_i_kliknij(3)  # wlaczamy handel surkami

        sleep(3)
        self.bocik.WLACZ_HANDEL = True  # rozpoczynamy sekwencje handlowa
        self.bocik.wykryj_i_kliknij(6)  # zdjecie odniesienia
        self.bocik.WLACZ_HANDEL = False  # koniec sekwencje handlowaj
        sleep(3)



    def wysylanie_surek(self, rodzaj_surek, ilosc_surek):
        sleep(1)
        self.bocik.wykryj_i_kliknij(7)  # przechodzimy z powrotem do zakladki obok
        sleep(10)
        self.bocik.wykryj_i_kliknij(13)  # otwieranie skylabu
        sleep(3)

        if rodzaj_surek == "promerium":
            sleep(2)
            ilosc_surek_str = str(ilosc_surek)
            self.bocik.ilosc_PROMERIUM = ilosc_surek_str
            self.bocik.WYSYLANIE_SUREK_PROMERIUM = True  # sekwencja wpisywania i wysylania surek
            self.bocik.wykryj_i_kliknij(8)  # otwieranie modulu transportowego
            self.bocik.WYSYLANIE_SUREK_PROMERIUM = False
            sleep(2)

        if rodzaj_surek == "dur_i_prom":
            sleep(2)
            ilosc_surek_str = str(ilosc_surek)
            self.bocik.ilosc_duranium = ilosc_surek_str
            self.bocik.ilosc_prometid = ilosc_surek_str
            self.bocik.WYSYLANIE_SUREK_DUR_i_PROMETID = True  # sekwencja wpisywania i wysylania surek
            self.bocik.wykryj_i_kliknij(8)  # otwieranie modulu transportowego
            self.bocik.WYSYLANIE_SUREK_DUR_i_PROMETID = False
            sleep(2)

        self.bocik.wykryj_i_kliknij(17)  # klik na przycisk wysylania surek
        sleep(5)
        self.prewencja_przed_wyskakujacymi_oknami("zamykanie_okna")
        if self.bocik.wykryj_i_kliknij(9):  # odczytujemy potwierdzenie o wysylanych surkach
            self.wpis_do_raportu(f"################# ----- SUROWCE ZOSTALY WYSLANE dla {self.login} ------ ####################")
            self.stan_misji = True
        else:
            self.wpis_do_raportu(f"### niestety ale wyslanie surek dla {self.login} zkonczylo sie niepowodzeniem ###")
            self.stan_misji = False
        sleep(3)

    def wpis_do_raportu(self, tekst):
        now = datetime.now()
        aktualny_czas = now.strftime("%H:%M:%S")
        with open("Raport.txt", "a") as text_file:
            text_file.writelines(f"-[{aktualny_czas}]- " + f"{tekst}" + '\n')

    def napisz_sprawozdanie(self, login, rodzaj_surek, ilosc_surek):
        if self.stan_misji == True:
            if self.ilosc_surek == 1500 or self.ilosc_surek == 3000:
                now = datetime.now()
                aktualny_czas = now.strftime("%H:%M:%S")
                five_hour = timedelta(hours=6)
                new = now + five_hour
                nowy_czas = new.strftime("%H:%M:%S")
                ilosc_surek = str(ilosc_surek)
                with open("Sprawozdanie.txt", "a") as text_file:
                    text_file.writelines(f"[{aktualny_czas}]- " + f"Misja dla statku {login} zakonczona POWODZENIEM" + '\n' + "Godzina wyznaczona dla nastepnej misji: ---"+ f"{nowy_czas}" + '\n' + "Ladunek: :" + f"{rodzaj_surek} w ilosci: " +f"{ilosc_surek} jednostek"  + '\n'  + '\n'  + '\n' )
                self.stan_misji = None
                self.ilosc_surek = None

            if self.ilosc_surek ==750  or self.ilosc_surek==200:
                now = datetime.now()
                aktualny_czas = now.strftime("%H:%M:%S")
                five_hour = timedelta(hours=3)
                new = now + five_hour
                nowy_czas = new.strftime("%H:%M:%S")
                ilosc_surek = str(ilosc_surek)
                with open("Sprawozdanie.txt", "a") as text_file:
                    text_file.writelines(
                        f"[{aktualny_czas}]- " + f"Misja dla statku {login} zakonczona POWODZENIEM" + '\n' + "Godzina wyznaczona dla nastepnej misji: ---" + f"{nowy_czas}" + '\n' + "Ladunek: :" + f"{rodzaj_surek} w ilosci :" + f"{ilosc_surek} jednostek" + '\n' + '\n' + '\n')
                self.stan_misji = None
                self.ilosc_surek = None

        if self.stan_misji == False:
            now = datetime.now()
            aktualny_czas = now.strftime("%H:%M:%S")
            five_hour = timedelta(hours=6)
            new = now + five_hour
            nowy_czas = new.strftime("%H:%M:%S")
            ilosc_surek = str(ilosc_surek)
            with open("Sprawozdanie.txt", "a") as text_file:
                text_file.writelines(
                    f"[{aktualny_czas}]- " + f"Misja dla statku {login} zakonczona NIEPOWODZENIEM !!!!!!!" + '\n'  + '\n'  + '\n')
            self.stan_misji = None
            self.ilosc_surek = None
    def wypisz_do_raportu_godzine_przeznaczenia(self, login):
        now = datetime.now()
        aktualny_czas = now.strftime("%H:%M:%S")
        five_hour = timedelta(hours=6)
        new = now + five_hour
        nowy_czas = new.strftime("%H:%M:%S")
        with open("Raport.txt", "a") as text_file:
            text_file.writelines(f"-[{aktualny_czas}]- " + f"Rozpoczecie nastepnej sekwencji dla {login} o godzinie: "+ f"##################### {nowy_czas} ###################" + '\n')

    def wylonczanie_darkorbit(self):
        sleep(2)
        self.bocik.wylaczanie_darkorbit()



