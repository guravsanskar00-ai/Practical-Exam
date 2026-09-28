from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def create_database():

    conn = sqlite3.connect('student.db')

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            course TEXT
        )
    ''')

    conn.commit()
    conn.close()


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        id = request.form['id']
        name = request.form['name']
        age = request.form['age']
        course = request.form['course']

        conn = sqlite3.connect('student.db')
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO student VALUES (?, ?, ?, ?)",
            (id, name, age, course)
        )

        conn.commit()
        conn.close()

    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM student")

    students = cursor.fetchall()

    conn.close()

    return render_template(
        'home.html',
        students=students
    )


if __name__ == '__main__':
    create_database()
    app.run(debug=True)