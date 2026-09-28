from flask import Flask, render_template

app = Flask(__name__)

employees = [
    {"name": "Sanskar", "department": "IT", "experience": 0},
    {"name": "Rahul", "department": "HR", "experience": 2},
    {"name": "Amit", "department": "Sales", "experience": 6},
    {"name": "Priya", "department": "Finance", "experience": 10}
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/employees')
def employee():
    return render_template('employees.html', employees=employees)

@app.route('/department')
def department():
    return render_template('department.html')

if __name__ == '__main__':
    app.run(debug=True)