import pytest
from db import get_connection

@pytest.fixture
def db_conn():
    conn = get_connection()
    cursor = conn.cursor()
    yield conn, cursor
    conn.rollback()  # Rollback changes after each test
    cursor.close()
    conn.close()

def test_insert_seller(db_conn):
    conn, cursor = db_conn
    seller_data = ("Test Seller", "seller@example.com", "1234567890", "123 Test Street")
    
    cursor.execute(
        "INSERT INTO sellers (name, email, phone, address) VALUES (%s, %s, %s, %s)",
        seller_data
    )
    conn.commit()
    cursor.execute("SELECT * FROM sellers WHERE email = %s", (seller_data[1],))
    result = cursor.fetchone()

    assert result is not None
    assert result[1] == "Test Seller"
    assert result[2] == "seller@example.com"

def test_insert_buyer(db_conn):
    conn, cursor = db_conn
    buyer_data = ("Test Buyer", "buyer@example.com", "9876543210", "testpass123")
    
    cursor.execute(
        "INSERT INTO buyers (name, email, phone, password) VALUES (%s, %s, %s, %s)",
        buyer_data
    )
    conn.commit()
    cursor.execute("SELECT * FROM buyers WHERE email = %s", (buyer_data[1],))
    result = cursor.fetchone()

    assert result is not None
    assert result[1] == "Test Buyer"
    assert result[2] == "buyer@example.com"

def test_insert_bag(db_conn):
    conn, cursor = db_conn

    # Insert a test seller first to satisfy foreign key
    seller_data = ("Bag Owner", "bagowner@example.com", "1112223333", "Bag Street")
    cursor.execute(
        "INSERT INTO sellers (name, email, phone, address) VALUES (%s, %s, %s, %s)",
        seller_data
    )
    seller_id = cursor.lastrowid

    # Now insert a bag for that seller
    bag_data = (seller_id, "Test Bag", "A stylish test bag", 499.99, "backpacks", "testbag.jpg")
    cursor.execute(
        """INSERT INTO bags 
        (seller_id, bag_name, bag_description, bag_price, bag_category, bag_image) 
        VALUES (%s, %s, %s, %s, %s, %s)""",
        bag_data
    )
    conn.commit()
    cursor.execute("SELECT * FROM bags WHERE bag_name = %s", ("Test Bag",))
    result = cursor.fetchone()

    assert result is not None
    assert result[2] == "Test Bag"
    assert result[3] == "A stylish test bag"
