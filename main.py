from flask import Flask, render_template, request, redirect, url_for
from db import get_connection  # Keep DB connection logic isolated
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('html/index.html')

# Seller form page
@app.route('/seller', methods=['GET', 'POST'])
def seller():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        address = request.form.get('address')

        bag_name = request.form.get('bag_name')
        bag_description = request.form.get('bag_description')
        bag_price = request.form.get('bag_price')
        bag_category = request.form.get('bag_category')

        bag_image = request.files.get('bag_image')
        image_filename = None

        if bag_image and allowed_file(bag_image.filename):
            image_filename = secure_filename(bag_image.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)
            bag_image.save(image_path)

        # Save to database
        conn = get_connection()
        cursor = conn.cursor()

        # Insert seller info
        cursor.execute(
            "INSERT INTO sellers (name, email, phone, address) VALUES (%s, %s, %s, %s)",
            (name, email, phone, address)
        )
        seller_id = cursor.lastrowid

        # Insert bag info
        cursor.execute(
            """INSERT INTO bags 
            (seller_id, bag_name, bag_description, bag_price, bag_category, bag_image) 
            VALUES (%s, %s, %s, %s, %s, %s)""",
            (seller_id, bag_name, bag_description, bag_price, bag_category, image_filename)
        )

        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('popup'))

    return render_template('html/seller.html')

# Buyer form page
@app.route('/buyer', methods=['GET', 'POST'])
def buyer():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO buyers (name, email, phone, password) VALUES (%s, %s, %s, %s)",
            (name, email, phone, password)
        )
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('popup'))

    return render_template('html/buyer.html')

# Confirmation page
@app.route('/popup')
def popup():
    return render_template('html/popup2.html')

# Dashboard page
@app.route('/dashboard')
def dashboard():
    return render_template('html/dashboard.html')

# Product categories
@app.route('/products/<category>')
def show_category(category):
    try:
        return render_template(f'html/{category}.html')
    except:
        return "Category page not found", 404
    
    
@app.route('/products/bags')
def bags():
    return render_template('html/bags.html')    

if __name__ == '__main__':
    app.run(debug=True)
