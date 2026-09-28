from flask import Flask, render_template
app = Flask(__name__)
@app.route("/product/<name>/<int:price>/<product_type>")
def product(name, price, product_type):
    discount = price * 0.10
    discounted_price = price - discount
    gst = discounted_price * 0.18
    return render_template("product.html", name=name, price=price, product_type=product_type, discount=discount, discounted_price=discounted_price, gst=gst)
if __name__ == "__main__":
    app.run(debug=True)    