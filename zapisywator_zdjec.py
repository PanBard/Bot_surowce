import  os

class Lista_zdjec:

    def tworz_liste_do_handlu_surkami(self):
        #bierze aktualną cierzkę w której znajduje się projekt
        path = os.getcwd()

        # doklejamy do ściezkik nazwę folderu
        res = os.listdir(path + '\\img\\')

        # print(res)

        #otwieramy plik
        plik_txt = open("lista.txt","wt")

        #zapisywanie nazw zdjęć po kolei w pliku txt
        for lines in res:
            plik_txt.writelines( lines + '\n')

        #zamykamy plik
        plik_txt.close()

    def tworz_liste_do_ulepszenia_skylabu(self):
        #bierze aktualną cierzkę w której znajduje się projekt
        path = os.getcwd()

        # doklejamy do ściezkik nazwę folderu
        res = os.listdir(path + '\\img2\\')

        # print(res)

        #otwieramy plik
        plik_txt = open("lista_skylab.txt","wt")

        #zapisywanie nazw zdjęć po kolei w pliku txt
        for lines in res:
            plik_txt.writelines( lines + '\n')

        #zamykamy plik
        plik_txt.close()


