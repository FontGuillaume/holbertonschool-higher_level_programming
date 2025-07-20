from flask import Flask, request, render_template
import csv
import json

app = Flask(__name__)

def read_json(filename):
    with open(filename, "r") as f:
        return json.load(f)  # renvoie une liste directement

def read_csv(filename):
    with open(filename, newline="") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

@app.route("/products")
def product_display():
    source = request.args.get("source")
    product_id = request.args.get("id")
    products = []
    error = None

    if source == "json":
        try:
            products = read_json("products.json")
        except Exception:
            error = "Erreur lors de la lecture du fichier JSON."
    elif source == "csv":
        try:
            products = read_csv("products.csv")
        except Exception:
            error = "Erreur lors de la lecture du fichier CSV."
    else:
        error = "Wrong source"

    # Filtrer par id si demandé
    if not error and product_id:
        filtered = [p for p in products if str(p.get("id")) == str(product_id) or str(p.get("id")) == str(product_id)]
        if filtered:
            products = filtered
        else:
            error = "Product not found"
            products = []

    return render_template("product_display.html", products=products, error=error)

if __name__ == "__main__":
    app.run(debug=True, port=5500)
