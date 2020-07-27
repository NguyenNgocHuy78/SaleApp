from saleapp import app
import json
import os

def read_products(keyword=None, from_price=None, to_price=None):
    with open(os.path.join(app.root_path, "data/products.json"), encoding="utf-8") as f:
        products = json.load(f)

        if keyword:
            return [product for product in products if product["name"].lower().find(keyword.lower()) >= 0]

        if from_price and to_price:
            return [product for product in products if product["price"] >= from_price and product["price"] <= to_price]

        return products

def read_product_by_category_id(category_id):
    return [product for product in read_products() if product["category_id"] == category_id]

def read_categories():
    with open(os.path.join(app.root_path, "data/categories.json"), encoding="utf-8") as f:
        return json.load(f)

def read_product_by_id(product_id):
    products = read_products()
    for p in products:
        if p.id == product_id:
            return p
    return None


def add_products(name, description, price, image, category):
    product = read_products()
    product.append({
            "id": len(product) + 1,
            "name": name,
            "description": description,
            "price": float(price),
            "image": image,
            "category_id": int(category)
        })
    try:
        with open(os.path.join(app.root_path, "data/products.json"), "w", encoding="utf-8") as f:
            json.dump(product, f, ensure_ascii=False, indent=4)

        return True
    except Exception as ex:
        print(ex)
        return False

if __name__ == "__main__":
    print(read_products())