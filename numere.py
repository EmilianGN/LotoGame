import random
from random import randint


class Numere:
    numbers = list(range(1, 50))
    numere_extrase = set()
    @classmethod
    def extragere(cls):
        counter = 0
        while counter < 6:
            cls.numere_extrase.add(cls.numbers.pop(randint(0, len(cls.numbers) - 1)))
            counter += 1
        return (cls.numere_extrase)

