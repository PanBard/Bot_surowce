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



#
#
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("WielkiPtak45")                #-goliat i ladownia
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("GeneralojcjeC")                #-goliat i ladownia
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("SynKapitanna")                #-goliat i ladownia
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("BoBoKSPOK1")                #-goliat i ladownia
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("DanutaNieznam")                #-goliat i ladownia
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("wasatyLeczsz34")                #-goliat i ladownia
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("PanBurmistrz98")                #-goliat i ladownia
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("Antoniawracaj")                #-goliat i ladownia
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("policjaGwiezdna20")                #-goliat i ladownia
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("benaffleck45")                #-goliat i ladownia
#
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("sajmonpegg5")                #-goliat i ladownia
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("TADZIKenter")                #-goliat i ladownia
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("kociakiTAKEJA")                #-goliat i ladownia
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("trytoniKolhoz")                #-goliat i ladownia
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("kudlaczeNAtargu")                #-goliat i ladownia
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("fajerwerkiwkosm")                #-goliat i ladownia
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("planetaSWmikolaja")                #-goliat i ladownia
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("zjdFEDERACJApln")                #-goliat i ladownia
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("walkaZnuda")                #-goliat i ladownia
# kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("zamkniecieparasola")                #-goliat i ladownia
#
#
# kierownik.rozpocznij_sekwencje_zarabiania("SpokDre",rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("RyszardLipton", rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("DoktorKostek", rodzaj_surek="promerium", ilosc_surek=3000)#
# kierownik.rozpocznij_sekwencje_zarabiania("Smiesznystworek", rodzaj_surek="promerium", ilosc_surek=3000)#
# kierownik.rozpocznij_sekwencje_zarabiania("kuciaki",rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("miedzygalaktyczny", rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("KapitanstatkU", rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("zultePudelko12",rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("bajkiDisneja", rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("SZkocik",rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("takEJ", rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("dyskotekowapl", rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("diskopol", rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("napakerze",rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("margarettaczer",rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("czadowich", rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("morzadno",rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("aktotoprzyszedl",rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("enterprajsxd", rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("gieniabagie",rodzaj_surek="promerium", ilosc_surek=3000)
# #



# ############################## LICYTACJA - start #############################################
# kierownik.spij_odliczone_sekundy()
# kierownik.wybudzanie()
#
# lsta_kont = kierownik.utworz_liste(nazwa_pliku="loginy_do_licytacji.txt")
# for x in range(len(lsta_kont)):
#     konta = kierownik.utworz_liste(nazwa_pliku="loginy_do_licytacji.txt")
#     nr_konta = kierownik.utworz_liste(nazwa_pliku="kolejka_aukcji.txt")
#     nr_konta = str(nr_konta[0])
#     nr_konta = int(nr_konta)
#     print(f"numer konta {nr_konta}")
#     if nr_konta == x:
#         nr_konta =x
#     else: nr_konta = nr_konta + x
#
#     kierownik.sekwencja_licytacji(login=konta[nr_konta],nr_zdj_przedmiotu=36,ilosc_nacisniec_strzalki=7,ilosc_kredytow=40000)
#     print(f"Zakonczono licytacje dla konta {konta[nr_konta]}")
#     nr_konta = nr_konta + 1
#     kierownik.aukcja_trzymanie_numeru_konta(nr_konta)
#     print(f"Nastepna aukcja dla konta {konta[nr_konta]}")
#
#     czas_rozpoczecia = kierownik.daj_aktualna_godzine()  # zapisanie godziny do wpisania w sprawozdanie
#     kierownik.zapisanie_godziny_wybudzenia(uwzgledniana_ilosc_godzin=1.05) #zapisanie godziny po zakonczeniu przez pierwsze konto
#     kierownik.zapisz_sprawozdanie_czasowe(czas_rozpoczecia)
#     kierownik.spij_odliczone_sekundy()
#     kierownik.wybudzanie()
#
#
# ############################## LICYTACJA - end #############################################




