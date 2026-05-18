import sqlite3
conn =sqlite3.connect("hello.db");
cur =conn.cursor();
data=cur.execute("select * from products");
for row in data:
    print(row[0] ," ",row[1]," ",row[2]," ",row[3]);
conn.close();