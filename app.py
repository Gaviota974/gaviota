from flask import Flask, render_template

app = Flask(__name__)

# Liste des catégories avec id, titre, prix et des informations fictives
categories = [
    {"id": 1, "title": " Asian leak ", "price": 6.99 , "image": "category1.jpg"},
    {"id": 2, "title": "Latina leak ", "price": 6.99, "image": "category2.jpg"},
    {"id": 3, "title": "Ebony leak ", "price": 6.99, "image": "category3.jpg"},
    {"id": 4, "title": "Homemade", "price": 10, "image": "category4.jpg"},
    {"id": 5, "title": "All", "price": 19.99, "image": "category5.jpg"},
]

@app.route('/')
def index():
    return render_template('index.html', categories=categories)

@app.route('/category/<int:category_id>')
def category(category_id):
    category = next((cat for cat in categories if cat["id"] == category_id), None)
    return render_template('category.html', category=category)

if __name__ == "__main__":
    app.run(debug=True)
