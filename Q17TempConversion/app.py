from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def temperature():

    result = None

    if request.method == 'POST':

        temp = float(request.form['temp'])
        conversion = request.form['conversion']

        if conversion == 'CtoF':
            result = (temp * 9 / 5) + 32
            unit = "°F"

        else:
            result = (temp - 32) * 5 / 9
            unit = "°C"

        return render_template(
            'temperature.html',
            result=result,
            unit=unit
        )

    return render_template('temperature.html')

if __name__ == '__main__':
    app.run(debug=True)