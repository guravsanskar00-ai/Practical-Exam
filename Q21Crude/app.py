from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


def get_db():
    conn = sqlite3.connect('student.db')
    conn.row_factory = sqlite3.Row
    return conn


def create_database():

    conn = get_db()

    conn.execute('''
        CREATE TABLE IF NOT EXISTS student (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            course TEXT
        )
    ''')

    conn.commit()
    conn.close()


@app.route('/')
def home():

    conn = get_db()

    students = conn.execute(
        "SELECT * FROM student"
    ).fetchall()

    conn.close()

    return render_template(
        'home.html',
        students=students
    )


@app.route('/add', methods=['GET', 'POST'])
def add():

    if request.method == 'POST':

        id = request.form['id']
        name = request.form['name']
        age = request.form['age']
        course = request.form['course']

        conn = get_db()

        conn.execute(
            "INSERT INTO student VALUES (?, ?, ?, ?)",
            (id, name, age, course)
        )

        conn.commit()
        conn.close()

        return redirect('/')

    return render_template('add.html')


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):

    conn = get_db()

    student = conn.execute(
        "SELECT * FROM student WHERE id=?",
        (id,)
    ).fetchone()

    if request.method == 'POST':

        name = request.form['name']
        age = request.form['age']
        course = request.form['course']

        conn.execute(
            '''
            UPDATE student
            SET name=?, age=?, course=?
            WHERE id=?
            ''',
            (name, age, course, id)
        )

        conn.commit()
        conn.close()

        return redirect('/')

    conn.close()

    return render_template(
        'update.html',
        student=student
    )


@app.route('/delete/<int:id>')
def delete(id):

    conn = get_db()

    conn.execute(
        "DELETE FROM student WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect('/')


if __name__ == '__main__':
    create_database()
    app.run(debug=True)