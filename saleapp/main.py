from flask import Flask, render_template, request
from saleapp import app
from saleapp import dao

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/products")
def product_list():
    keyword = request.args["keyword"] if request.args.get("keyword") else None
    return render_template("product-list.html", products=dao.read_products(keyword=keyword))

@app.route("/products/<int:cate_id>")
def product_by_cate_id(cate_id):
    return render_template("product-list.html", products=dao.read_product_by_category_id(category_id=cate_id))


if __name__ == "__main__":
    app.run(debug=True)