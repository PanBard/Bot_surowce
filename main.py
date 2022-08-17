from zapisywator_zdjec import Lista_zdjec
from time import time, sleep
from zarzadzanie import Kierownik

# #robimy plik txt i robimy liste zdjec
# zdjecia = Lista_zdjec()
# zdjecia.tworz_liste()
# print("lista zrobiona")

kierownik = Kierownik()



kierownik.rozpocznij_sekwencje_zarabiania("KONSOLETA", rodzaj_surek="promerium",ilosc_surek=3000)
kierownik.rozpocznij_sekwencje_zarabiania("SpokDre", rodzaj_surek="dur_i_prom", ilosc_surek=1500)
kierownik.rozpocznij_sekwencje_zarabiania("RyszardLipton", rodzaj_surek="dur_i_prom", ilosc_surek=1500)
kierownik.rozpocznij_sekwencje_zarabiania("DoktorKostek", rodzaj_surek="dur_i_prom", ilosc_surek=1500)
kierownik.rozpocznij_sekwencje_zarabiania("Smiesznystworek", rodzaj_surek="dur_i_prom", ilosc_surek=1500)
kierownik.rozpocznij_sekwencje_zarabiania("kuciaki", rodzaj_surek="dur_i_prom", ilosc_surek=1500)
kierownik.rozpocznij_sekwencje_zarabiania("miedzygalaktyczny", rodzaj_surek="dur_i_prom", ilosc_surek=1500)







# while True:
#     kierownik.rozpocznij_sekwencje_zarabiania("KONSOLETA", rodzaj_surek="promerium",ilosc_surek=3000)
#     kierownik.rozpocznij_sekwencje_zarabiania("SpokDre", rodzaj_surek="dur_i_prom", ilosc_surek=1500)
#     sleep(22000)









