from random import randint

from faker import Faker


class Jucator:
    def __init__(self):
        fake = Faker()
        self.nume = fake.name()
        self.numere = Jucator.alege_numere(0)
    @staticmethod
    def alege_numere(ii_jucator=1):
        '''

        :param ii_jucator: 1jucator 0cpu
        :return:
        '''

        numere_alese = set()
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


# jucatori = Jucatori(3)
# for jucator in (jucatori.lista_jucatori):
#     print(f"{jucator.numere}   {jucator.nume}")

# for i in range(len(jucatori.lista_jucatori)):
#     print(f"{jucatori.lista_jucatori[i].numere}   {jucatori.lista_jucatori[i].nume}")