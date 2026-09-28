from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/student')
def student():
    name = "Sanskar"
    roll = 101
    course = "B.Sc. Computer Science"

    return render_template(
        'student.html',
        name=name,
        roll=roll,
        course=course
    )

if __name__ == '__main__':
    app.run(debug=True)