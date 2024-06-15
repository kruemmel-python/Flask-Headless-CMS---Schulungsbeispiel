import base64
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'images')
app.config['MAX_CONTENT_PATH'] = 1000000  # max 1MB

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        try:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], os.path.basename(self.image_url))
            print(f"Loading image from: {image_path}")
            with open(image_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            return {
                'id': self.id,
                'name': self.name,
                'price': self.price,
                'description': self.description,
                'image_url': self.image_url,
                'image_data': encoded_string
            }
        except Exception as e:
            print(f"Error encoding image from {image_path}: {e}")
            return {
                'id': self.id,
                'name': self.name,
                'price': self.price,
                'description': self.description,
                'image_url': self.image_url,
                'image_data': None,
                'error': str(e)
            }

@app.route('/products', methods=['GET'])
def get_products():
    try:
        products = Product.query.all()
        product_dicts = [product.to_dict() for product in products]
        print(f"Returning products: {product_dicts}")
        return jsonify(product_dicts)
    except Exception as e:
        print(f"Error getting products: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/products', methods=['POST'])
def add_product():
    try:
        data = request.form
        file = request.files['image']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print(f"Saved image to: {os.path.join(app.config['UPLOAD_FOLDER'], filename)}")

        new_product = Product(
            name=data['name'],
            price=float(data['price']),
            description=data['description'],
            image_url=filename  # Save only the filename, not the full path
        )
        db.session.add(new_product)
        db.session.commit()
        return jsonify(new_product.to_dict()), 201
    except Exception as e:
        print(f"Error adding product: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        return redirect(url_for('add_product'))
    return render_template('admin.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if not Product.query.first():
            sample_product = Product(
                name='Sample Product',
                price=9.99,
                description='This is a sample product.',
                image_url='sample.jpg'
            )
            db.session.add(sample_product)
            db.session.commit()
    app.run(debug=True)
