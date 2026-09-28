from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    message = "Welcome to Flask Application!"
    return render_template('home.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)