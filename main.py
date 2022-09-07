from zapisywator_zdjec import Lista_zdjec
from time import time, sleep
from zarzadzanie import Kierownik

# #robimy plik txt i robimy liste zdjec
# zdjecia = Lista_zdjec()
# # zdjecia.tworz_liste_do_handlu_surkami()
# zdjecia.tworz_liste_do_ulepszenia_skylabu()
# print("lista zrobiona")


kierownik = Kierownik()

# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("SpokDre") # goliat+ ladownia             #2
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("RyszardLipton")# goliat+ ladownia          #3
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("DoktorKostek")# goliat+ ladownia          #4
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("Smiesznystworek")# goliat+ ladownia          #5
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("kuciaki")# goliat+ ladownia          #6
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("miedzygalaktyczny")# goliat+ ladownia           #7
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("KapitanstatkU") #goliat + ladownia           #8
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("zultePudelko12") #goliat + ladownia           #9
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("bajkiDisneja")#goliat           #10
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("SZkocik") #goliat           #11
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("takEJ") # goliat+ ladownia           #12
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("dyskotekowapl") # goliat + ladownia           #13
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("diskopol") # goliath + ladownia           #14
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("napakerze") # goliat + ladownia           #15
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("margarettaczer") # goliat+ ladownia           #16
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("czadowich")# goliat+ ladownia           #17
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("morzadno")# goliat+ ladownia           #18
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("aktotoprzyszedl")# goliath+ ladownia           #19
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("enterprajsxd") # goliath+ ladownia           #20
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("gieniabagie") #goliat+ ladownia           #21








################### PETLA ZARABIANIA - POCZATEK #######################
kierownik.spij_odliczone_sekundy()
kierownik.wybudzanie()

while True:
    kierownik.rozpocznij_sekwencje_zarabiania("KONSOLETA", rodzaj_surek="promerium", ilosc_surek=3000)
    czas_rozpoczecia = kierownik.daj_aktualna_godzine() #zapisanie godziny do wpisania w sprawozdanie
    kierownik.zapisanie_godziny_wybudzenia() #zapisanie godziny po zakonczeniu przez pierwsze konto
    kierownik.rozpocznij_sekwencje_zarabiania("SpokDre",rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("RyszardLipton", rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("DoktorKostek", rodzaj_surek="promerium", ilosc_surek=3000)#
    kierownik.rozpocznij_sekwencje_zarabiania("Smiesznystworek", rodzaj_surek="promerium", ilosc_surek=3000)#
    kierownik.rozpocznij_sekwencje_zarabiania("kuciaki",rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("miedzygalaktyczny", rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("KapitanstatkU", rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("zultePudelko12",rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("bajkiDisneja", rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("SZkocik",rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("takEJ", rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("dyskotekowapl", rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("diskopol", rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("napakerze",rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("margarettaczer",rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("czadowich", rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("morzadno",rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("aktotoprzyszedl",rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("enterprajsxd", rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("gieniabagie",rodzaj_surek="promerium", ilosc_surek=3000)


    # kierownik.rozpocznij_sekwencje_zarabiania("gieniabagie", rodzaj_surek="dur_i_prom", ilosc_surek=1500)
    # kierownik.rozpocznij_sekwencje_zarabiania("gieniabagie", rodzaj_surek="dur_i_prd_i_promerium", ilosc_surek=1000)


    kierownik.zapisz_sprawozdanie_czasowe(czas_rozpoczecia)
    kierownik.spij_odliczone_sekundy()
    kierownik.wybudzanie()

################### PETLA ZARABIANIA - KONIEC #######################















# ###### wyplata###############
#
#
# kierownik.wyplac_hajsownikom(ilosc_statkow=4, numer_statku=18, ilosc_kredytow=300000)
# ########## koniec wyplaty ###############

