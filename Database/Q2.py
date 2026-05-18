import sqlite3;
conn=sqlite3.connect("hello.db");
cur=conn.cursor();
# cur.execute("insert into products values(102,'mobile',5000,5)");
cur.execute("update products set name='Laptop',price=500 where id =102")
conn.commit();
print("data Inserted SUCESSFULLY");
conn.close();