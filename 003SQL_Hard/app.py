from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        
        # Consulta insegura que permite inyección SQL
        conn = sqlite3.connect('BD.db')
        c = conn.cursor()
        query = f"SELECT * FROM honney WHERE id = '{user_input}'"
        c.execute(query)
        result = c.fetchall()
        conn.close()
        return render_template_string('''
            <pre>{{ results }}</pre>
            <form method="POST">
                <input type="text" name="user_input" placeholder="Ingrese ID" required>
                <input type="submit" value="Enviar">
            </form>
        ''', results=result)

    return render_template_string('''
        <h1>Consulta Insegura</h1>
        <form method="POST">
            <input type="text" name="user_input" placeholder="Ingrese id" required>
            <input type="submit" value="Enviar">
        </form>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