# kierownik.rozpocznij_sekwencje_zarabiania("WielkiPtak45",rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("GeneralojcjeC",rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("SynKapitanna",rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("BoBoKSPOK1",rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("DanutaNieznam",rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("wasatyLeczsz34",rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("PanBurmistrz98",rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("Antoniawracaj",rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("policjaGwiezdna20",rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("benaffleck45",rodzaj_surek="promerium", ilosc_surek=3000)
#
# kierownik.rozpocznij_sekwencje_zarabiania("sajmonpegg5",rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("TADZIKenter",rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("kociakiTAKEJA",rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("trytoniKolhoz",rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("kudlaczeNAtargu",rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("fajerwerkiwkosm",rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("planetaSWmikolaja",rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("zjdFEDERACJApln",rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("walkaZnuda",rodzaj_surek="promerium", ilosc_surek=3000)
# kierownik.rozpocznij_sekwencje_zarabiania("zamkniecieparasola",rodzaj_surek="promerium", ilosc_surek=3000)





# ################### PETLA ULEPSZANIA - POCZATEK #######################
# kierownik.spij_odliczone_sekundy()
# kierownik.wybudzanie()
#
# while True:
#     kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("WielkiPtak45")
#     czas_rozpoczecia = kierownik.daj_aktualna_godzine() #zapisanie godziny do wpisania w sprawozdanie
#     kierownik.zapisanie_godziny_wybudzenia(uwzgledniana_ilosc_godzin=5.4) #zapisanie godziny po zakonczeniu przez pierwsze konto
#     kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("GeneralojcjeC")
#     kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("SynKapitanna")
#     kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("BoBoKSPOK1")
#     kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("DanutaNieznam")
#     kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("wasatyLeczsz34")
#     kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("PanBurmistrz98")
#     kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("Antoniawracaj")
#     kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("policjaGwiezdna20")
#     kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("benaffleck45")
#
#     kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("sajmonpegg5")
#     kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("TADZIKenter")
#     kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("kociakiTAKEJA")
#     kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("trytoniKolhoz")
#     kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("kudlaczeNAtargu")
#     kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("fajerwerkiwkosm")
#     kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("planetaSWmikolaja")
#     kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("zjdFEDERACJApln")
#     kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("walkaZnuda")
#     kierownik.rozpocznij_sekwencje_ulepszania_skylabu_itp("zamkniecieparasola")
#
#     kierownik.zapisz_sprawozdanie_czasowe(czas_rozpoczecia)
#     kierownik.spij_odliczone_sekundy()
#     kierownik.wybudzanie()

# ################### PETLA ULEPSZANIA - KONIEC #######################
















################### PETLA ZARABIANIA - POCZATEK #######################
kierownik.spij_odliczone_sekundy()
kierownik.wybudzanie()

while True:
    kierownik.rozpocznij_sekwencje_zarabiania("KONSOLETA", rodzaj_surek="promerium", ilosc_surek=3000)
    czas_rozpoczecia = kierownik.daj_aktualna_godzine() #zapisanie godziny do wpisania w sprawozdanie
    kierownik.zapisanie_godziny_wybudzenia(uwzgledniana_ilosc_godzin=6) #zapisanie godziny po zakonczeniu przez pierwsze konto
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

    kierownik.rozpocznij_sekwencje_zarabiania("WielkiPtak45", rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("GeneralojcjeC", rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("SynKapitanna", rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("BoBoKSPOK1", rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("DanutaNieznam", rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("wasatyLeczsz34", rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("PanBurmistrz98", rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("Antoniawracaj", rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("policjaGwiezdna20", rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("benaffleck45", rodzaj_surek="promerium", ilosc_surek=3000)

    kierownik.rozpocznij_sekwencje_zarabiania("sajmonpegg5", rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("TADZIKenter", rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("kociakiTAKEJA", rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("trytoniKolhoz", rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("kudlaczeNAtargu", rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("fajerwerkiwkosm", rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("planetaSWmikolaja", rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("zjdFEDERACJApln", rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("walkaZnuda", rodzaj_surek="promerium", ilosc_surek=3000)
    kierownik.rozpocznij_sekwencje_zarabiania("zamkniecieparasola", rodzaj_surek="promerium", ilosc_surek=3000)


    kierownik.zapisz_sprawozdanie_czasowe(czas_rozpoczecia)
    kierownik.spij_odliczone_sekundy()
    kierownik.wybudzanie()

################### PETLA ZARABIANIA - KONIEC #######################















# ###### wyplata###############
#
# sleep(3)
# kierownik.wyplac_hajsownikom(ilosc_statkow=20, numer_statku=22, ilosc_kredytow=5000000)
# ########## koniec wyplaty ###############

