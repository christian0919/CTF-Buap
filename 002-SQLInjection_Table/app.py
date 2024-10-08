from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Conexión a la base de datos SQLite
def get_db_connection():
    conn = sqlite3.connect('mydatabase.db')
    conn.row_factory = sqlite3.Row
    return conn

# Crear la tabla flag y agregar un registro
def init_db():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS flag (id INTEGER PRIMARY KEY, value TEXT)')
    conn.execute('INSERT INTO flag (value) VALUES ("fPqUzum4ky")')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        user_input = request.form['user_input']

        # Aquí está la inyección SQL vulnerable
        query = f"SELECT * FROM flag WHERE value = '{user_input}'"

        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
        except sqlite3.Error as e:
            result = [("Error en la consulta: ", e)]
        finally:
            conn.close()

    return render_template('form.html', result=result)

if __name__ == '__main__':
    init_db()  # Inicializa la base de datos
    app.run(debug=True)
