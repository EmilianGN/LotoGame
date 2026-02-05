import sqlite3

class ConexiuneSql:
    @staticmethod
    def sql_query(fisier_db, query_db, tabel_db, drop=False):
        connection = sqlite3.connect(fisier_db)  # conectare la baza de date din fisier_db
        cursor = connection.cursor()  # cursor
        if drop:
            cursor.execute(f"""
                DROP TABLE IF EXISTS "{tabel_db}" 
                """)  # executa comanda drop
            connection.commit()  # comite interogarea drop

        cursor.execute(query_db)  # executa interogarea
        connection.commit()  # comite interogarea

        connection.close()  # inchide conexiunea

    @staticmethod
    def sql_query_result(db_file, db_query, print_out=False):
        '''
        This is a method that returns a result from database
        :param db_file:
        :param db_query:
        :param print_out:
        :return: returns a list of tuples
        '''
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        cursor.execute(db_query)
        rows = cursor.fetchall()
        if print_out:
            for row in rows:
                print(row)
        connection.close()
        return rows

    @staticmethod
    def sql_query_get_last_id(fisier_db, db_table):
        last_id = ConexiuneSql.sql_query_result(fisier_db, f"""SELECT MAX(ID) FROM "{db_table}";""")
        last_id = last_id[0][0]  # last_id este o tupla, deci valoarea care o cautam este chiar la acel index
        if last_id is None:
            last_id = 0
        return last_id