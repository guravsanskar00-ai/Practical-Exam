from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "secret123"

@app.route('/', methods=['GET', 'POST'])
def contact():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        if not name or not email or not subject or not message:
            flash("Please fill all fields.")
        else:
            flash("Contact form submitted successfully.")

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)