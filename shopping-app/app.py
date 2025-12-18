from flask import Flask, render_template_string, request

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mobile", "price": 20000},
    {"id": 3, "name": "Headphones", "price": 2000}
]

cart = []

HTML = """
<h1>🛒 Simple Shopping App</h1>
<h2>Products</h2>
<ul>
{% for p in products %}
<li>{{p.name}} - ₹{{p.price}}
<form method="post" action="/add">
<input type="hidden" name="id" value="{{p.id}}">
<button>Add to Cart</button>
</form>
</li>
{% endfor %}
</ul>

<h2>Cart</h2>
<ul>
{% for c in cart %}
<li>{{c.name}} - ₹{{c.price}}</li>
{% endfor %}
</ul>
"""

@app.route("/")
def home():
    return render_template_string(HTML, products=products, cart=cart)

@app.route("/add", methods=["POST"])
def add():
    pid = int(request.form["id"])
    for p in products:
        if p["id"] == pid:
            cart.append(p)
    return home()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
