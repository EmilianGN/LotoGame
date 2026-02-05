import sqlite3

class ConexiuneSql:
    @staticmethod
    def sql_query(db_file, db_query, db_table, drop=False):
        connection = sqlite3.connect(db_file)  # connect to database from db_file
        cursor = connection.cursor()  # cursor
        if drop:
            cursor.execute(f"""
                DROP TABLE IF EXISTS "{db_table}" 
                """)  # Execute a drop command
            connection.commit()  # commit the drop query

        cursor.execute(db_query)  # execute users query
        connection.commit()  # commit users query

        connection.close()

    @staticmethod
    def sql_query_result(db_file, db_query, print_out=False):
        connection = sqlite3.connect(db_file)  # connect to database from db_file
        cursor = connection.cursor()  # cursor
        cursor.execute(db_query)  # execute the query
        rows = cursor.fetchall()  # fetch all the output
        if print_out:
            for row in rows:
                print(row)
        connection.close()  # close the connection
        return rows

    @staticmethod
    def sql_query_get_last_id(db_file, db_table):
        last_id = ConexiuneSql.sql_query_result(db_file, f"""SELECT MAX(ID) FROM "{db_table}";""")
        last_id = last_id[0][0]  # last_id is a list of tuples, so the value we want is at that index
        if last_id is None:
            last_id = 0
        return last_id