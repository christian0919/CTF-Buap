import sqlite3

# Crear la base de datos y las tablas
conn = sqlite3.connect('BD.db')
c = conn.cursor()

# Crear la tabla flag
c.execute('''
CREATE TABLE IF NOT EXISTS flag (
    id TEXT PRIMARY KEY
)
''')



# Crear la tabla honney
c.execute('''
CREATE TABLE IF NOT EXISTS honney (
    id TEXT PRIMARY KEY
)
''')

# Insertar datos en honney
c.execute('INSERT INTO flag (id) VALUES (?)', ('s8c7fee',))
# Insertar datos en flag
c.executemany('INSERT INTO honney (id) VALUES (?)', [
    ('123',),
    ('ccsad',),
    ('890809',)
])
conn.commit()
conn.close()
