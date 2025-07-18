from flask import Flask, request, render_template
import csv
import json

app = Flask(__name__)

@app.route("/")
def product_display():
    source = request.args.get("source")
    product_id = request.args.get("id")
    products = []

    if source == "json":
        with open("products.json", "r") as f:
            data = json.load(f)
            products = data.get("products", [])

    elif source == "csv":
        with open("products.csv", newline="") as f:
            reader = csv.DictReader(f)
            products = [row for row in reader]

    else:
        return "Invalid source parameter", 400
    
    if product_id:
        products = [p for p in products if str(p.get("id")) == str(product_id)]
        return render_template("product_display.html", products=products)
    
if __name__ == "__main__":
    app.run(debug=True, port=5500)
