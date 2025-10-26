# Contoh model untuk users (Opsional jika menggunakan ORM seperti SQLAlchemy)
# class User:
#     def __init__(self, fullname, email, password):
#         self.fullname = fullname
#         self.email = email
#         self.password = password

from myapp.app import mysql
from werkzeug.security import check_password_hash,generate_password_hash

def create_user(fullname, email, password,no_hp):
        hashed_password = generate_password_hash(password)
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users (fullname, email, password,no_hp) VALUES (%s, %s, %s,%s)",
                   (fullname, email, hashed_password,no_hp))
        mysql.connection.commit()
        cursor.close()

def get_user_by_email(email):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()
        return user

def tambah_donasi(jumlah_donasi,nama,pesan,user_id):
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO donasi (jumlah_donasi, nama, pesan,user_id) VALUES (%s, %s, %s,%s)",
                   (jumlah_donasi, nama, pesan,user_id))
        mysql.connection.commit()
        cursor.close()

def get_user_donasi(user_id):
        cursor = mysql.connection.cursor()
        cursor.execute("""
                SELECT *
        FROM donasi d
        JOIN users u ON u.user_id = d.user_id
        WHERE u.user_id = %s
        """, (user_id,))
        donasi = cursor.fetchall()
        cursor.close()
        return donasi

def verify_password(hashed_password, password):
        return check_password_hash(hashed_password, password)

