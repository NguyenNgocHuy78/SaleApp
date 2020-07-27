from flask import Flask, render_template, request, redirect, url_for
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

@app.route("/products/add", methods=["get", "post"])
def product_add():

    err_msg = None
    if request.method.lower() == "post":
        if dao.add_products(**dict(request.form)):
            return redirect(url_for('product-add.html'))
        else:
            err_msg = "Wrong!"

        categories = dao.read_categories()
        product = None
        if request.args.get("product_id"):
            product = dao.read_product_by_id(product_id=request.args("product_id"))

        return redirect(url_for('product-add.html'))

    categories = dao.read_categories()
    return render_template("product-add.html", categories=categories)

if __name__ == "__main__":
    app.run(debug=True)