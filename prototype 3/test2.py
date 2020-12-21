import sqlite3
conn = sqlite3.connect('image.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS my_table (name TEXT, data BLOB)
""")
conn.commit()
conn.close()
conn.close()