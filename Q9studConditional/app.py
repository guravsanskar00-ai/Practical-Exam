from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result')
def result():

    name = "Sanskar"
    percentage = 82

    return render_template(
        'result.html',
        name=name,
        percentage=percentage
    )

if __name__ == '__main__':
    app.run(debug=True)