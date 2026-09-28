from flask import Flask, render_template, request, flash
from datetime import date, datetime

app = Flask(__name__)
app.secret_key = "secret123"

@app.route('/', methods=['GET', 'POST'])
def age():

    calculated_age = None
    name = ""

    if request.method == 'POST':

        name = request.form['name']
        dob = request.form['dob']

        if not name or not dob:
            flash("Please enter Name and Date of Birth.")
        else:
            birth_date = datetime.strptime(dob, "%Y-%m-%d").date()
            today = date.today()

            calculated_age = today.year - birth_date.year

            if (today.month, today.day) < (birth_date.month, birth_date.day):
                calculated_age -= 1

    return render_template(
        'age.html',
        name=name,
        age=calculated_age
    )

if __name__ == '__main__':
    app.run(debug=True)