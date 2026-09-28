from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "secret123"

@app.route('/', methods=['GET', 'POST'])
def order():

    total = None

    if request.method == 'POST':

        name = request.form['name']
        food = request.form['food']

        try:
            quantity = int(request.form['quantity'])
            price = float(request.form['price'])
        except:
            flash("Invalid quantity or price.")
            return render_template('order.html')

        if not name or not food or quantity <= 0 or price <= 0:
            flash("Please enter valid information.")
        else:
            subtotal = quantity * price

            service_charge = subtotal * 0.05

            gst = (subtotal + service_charge) * 0.18

            total = subtotal + service_charge + gst

            return render_template(
                'order.html',
                name=name,
                food=food,
                quantity=quantity,
                price=price,
                subtotal=subtotal,
                service_charge=service_charge,
                gst=gst,
                total=total
            )

    return render_template('order.html')

if __name__ == '__main__':
    app.run(debug=True)