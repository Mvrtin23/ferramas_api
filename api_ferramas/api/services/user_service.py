from api.db.database import get_db
from api.models.user import User

def get_all_users():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM users")
    rows = cursor.fetchall()
    users = [User(**row).to_dict() for row in rows]
    return users
