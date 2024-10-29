import mysql.connector

host = "localhost"
user = "foydalanuvchi"
parol = "parol"
malumotlar_bazasi = "sys"

connection = mysql.connector.connect(
    host=host,
    user=user,
    password=parol,
    database=malumotlar_bazasi
)

cursor = connection.cursor()

jadval_yaratish = """
CREATE TABLE IF NOT EXISTS Kategoriyalar (
    id INT AUTO_INCREMENT PRIMARY KEY,
    kategoriya_nomi VARCHAR(100) NOT NULL,
    tavsif TEXT,
    yaratilgan_vaqt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""
cursor.execute(jadval_yaratish)
print("Kategoriyalar jadvali yaratildi yoki mavjud.")

malumotlar_qoshish = """
INSERT INTO Kategoriyalar (kategoriya_nomi, tavsif) VALUES (%s, %s);
"""
kategoriyalar = [
    ('Dasturlash', 'Dasturchi'),
    ('Dizayn', 'Dizayner'),
    ('Marketing', 'Marketolog yoki SMM')
]
cursor.executemany(malumotlar_qoshish, kategoriyalar)
connection.commit()
print("Ma'lumotlar jadvalga qo'shildi.")

tanlash_sorovi = "SELECT * FROM Kategoriyalar;"
cursor.execute(tanlash_sorovi)
kategoriyalar = cursor.fetchall()

for kategoriya in kategoriyalar:
    print(f"ID: {kategoriya[0]}, Nomi: {kategoriya[1]}, Tavsif: {kategoriya[2]}, Yaratilgan vaqt: {kategoriya[3]}")

cursor.close()
connection.close()