from flask import Flask, render_template

app = Flask(__name__)

courses = [
    "Python",
    "Java",
    "Web Technology",
    "Data Science",
    "Computer Networks"
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/courses')
def course():
    return render_template('courses.html', courses=courses)

if __name__ == '__main__':
    app.run(debug=True)