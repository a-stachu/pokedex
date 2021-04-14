import sqlite3

with open('pokemony.csv', 'r') as file:
    conn = sqlite3.connect('pokemon.db')
    conn.execute("DROP TABLE IF EXISTS pokemon")
    conn.execute("CREATE TABLE pokemon(" +
                 "[pokemon_id] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, " +
                 "[Name] VARCHAR(32) NOT NULL, " +
                 "[Type1] VARCHAR(32) NOT NULL, " +
                 "[Type2] VARCHAR(32) NOT NULL, " +
                 "[HP] INT NOT NULL," +
                 "[Attack] FLOAT NOT NULL) ")

    first_row = True

    for row in file:
        if first_row:
            columns = row.rstrip().split()
            first_row = False
        else:
            values = row.rstrip().split(',')
            query = "INSERT INTO pokemon(" + \
                    "," .join(columns) + \
                    ") VALUES(?, ?, ?, ?, ?)"
            conn.execute(query, tuple(values))

conn.commit()
conn.close()