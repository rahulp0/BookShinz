
import sqlite3

con = sqlite3.connect("Database.db")

cur = con.cursor()
#cur.execute("CREATE TABLE IF NOT EXISTS b_img(img_name BLOB")
cur.execute("CREATE TABLE IF NOT EXISTS keeper( k_id varchar(35) PRIMARY KEY, k_pword VARCHAR(12))")
cur.execute("CREATE TABLE IF NOT EXISTS cust( c_id varchar(35) PRIMARY KEY, c_pword VARCHAR (12), c_name VARCHAR (45),c_purchased INTEGER,c_email VARCHAR (40),c_cat VARCHAR (10) ) ")
cur.execute("CREATE TABLE IF NOT EXISTS bstore( b_id BIGINT PRIMARY KEY,b_name VARCHAR (35),author_name VARCHAR(30),ratings FLOAT,book_count INTEGER, price double)")
cur.execute("CREATE TABLE IF NOT EXISTS authentication ( username varchar(35) PRIMARY KEY, password VARCHAR (12))")
#cur.execute('insert into b_img(id, name, bin) values (?,?,?)', (id, name, sqlite3.Binary(file.read())))
#
cur.execute("CREATE TABLE IF NOT EXISTS reviews ( review TEXT,c_id varchar(35) ,b_id BIGINT, FOREIGN KEY (c_id) REFERENCES cust(c_id),FOREIGN KEY (b_id) REFERENCES bstore(b_id))")


v1=1000
p1=99.99
v2='12345' 
v0=101
s1 = 'Introduction to some shinz '
g0 = 'Galileo'
c1=9
for i in range (0,5):
	cur.execute("INSERT INTO bstore( b_id ,b_name ,author_name ,ratings,book_count ,price) values (?,?,?,?,?,?)",(v1,s1,g0,'',c1,p1))
	v0 +=1
	p1+=100
	v1+=1
	v2 += '+'
	g0+='+'
	s1 = s1+str(v0)
cur.execute("INSERT INTO authentication ( username , password ) VALUES (?,?)",('admi1','pword'))
cur.execute("INSERT INTO keeper ( k_id , k_pword ) VALUES (?,?)",('admin','pword'))
cur.execute("INSERT INTO cust ( c_id , c_pword , c_name ,c_purchased ,c_email ,c_cat ) VALUES (?,?,?,?,?,?)",('rahul','pword','RAHUL PRAKASH',17,'rah@fmail.com','Gold'))


con.commit()
cur.close()
con.close()