import os

import sqlite3
from flask import (
    Flask,
    g,
    jsonify,
)

DATABASE = 'employees.db'
app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def get_hello():
    return {'hello': 'world'}

@app.route('/employees')
def get_employees():
    return jsonify([
            dict(row)
            for row in get_db()
                .execute('SELECT * FROM employees')
                .fetchall()
        ])

if __name__ == '__main__':
    # This is used when running locally
    app.run(
        host='127.0.0.1',
        port=os.getenv('PORT', default=8080),
        debug=True,
    )
