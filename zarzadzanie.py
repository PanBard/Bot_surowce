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
    stan_ulepszania_skylabu = []
    nazwy_ulepszanych_modulow =[]

    czas_poczatku_sekwencji =None

    robocza_wspolrzedna_x = None
    robocza_wspolrzedna_y = None



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
        self.czekaj(3,3,3)#czekaj az pojawi sie przycisk handlu surkami
        self.sprzedaz_surek()
        self.wysylanie_surek(rodzaj_surek, ilosc_surek)
        self.wylonczanie_darkorbit()
        self.wpis_do_raportu(f"Zakonczono sekwencje - {login}")
        self.wypisz_do_raportu_godzine_przeznaczenia(login)
        self.napisz_sprawozdanie(login, rodzaj_surek, ilosc_surek)

    def rozpocznij_sekwencje_ulepszania_skylabu_itp(self, login):
        self.login = login

        self.wpis_do_raportu(f"Rozpoczeto sekwencje ulepszania skylabu dla - {login}")
        self.wlonczanie_darkorbit()
        self.czekaj(2,16,5) #czekaj az pojawi sie przycisk logowania lub do zatwierdzenia prywatnosci lub ikona minimapy
        self.prewencja_przed_wyskakujacymi_oknami("zgoda_prywatnosci")
        self.logowanie(login)
        self.czekaj(18,15,5) #czekaj az pojawi sie przycisk zamkniecia okna lub startu lub ikona minimapy
        self.prewencja_przed_wyskakujacymi_oknami("zamykanie_okna")
        self.sprawdzanie_skylabu_czy_skonczony_proces()

        # self.ulepszenie_rafinerii_kolektora(login,20) #wlonczanie pierwszy raz prometidu
        # self.ulepszenie_rafinerii_kolektora(login,18) #wlonczanie pierwszy raz duranium
        # self.ulepszenie_rafinerii_kolektora(login, 11)  # wlonczanie pierwszy raz promerium
        # self.ulepszenie_rafinerii_kolektora(login, 10)  # wlonczanie pierwszy raz xeno

        # self.wlaczenie_rafinerii_kolektora(login,30) # wznowienieraf promerium
        # self.wlaczenie_rafinerii_kolektora(login,31) # wznowienieraf prometidu
        # self.wlaczenie_rafinerii_kolektora(login,32) # wznowienieraf duranium

        # self.wylaczenie_rafinerii_kolektora(login,26) #wylonczanie promerium
        # self.wylaczenie_rafinerii_kolektora(login,19) #wylonczanie prometidu
        # self.wylaczenie_rafinerii_kolektora(login, 17)  # wylonczanie duranium


        self.ulepszenie_rafinerii_kolektora(login, 3)  # kolektor terbium
        self.ulepszenie_rafinerii_kolektora(login, 1)  # kolektor endurium
        self.ulepszenie_rafinerii_kolektora(login, 2)  # kolektor prometrium
        #

        #
        self.ulepszenie_rafinerii_kolektora(login,19) #rafineria prometidu
        self.ulepszenie_rafinerii_kolektora(login,17) #rafineria duranium
        self.ulepszenie_rafinerii_kolektora(login, 26)  # rafineria promerium
        self.ulepszenie_rafinerii_kolektora(login, 27)  # modul xeno

        self.ulepszenie_rafinerii_kolektora(login,5) #modul podstawowy
        self.ulepszenie_rafinerii_kolektora(login,6) #modul sloneczny
        self.ulepszenie_rafinerii_kolektora(login, 4)  # modul magazynowy

        self.zapisz_skrina_o_stanie_skylabu(login)
        self.wylonczanie_darkorbit()
        self.napisz_sprawozdanie_skylabu(login)
        self.wpis_do_raportu(f"Zakonczono sekwencje ulepszania skylabu dla - {login}")




    # def sekwencja_pierwszego_logowania(self, login, haslo):
    #     self.login = login
    #     self.wlonczanie_darkorbit()
    #     self.czekaj(2, 16,5)  # czekaj az pojawi sie przycisk logowania lub do zatwierdzenia prywatnosci lub ikona minimapy
    #     self.prewencja_przed_wyskakujacymi_oknami("zgoda_prywatnosci")
    #     self.logowanie_pierwszy_raz(login, haslo)
    #     self.czekaj(18, 15, 18)  # czekaj az pojawi sie przycisk zamkniecia okna lub startu lub ikona minimapy
    #     self.prewencja_przed_wyskakujacymi_oknami("zamykanie_okna")
    # dorobic wchodzenie do skylabu (zeby juz se surki robily)
    #     self.wlonczanie_gry_do_mapy()
    #     self.czekaj(5, 5, 5)  # czekaj az pojawi sie przycisk minimapy
    #     self.prewencja_przed_wyskakujacymi_oknami("zamykanie_okna")
    #     self.klik_w_ok()
    #     self.robienie_porzadkow_z_ustawieniami()

    def wlonczanie_darkorbit(self):
        self.bocik.wlaczanie_darkorbit()

    def czekaj(self, na_obiekt1, na_obiekt2, na_obiekt3):
        czas = time()
        self.wpis_do_raportu("Rozpoczeto procedure czekania")
        while True:
            if self.bocik.wykryj(na_obiekt1) or self.bocik.wykryj(na_obiekt2) or self.bocik.wykryj(na_obiekt3):
                czas2 = time() - czas
                self.wpis_do_raportu(f"Zakonczono czekanie po {czas2} sekundach.")
                break
            else: sleep(0.5)

            if time()-czas >= 120:
                self.wpis_do_raportu("Przerwano procedure czekania bo nie znaleziono obiektu (uplynol czas czekania:  2 minuty)")
                break
        sleep(2)



    def logowanie(self, login):
        sleep(1)
        self.bocik.wykryj_i_kliknij(0)
        sleep(1)
        self.bocik.login(login)

    def logowanie_pierwszy_raz(self, login, haslo):
        sleep(1)
        self.bocik.wykryj_i_kliknij(0)
        sleep(1)
        self.bocik.login_pierwszy_raz(login,haslo)

    def klik_w_ok(self):
        self.bocik.wykryj_i_kliknij_skylabu(22)


    def ulepszenie_rafinerii_kolektora(self,login, nr_kolektora):
        self.bocik.wykryj_i_kliknij_skylabu(nr_kolektora) # klikamy na wybrana rafinerie/kolektor
        sleep(1)
        self.bocik.wykryj_i_kliknij_skylabu(9) # klikamy na przycisk ulepszenie
        sleep(1)
        self.bocik.wykryj_i_kliknij_skylabu(7)  # klikamy na przycisk buduj
        self.czekaj(11,11,15)# czeka na przycisk ok lub przycisk startu
        sleep(2)
        if self.bocik.wykryj_i_kliknij_skylabu(8):  # odczytujemy potwierdzenie o modernizacji
            self.wpis_do_raportu(f"Modul {self.bocik.daj_nazwe_obiektu(nr_kolektora)} zostal ulepszony dla {login} ------ ####################")
            self.stan_ulepszania_skylabu.append(1)
            self.nazwy_ulepszanych_modulow.append(self.bocik.daj_nazwe_obiektu(nr_kolektora))
        else:
            self.wpis_do_raportu(f"### dla {login} nie ulepszono: {self.bocik.daj_nazwe_obiektu(nr_kolektora)} ###")
            self.stan_ulepszania_skylabu.append(0)
            self.nazwy_ulepszanych_modulow.append(self.bocik.daj_nazwe_obiektu(nr_kolektora))
        sleep(1)
        if self.klik_w_ok():
            pass
        else: self.bocik.wykryj_i_kliknij(19)

        sleep(2)

    def wylaczenie_rafinerii_kolektora(self, login, nr_kolektora):
        self.bocik.wykryj_i_kliknij_skylabu(nr_kolektora)  # klikamy na wybrana rafinerie/kolektor
        sleep(1)
        self.bocik.wykryj_i_kliknij_skylabu(12)  # klikamy na przycisk wylaczania
        self.czekaj(11,11,11)
        if self.bocik.wykryj_i_kliknij_skylabu(25):  # odczytujemy potwierdzenie o wylaczeniu
            self.wpis_do_raportu(f"Modul {self.bocik.daj_nazwe_obiektu(nr_kolektora)} zostal WYLACZONY (OFF) dla {login} ------ ####################")
            self.stan_ulepszania_skylabu.append(1)
            self.nazwy_ulepszanych_modulow.append(self.bocik.daj_nazwe_obiektu(nr_kolektora))
        else:
            self.wpis_do_raportu(f"### dla {login} nie wylaczono: {self.bocik.daj_nazwe_obiektu(nr_kolektora)} ###")
            self.stan_ulepszania_skylabu.append(0)
            self.nazwy_ulepszanych_modulow.append(self.bocik.daj_nazwe_obiektu(nr_kolektora))
        sleep(1)
        if self.klik_w_ok():
            pass
        else: self.bocik.wykryj_i_kliknij(19)

        sleep(2)

    def wlaczenie_rafinerii_kolektora(self, login, nr_kolektora):
        self.bocik.wykryj_i_kliknij_skylabu(nr_kolektora)  # klikamy na wybrana rafinerie/kolektor
        sleep(1)
        self.bocik.wykryj_i_kliknij_skylabu(28)  # klikamy na przycisk wlaczania
        self.czekaj(11,11,11)
        if self.bocik.wykryj_i_kliknij_skylabu(29):  # odczytujemy potwierdzenie o wlaczeniu
            self.wpis_do_raportu(f"Modul {self.bocik.daj_nazwe_obiektu(nr_kolektora)} zostal WlACZONY (ON) dla {login} ------ ####################")
            self.stan_ulepszania_skylabu.append(1)
            self.nazwy_ulepszanych_modulow.append(self.bocik.daj_nazwe_obiektu(nr_kolektora))
        else:
            self.wpis_do_raportu(f"### dla {login} nie wlaczono: {self.bocik.daj_nazwe_obiektu(nr_kolektora)} ###")
            self.stan_ulepszania_skylabu.append(0)
            self.nazwy_ulepszanych_modulow.append(self.bocik.daj_nazwe_obiektu(nr_kolektora))
        sleep(1)
        if self.klik_w_ok():
            pass
        else: self.bocik.wykryj_i_kliknij(19)

        sleep(2)

    def robienie_porzadkow_z_ustawieniami(self):
        self.bocik.wykryj_i_kliknij_skylabu(15) #ikona ustawien
        sleep(3)
        self.bocik.WLACZ_USTAWIANIE_USTAWIEN = True
        self.bocik.wykryj_i_kliknij_skylabu(16)
        self.bocik.WLACZ_USTAWIANIE_USTAWIEN = False
        print("koniec")

    def napisz_sprawozdanie_skylabu(self, login):
        now = datetime.now()
        aktualny_czas = now.strftime("%H:%M:%S")
        five_hour = timedelta(hours=6)
        new = now + five_hour
        with open("Sprawozdanie.txt", "a") as text_file:
            text_file.writelines(f"[{aktualny_czas}]- " + f"Sprawozdanie dla statku {login} z ulepszania skylabu: " + '\n' )

        for x in range(len(self.stan_ulepszania_skylabu)):
            if self.stan_ulepszania_skylabu[x] == 1:
                with open("Sprawozdanie.txt", "a") as text_file:
                    text_file.writelines(f"Zostal ulepszony: {self.nazwy_ulepszanych_modulow[x]}  " + '\n')
            else:
                with open("Sprawozdanie.txt", "a") as text_file:
                    text_file.writelines(f"###Nie zostal ulepszony: {self.nazwy_ulepszanych_modulow[x]}  ####" + '\n')

        with open("Sprawozdanie.txt", "a") as text_file:
            text_file.writelines( '\n'+ '\n')
        self.stan_ulepszania_skylabu.clear()
        self.nazwy_ulepszanych_modulow.clear()



    def zapisz_skrina_o_stanie_skylabu(self,login):
        sleep(2)
        self.bocik.zrob_skrina_skylab(login)


    def prewencja_przed_wyskakujacymi_oknami(self, tryb):
        if tryb == "zamykanie_okna":
            while True:
                sleep(1)
                if self.bocik.wykryj_i_kliknij(18) or self.bocik.wykryj_i_kliknij(19):
                    sleep(1)
                else: break


        if tryb == "zgoda_prywatnosci":
            while True:
                sleep(1)
                if self.bocik.wykryj_i_kliknij(16):
                    sleep(1)
                else: break

    def sprawdzanie_skylabu_czy_skonczony_proces(self):
        sleep(1)
        self.bocik.wykryj_i_kliknij(13)  # otwieranie skylabu
        sleep(5)
        self.bocik.wykryj_i_kliknij_skylabu(22)
        sleep(3)

    def odebranie_surek(self):
        sleep(2)
        self.bocik.wykryj_i_kliknij(13)  # otwieranie skylabu
        sleep(5)
        if self.bocik.wykryj_i_kliknij(12) : # sprawdzenie czy transfer sie zakonczyl
            sleep(5)
        else: self.bocik.wykryj_i_kliknij(11) # klika na przycisk ok


    def wlonczanie_gry_do_mapy(self):
        sleep(1)
        self.bocik.wykryj_i_kliknij(15)  # start mapy gry
        self.czekaj(15,10,5) #czekaj az pojawi sie przycisk startu lub odbioru lub napis minimapy
        if self.bocik.wykryj_i_kliknij(15):  # klik na ikone start mapy gry
            pass
        else: self.bocik.wykryj_i_kliknij(10)  # klik na ikone odbierz
        self.czekaj(5,5,5)#czekaj az pojawi sie napis minimapy
        sleep(1)

    def autopozycjonowanie_do_bazy_handlu_surkami(self):
        sleep(1)
        self.bocik.WLACZ_POZYCJONOWANIE_MAPY = True
        self.bocik.wykryj_i_kliknij(5)  # pozycjonowanie mapy i ruszanie statkiem do bazy
        self.bocik.WLACZ_POZYCJONOWANIE_MAPY = False


    def sprzedaz_surek(self):
        self.bocik.wykryj_i_kliknij(3)  # wlaczamy handel surkami

        self.czekaj(6,6,6)
        self.bocik.WLACZ_HANDEL = True  # rozpoczynamy sekwencje handlowa
        self.bocik.wykryj_i_kliknij(6)  # zdjecie odniesienia
        self.bocik.WLACZ_HANDEL = False  # koniec sekwencje handlowaj
        sleep(1)



    def wysylanie_surek(self, rodzaj_surek, ilosc_surek):
        sleep(1)
        self.bocik.wykryj_i_kliknij(7)  # przechodzimy z powrotem do zakladki obok
        sleep(15)
        # self.bocik.wykryj_i_kliknij(13)  # otwieranie skylabu


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

        if rodzaj_surek == "terb_end_prom":
            sleep(2)
            ilosc_surek_str = str(ilosc_surek)
            self.bocik.ilosc_PROMERIUM = ilosc_surek_str
            self.bocik.WYSYLANIE_SUREK_TERB_END_PROM = True  # sekwencja wpisywania i wysylania surek
            self.bocik.wykryj_i_kliknij(8)  # otwieranie modulu transportowego
            self.bocik.WYSYLANIE_SUREK_TERB_END_PROM = False
            sleep(2)

        if rodzaj_surek == "dur_i_prd_i_promerium":
            sleep(2)
            ilosc_surek_str = str(ilosc_surek)
            self.bocik.ilosc_duranium = ilosc_surek_str
            self.bocik.ilosc_prometid = ilosc_surek_str
            self.bocik.ilosc_PROMERIUM = ilosc_surek_str
            self.bocik.WYSYLANIE_SUREK_DUR_i_PRD_i_PROMERIUM = True  # sekwencja wpisywania i wysylania surek
            self.bocik.wykryj_i_kliknij(8)  # otwieranie modulu transportowego
            self.bocik.WYSYLANIE_SUREK_DUR_i_PRD_i_PROMERIUM = False

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
            if self.ilosc_surek == 1500 or self.ilosc_surek == 3000 or self.ilosc_surek==1000:
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

            if self.ilosc_surek ==750  or self.ilosc_surek==500 :
                now = datetime.now()
                aktualny_czas = now.strftime("%H:%M:%S")
                five_hour = timedelta(hours=3)
                new = now + five_hour
                nowy_czas = new.strftime("%H:%M:%S")
                ilosc_surek = str(ilosc_surek)
                with open("Sprawozdanie.txt", "a") as text_file:
                    text_file.writelines(
                        f"[{aktualny_czas}]- " + f"Misja dla statku {login} zakonczona POWODZENIEM" + '\n' + "Godzina wyznaczona dla nastepnej misji: ---" + f"{nowy_czas}" + '\n' + "Ladunek: :" + f"{rodzaj_surek} w ilosci: " + f"{ilosc_surek} jednostek" + '\n' + '\n' + '\n')
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



    def wpis_do_sprawozdania_informacji_o_godzinie_wybudzenia(self, sekundy,czas_konca_sekwencji,roznica_sekundach):
        now = datetime.now()
        aktualny_czas = now.strftime("%H:%M:%S")

        czas_rozpoczecia = self.czas_poczatku_sekwencji.strftime("%H:%M:%S")
        czas_konca_sekwencjii = czas_konca_sekwencji.strftime("%H:%M:%S")

        six_hour = timedelta(hours=6)
        czas_za_6_godzin = self.czas_poczatku_sekwencji + six_hour

        roznica_w_minutach = roznica_sekundach / 60
        reszta_w_sekundach = roznica_sekundach % 60
        with open("Sprawozdanie.txt", "a") as text_file:
            text_file.writelines(
                f"[{aktualny_czas}]- " +'\n'+f"Czas rozpoczecia sekwencji zarabiania: {czas_rozpoczecia}s"+'\n'+f"Czas zakonczenia sekwencji zarabiania: {czas_konca_sekwencjii}s"+'\n'+ f"Roznica wynosi: {int(roznica_w_minutach)}min {int(reszta_w_sekundach)}s" +'\n' +f"~~~~~~~~~~~~~~Okres uspienia zakonczy sie po: {sekundy} sekundach, czyli o godzinie: {czas_za_6_godzin}~~~~~~" + '\n' + '\n')

    def daj_aktualna_godzine(self):
        self.czas_poczatku_sekwencji = datetime.now()
        aktualny_czas = time()

        return  aktualny_czas

    def daj_liczbe_sekund_do_spania(self, czas_rozpoczecia):
        aktualny_czas = time()
        czas_konca_sekwencji = datetime.now()
        roznica = aktualny_czas - czas_rozpoczecia
        szesc_godzin = 6*3600
        godzina_wybudzenia = czas_rozpoczecia +szesc_godzin
        czas_przerwy = szesc_godzin - roznica
        czas_przerwy = czas_przerwy + 60
        self.wpis_do_sprawozdania_informacji_o_godzinie_wybudzenia(czas_przerwy,czas_konca_sekwencji,roznica)
        return czas_przerwy

    def zapisanie_godziny_wybudzenia(self):
        czas = time()
        czas_z_6_godzinami = czas + (3600*6)

        now = datetime.now()
        six_hour = timedelta(hours=6)
        czas_za_6_godzin = now + six_hour
        czas_za_6_godzin = czas_za_6_godzin.strftime("%H:%M:%S")

        with open("godzina_wybudzenia.txt", "w") as text_file:
            text_file.writelines(f"{czas_z_6_godzinami}" +'\n' + f"{czas_za_6_godzin}")

    def spij_odliczone_sekundy(self):
        plik_txt = open('godzina_wybudzenia.txt')
        godzina_przeznaczenia = plik_txt.readlines()
        plik_txt.close()

        godzina_konca_spania = godzina_przeznaczenia[1]
        godzina_przeznaczenia = float(godzina_przeznaczenia[0].rstrip('\n'))
        terazniejsza_godzina = time()
        sekundy_pozostale_do_spania = godzina_przeznaczenia - terazniejsza_godzina
        self.wpis_do_raportu(f"~~~~~~~~~~~~~~~~~~Wybudzenie po: {sekundy_pozostale_do_spania}s")
        now = datetime.now()
        aktualny_czas = now.strftime("%H:%M:%S")



        print( f"Rozpoczecie czekania o godzinie: {aktualny_czas}" +'\n'+ f"Zakonczenie czekania o godzinie: {godzina_konca_spania} "+'\n'+ f"Czas pozostaly do spania: {sekundy_pozostale_do_spania/3600} godz.")


        if sekundy_pozostale_do_spania > 0:
            sleep(sekundy_pozostale_do_spania)
        else: print("JAZDA BO JUZ CZAS!!!!!!!!!!!!!")

        print(f"spie se: {sekundy_pozostale_do_spania} sekund")
    def wylonczanie_darkorbit(self):
        sleep(2)
        self.bocik.wylaczanie_darkorbit()

    def spij_do_nadejscia_czasu_przeznaczenia(self, liczba_godzin):
        sekundy = liczba_godzin * 3610
        sleep(sekundy)
        print("spanko skonczone")

    def wybudzanie(self):
        self.bocik.wybudz()

    def czas(self,czas):
        now = datetime.now()
        print(now)
        czas = czas.strftime("%H:%M:%S")
        aktualny_czas = now.strftime("%H:%M:%S")
        print(aktualny_czas)
        five_hour = timedelta(hours=6)
        new = czas + five_hour
        nowy_czas = new.strftime("%H:%M:%S")
        print(nowy_czas)

    def wyplac_hajs(self,liczba_statkow,numer_statku ,ilosc_kredytow):

        for x in range(liczba_statkow):
            x = x + numer_statku
            self.bocik.wyplata(x ,ilosc_kredytow)
            sleep(2)
            self.bocik.wykryj_i_kliknij_skylabu(23)
            sleep(2)


    def wyplac_hajsownikom(self,ilosc_statkow, numer_statku, ilosc_kredytow):
        for x in range(ilosc_statkow):
            x = x + numer_statku


            self.czekaj(15,13,15)
            if self.bocik.wykryj_i_kliknij_skylabu(24):
                self.prewencja_przed_wyskakujacymi_oknami("zamykanie_okna")
                self.robocza_wspolrzedna_x =  self.bocik.screen_x_hajs
                self.robocza_wspolrzedna_y = self.bocik.screen_y_hajs
                sleep(2)
                self.bocik.wykryj_i_kliknij_skylabu(23)
                sleep(1)
                self.bocik.wyplata2(self.robocza_wspolrzedna_x, self.robocza_wspolrzedna_y,x, ilosc_kredytow)
                sleep(2)
                self.bocik.wykryj_i_kliknij_skylabu(23)
            else: print("ni ma wyplaty")