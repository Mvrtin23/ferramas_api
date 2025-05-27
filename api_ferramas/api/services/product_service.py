from api.db.database import get_db
from api.models.product import Product

def get_all_products():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, price FROM products")
    rows = cursor.fetchall()
    products = [Product(**row).to_dict() for row in rows]
    return products
