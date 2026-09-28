from flask import Flask, render_template

app = Flask(__name__)

products = [
    {"name": "Laptop", "price": 50000, "available": True},
    {"name": "Mobile", "price": 20000, "available": True},
    {"name": "Headphones", "price": 1500, "available": False},
    {"name": "Keyboard", "price": 1000, "available": True}
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products_page():
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)