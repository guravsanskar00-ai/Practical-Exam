from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "secret123"

@app.route('/', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        name = request.form['name']
        mobile = request.form['mobile']
        event = request.form['event']

        if not name or not mobile or not event:
            flash("Please fill all fields.")
        else:
            flash(
                f"Registration Successful! "
                f"Name: {name}, Mobile: {mobile}, Event: {event}"
            )

    return render_template('event.html')

if __name__ == '__main__':
    app.run(debug=True)