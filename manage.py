from app import db, app, Product

def init_db():
    with app.app_context():
        db.create_all()
        print("Database initialized!")

def add_sample_product():
    with app.app_context():
        sample_product = Product(
            name='Sample Product',
            price=9.99,
            description='This is a sample product.',
            image_url='/static/images/sample.jpg'
        )
        db.session.add(sample_product)
        db.session.commit()
        print("Sample product added!")

if __name__ == '__main__':
    init_db()
    add_sample_product()
