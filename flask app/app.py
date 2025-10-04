from flask import Flask, request, redirect, url_for
import psycopg2
from celery import Celery

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        dbname="mydatabase",
        user="user",
        password="password",
        host="db", 
        port="5432"
    )
    return conn

def create_database_and_table():
    """Function for creating DB and Table 'items'."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        );
    ''')
    conn.commit()
    conn.close()

@app.before_request
def initialize_database():
    """Initialisation of DB before every request"""
    create_database_and_table()

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)
    return celery

app.config['CELERY_BROKER_URL'] = 'redis://redis:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://redis:6379/0'

celery = make_celery(app)

@app.route('/')
def home():
    create_database_and_table()
    return '''
        <html>
            <body>
                <h1>Welcome to the main page!</h1>
                <button onclick="window.location.href='/allow';">Take me to Allow</button>
            </body>
        </html>
    '''

@app.route('/allow', methods=['GET', 'POST'])
def allow():
    if request.method == 'POST':
        item_name = request.form['item_name']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO items (name) VALUES (%s);', (item_name,))
        conn.commit()
        conn.close()
        
        return redirect(url_for('allow', success='true'))

    return '''
        <html>
            <body>
                <h1>Welcome to Allow page!</h1>
                <form method="POST">
                    <label for="item_name">Unesite podatke:</label>
                    <input type="text" id="item_name" name="item_name" required>
                    <button type="submit">Add to the the database</button>
                </form>
                <button onclick="window.location.href='/ispis';">Show data</button>
                <button onclick="window.location.href='/obris';">Go to delete page</button>
            </body>
        </html>
    '''

@app.route('/ispis')
def ispis():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items;')
    items = cursor.fetchall()
    conn.close()

    html = '<h1>Data from the database:</h1><ul>'
    for item in items:
        html += f'<li>{item[1]}</li>'
    html += '</ul>'
    return html

@app.route('/obris', methods=['GET', 'POST'])
def obris():
    if request.method == 'POST':
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM items WHERE id = (SELECT MAX(id) FROM items);')
        conn.commit()
        conn.close()
        
        return redirect(url_for('obris'))

    return '''
        <html>
            <body>
                <h1>Deleting page</h1>
                <form method="POST">
                    <button type="submit">Delete the last element</button>
                </form>
                <button onclick="window.location.href='/ispis';">Show data</button>
            </body>
        </html>
    '''

if __name__ == '__main__':
    create_database_and_table()
    app.run(debug=True, host='0.0.0.0')