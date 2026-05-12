import sqlite3;
conn=sqlite3.connect("hello.db");
cur=conn.cursor();
cur.execute("insert into products values(102,'mobile',5000,5)");
conn.commit();
print("data Inserted SUCESSFULLY");
conn.close();