from statistics import correlation

from numere import Numere
from jucatori import Jucator
from jucatori import Jucatori

class Loto:
    buget_companie = 13000
    def __init__(self,nume,adresa="default",buget=buget_companie):
        self.nume=nume
        self.adresa=adresa
        self.buget=buget

class JocDeNoroc(Loto):
    def __init__(self,nume,procent_buget):
        super().__init__(nume=nume,buget=Loto.buget_companie*procent_buget)


    @staticmethod
    def porneste_jocul(nume,procent_buget,ii_jucator=1):
        joc = JocDeNoroc(nume, procent_buget)

        jucator = Jucator.alege_numere(ii_jucator)
        jucatori = Jucatori(550)

        numerere_extrase = Numere.extragere()
        print(numerere_extrase)
        numere_ghicite = numerere_extrase.intersection(jucator)

        # print(f"{jucator} Numere Jucate")
        # print(numere_ghicite)
        # print(f"Ai castigat {joc.castiguri(numere_ghicite)}")
        for n_jucator in (jucatori.lista_jucatori):
            n_numere_ghicite = numerere_extrase.intersection(n_jucator.numere)
            # print(f"{n_jucator.numere}   {n_jucator.nume}")
            # print(n_numere_ghicite)
            rezultat = joc.castiguri(n_numere_ghicite)
            if rezultat is not None:
                if rezultat[1]>2:
                    print(f"Ai castigat {joc.castiguri(n_numere_ghicite)}")

    def castiguri(self,numere_ghicite):
        premiu=self.buget

        if len(numere_ghicite)==6:
            return [premiu*0.8 ,6]
        elif len(numere_ghicite)==5:
            return [premiu * 0.6,5]
        elif len(numere_ghicite)==4:
            return [premiu * 0.4,4]
        elif len(numere_ghicite)==3:
            return [(premiu * 0.2)/,3]
        else:
            # print("Mai incearca o data!")
            return None


JocDeNoroc.porneste_jocul("6/49", 0.4, 0)


