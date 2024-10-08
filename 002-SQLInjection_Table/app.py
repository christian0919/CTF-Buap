from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('mydatabase.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        # Obtiene la entrada del usuario
        user_input = request.form['user_input']
        
        # Crea la consulta SQL vulnerable a inyección
        query = f'SELECT * FROM flag WHERE value = "{user_input}"'
        
        # Ejecuta la consulta
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()

    return render_template('form.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
