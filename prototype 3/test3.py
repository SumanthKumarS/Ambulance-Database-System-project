import sqlite3
conn = sqlite3.connect('image.db')
cursor = conn.cursor()
name = 'sumanth'

with open('images/house.png','rb') as f:
    data = f.read()

cursor.execute("""
INSERT INTO my_table (name,data) VALUES (?,?)
""",(name,data))

m = cursor.execute("""
SELECT * FROM my_table
""")

for x in m:
    rec_data = x[1]
with open('sumanth.png','wb') as f:
    f.write(rec_data)

conn.commit()
conn.close()
conn.close()