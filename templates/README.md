=# BagBazzar

#### Video Demo: <YOUR VIDEO URL HERE>

---

### Description

BagBazzar is a Flask-based web application designed to connect buyers and sellers in the bag industry. Sellers can list their custom bags by submitting product details and uploading images, while buyers can register and browse products by category. The application provides a dashboard, product category pages, and a confirmation popup after form submissions.

---

### Features

- **Seller registration and bag listing**: Sellers can submit personal details and add bags with descriptions, prices, categories, and images.
- **Buyer registration**: Buyers can register with contact information and a password.
- **Product browsing**: Users can view bags categorized by types like backpacks, totes, etc.
- **File uploads**: Supports image uploads for bags, stored securely on the server.
- **Dashboard**: Placeholder for future admin functionalities.
- **Confirmation popup** after successful form submission.

---

### Project Structure

- `project.py`: Main Flask app with routes handling user interactions, database insertions, and page rendering.
- `db.py`: Database connection module (assumed MySQL).
- `test_project.py`: Unit tests using `pytest` to verify database insertions for sellers, buyers, and bags.
- `requirements.txt`: Python dependencies required to run the project.
- `templates/html/`: HTML template files for all pages.
- `static/uploads/`: Directory where uploaded images are saved.

---

### How to Run

1. Clone the repo and navigate to the project directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask app:
   python project.py
4. Open your browser and visit http://127.0.0.1:5000/ to see the app.

5. Add a note about your database setup

Since your app depends on MySQL and a `db.py` connection, it’s good to mention this so users know they need to set it up before running.

Example:

```markdown
### Database Setup

- Ensure you have MySQL installed and running.
- Create a database (e.g., `bagbazzar`) and run the required SQL scripts to create tables (`sellers`, `buyers`, `bags`).
- Update your `db.py` with your MySQL credentials.
- Sample table creation scripts can be added here or in a separate file.

### Credits

Developed by: Harsh Thakur
GitHub: https://github.com/Harshthakur8569
edX: https://www.edx.org/user/HT_2002
Location: Delhi, India  
Date: 2025-05-31
```
