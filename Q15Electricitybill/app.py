from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bill():

    total = None

    if request.method == 'POST':

        name = request.form['name']
        number = request.form['number']
        units = int(request.form['units'])

        # Example slab rates
        if units <= 100:
            total = units * 5
        elif units <= 200:
            total = (100 * 5) + ((units - 100) * 7)
        else:
            total = (100 * 5) + (100 * 7) + ((units - 200) * 10)

        return render_template(
            'electricity.html',
            name=name,
            number=number,
            units=units,
            total=total
        )

    return render_template('electricity.html')

if __name__ == '__main__':
    app.run(debug=True)