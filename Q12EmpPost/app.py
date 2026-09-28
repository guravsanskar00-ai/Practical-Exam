from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def employee():

    data = None

    if request.method == 'POST':
        emp_id = request.form['emp_id']
        name = request.form['name']
        department = request.form['department']
        designation = request.form['designation']

        data = {
            'emp_id': emp_id,
            'name': name,
            'department': department,
            'designation': designation
        }

    return render_template('employee.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)