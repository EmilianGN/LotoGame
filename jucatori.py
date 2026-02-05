from random import randint
from xml.etree.ElementTree import tostring

from faker import Faker


class Jucator:
    def __init__(self,nume=None,numere=None):
        if nume is None and numere is None:
            fake = Faker()
            self.nume = fake.name()
            self.numere = Jucator.alege_numere(0)
        else:
            self.nume = nume
            self.numere = numere
    @staticmethod
    def alege_numere(ii_jucator=1):
        '''

        :param ii_jucator: 1jucator 0cpu
        :return: numere_alese
        '''

        numere_alese = set()
        if ii_jucator:
            print(f"Alege 6 numere")
        while len(numere_alese) < 6:
            interval=False
            while not interval:
                e_numar=False
                while not e_numar:
                    try:
                        if ii_jucator:
                            numar_ales = int(input("Introdu un numar: \n"))
                        else:
                            numar_ales = randint(1,49)
                        e_numar=True
                    except ValueError:
                        print("Numar invalid.")
                if numar_ales > 0 and numar_ales <50:
                    interval=True
                    numere_alese.add(numar_ales)
                else:
                    print("Alege un numar intre 1 si 49")
        return numere_alese

class Jucatori:
    lista_jucatori=[]
    def __init__(self,numar_jucatori : int):
        self.numar_jucatori = numar_jucatori
        for n in range(numar_jucatori):
            un_jucator = Jucator()
            Jucatori.lista_jucatori.append(un_jucator)


class Castigator(Jucator):
    def __init__(self,categorie=0,numere_ghicite=None,suma=0,nume=None,numere=None):
        super().__init__(nume,numere)
        self.categorie=categorie
        self.numere_ghicite=numere_ghicite
        self.suma=suma

    def __repr__(self):
        scris = (f"{self.nume:<25s} Numere {str(self.numere):<27s}"
                 f" Ghicite {str(self.numere_ghicite):<27} Cat:{self.categorie:<2}"
                 f" Castig:{self.suma}")
        return  scris

class ListaCastigatori:
    def __init__(self):
        self.lista_castigatori=list()
