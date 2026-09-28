from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "secret123"

@app.route('/', methods=['GET', 'POST'])
def attendance():

    percentage = None
    name = ""

    if request.method == 'POST':

        name = request.form['name']
        total_days = int(request.form['total_days'])
        present_days = int(request.form['present_days'])

        if total_days <= 0:
            flash("Total working days must be greater than 0.")

        else:
            percentage = (present_days / total_days) * 100

            if percentage >= 75:
                flash("Eligible for examination.")
            else:
                flash("Not Eligible for examination.")

    return render_template(
        'attendance.html',
        name=name,
        percentage=percentage
    )

if __name__ == '__main__':
    app.run(debug=True)