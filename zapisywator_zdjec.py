import  os

class Lista_zdjec:

    def tworz_liste(self):
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


