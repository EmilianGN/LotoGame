import sqlite3

connection = sqlite3.Connection('Jucatori.db')

cursor = connection.cursor()

table_jucatori="""
CREATE TABLE Jucatori (
ValoareID INT NOT NULL,
NumereJucate VARCHAR(127) NOT NULL,
PRIMARY KEY (ValoareID)
);
"""


cursor.execute(table_jucatori)

connection.commit()

connection.close()