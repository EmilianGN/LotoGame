import sqlite3
from pprint import pprint
from statistics import correlation

from numere import Numere
from jucatori import Jucator, ListaCastigatori, Castigator
from jucatori import Jucatori
from sql_db import ConexiuneSql


class Loto:
    buget_companie = 13000
    def __init__(self,nume,adresa="default",buget=buget_companie):
        self.nume=nume
        self.adresa=adresa
        self.buget=buget

class JocDeNoroc(Loto):
    def __init__(self,nume,procent_buget):
        super().__init__(nume=nume,buget=Loto.buget_companie*procent_buget)
        self.numere_castigatoare = Numere.extragere()
    @staticmethod
    def initializare_db(fisier_db,drop=False):
        tabel_db = "Jucatori"
        tabel_jucatori = f"""
        CREATE TABLE {tabel_db} (
        ID INT NOT NULL,
        Nume  VARCHAR(128),
        Numere VARCHAR(128),
        PRIMARY KEY (ID)
        );
        """
        ConexiuneSql.sql_query("baza_de_date.db",tabel_jucatori,tabel_db,True)
        tabel_db = "Rezultate"
        tabel_rezultate = f"""
        CREATE TABLE {tabel_db} (
        ID INT NOT NULL,
        Nume  VARCHAR(128),
        Categorie INT,
        Castig REAL,
        NumereGhicite VARCHAR(128),
        NumereExtrase VARCHAR(128),
        PRIMARY KEY (ID)
        );
        """
        ConexiuneSql.sql_query("baza_de_date.db", tabel_rezultate, tabel_db, True)
    @staticmethod
    def desfasurare_joc(nume, procent_buget, nr_participanti =50, ii_jucator=1):
        '''

        :param nume:
        :param procent_buget:
        :param ii_jucator: 1 for CPU , 0 for UserInput
        :return: lista_castogatori
        '''
        joc = JocDeNoroc(nume, procent_buget)
        jucatori = Jucatori(nr_participanti)
        if ii_jucator:
            nume_ales = input("Cu ce nume doresti sa te inregistrezi?\n")
            numere_jucator = Jucator.alege_numere(ii_jucator)
            jucatori.lista_jucatori.append(Jucator(nume_ales,numere_jucator))
            print(f"{numere_jucator}{nume_ales} ")

        lista_castigatori = ListaCastigatori()
        for n_jucator in (jucatori.lista_jucatori):
            n_numere_ghicite = joc.numere_castigatoare.intersection(n_jucator.numere)
            try:
                query_insert=f"""INSERT INTO Jucatori (ID,Nume,Numere)
                                VALUES({ConexiuneSql.sql_query_get_last_id("baza_de_date.db","Jucatori")+1},
                                "{n_jucator.nume}","{n_jucator.numere}");"""
            except sqlite3.OperationalError:
                JocDeNoroc.initializare_db("baza_de_date.db")
                query_insert = f"""INSERT INTO Jucatori (ID,Nume,Numere)
                                VALUES({ConexiuneSql.sql_query_get_last_id("baza_de_date.db", "Jucatori")+1},
                                "{n_jucator.nume}","{n_jucator.numere}");"""
            try:
                ConexiuneSql.sql_query("baza_de_date.db", query_insert,"Jucatori" )
            except sqlite3.OperationalError:
                JocDeNoroc.initializare_db("baza_de_date.db")
                ConexiuneSql.sql_query("baza_de_date.db", query_insert, "Jucatori")

            cat = joc.categorie(n_numere_ghicite)
            if len(n_numere_ghicite) > 2:
                lista_castigatori.lista_castigatori.append(Castigator(cat,n_numere_ghicite,nume=n_jucator.nume,
                                                                  numere=n_jucator.numere))

        return lista_castigatori , joc

    @staticmethod
    def categorie(numere_ghicite):
        '''
        Stabilire categorie de castig
        :param numere_ghicite:
        :return:
        '''

        if len(numere_ghicite)==6:
            return 1
        elif len(numere_ghicite)==5:
            return 2
        elif len(numere_ghicite)==4:
            return 3
        elif len(numere_ghicite)==3:
            return 4

    def calcul_castiguri(self,castigatori_finali:ListaCastigatori):
        cat_unu = 0
        cat_doi = 0
        cat_trei = 0
        cat_patru = 0
        for w_castigator in castigatori_finali.lista_castigatori:
            if w_castigator.categorie == 1:
                cat_unu +=1
            if w_castigator.categorie == 2:
                cat_doi +=1
            if w_castigator.categorie == 3:
                cat_trei +=1
            if w_castigator.categorie == 4:
                cat_patru +=1
        for w_castigator in castigatori_finali.lista_castigatori:
            if w_castigator.categorie == 1:
                w_castigator.suma = (self.buget*0.6)//cat_unu
            if w_castigator.categorie == 2:
                w_castigator.suma = (self.buget * 0.2) // cat_doi
            if w_castigator.categorie == 3:
                w_castigator.suma = (self.buget * 0.1) // cat_trei
            if w_castigator.categorie == 4:
                w_castigator.suma = (self.buget * 0.05) // cat_patru
        return castigatori_finali

    def salveaza_castigatori(self,castigatori:ListaCastigatori):
        for castigator in castigatori.lista_castigatori:
            try:
                query_insert = f"""INSERT INTO Rezultate (ID,Nume,Categorie,Castig,NumereGhicite,NumereExtrase)
                                VALUES({ConexiuneSql.sql_query_get_last_id("baza_de_date.db", "Rezultate")+1},
                                "{castigator.nume}",{castigator.categorie},{castigator.suma},"{castigator.numere_ghicite}",
                                "{self.numere_castigatoare}");"""
            except sqlite3.OperationalError:
                JocDeNoroc.initializare_db("baza_de_date.db")
                query_insert = f"""INSERT INTO Rezultate (ID,Nume,Categorie,Castig,NumereGhicite,NumereExtrase)
                                VALUES({ConexiuneSql.sql_query_get_last_id("baza_de_date.db", "Rezultate")+1},
                                "{castigator.nume}",{castigator.categorie},{castigator.suma},"{castigator.numere_ghicite}",
                                "{self.numere_castigatoare}");"""
            try:
                ConexiuneSql.sql_query("baza_de_date.db", query_insert, "Rezultate")
            except sqlite3.OperationalError:
                JocDeNoroc.initializare_db("baza_de_date.db")
                ConexiuneSql.sql_query("baza_de_date.db", query_insert, "Rezultate")

    @staticmethod
    def start_joc(nr_participanti,ii_jucator):
        (castigatori, joc) = JocDeNoroc.desfasurare_joc("6/49", 0.4,nr_participanti, ii_jucator)
        castigatori = joc.calcul_castiguri(castigatori)

        print(f"Numere extrase 6/49       ****** {joc.numere_castigatoare} ******")
        for castigator in castigatori.lista_castigatori:
            print(castigator)
        joc.salveaza_castigatori(castigatori)
        # result = ConexiuneSql.sql_query_result("baza_de_date.db","SELECT *FROM Rezultate")
        # pprint(result)

JocDeNoroc.start_joc(550,0)

