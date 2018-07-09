from flask import Flask,render_template,url_for,request
import sqlite3
app=Flask(__name__)

@app.route('/')
@app.route('/home')
def homepage():
  return render_template("homepage.html")

@app.route('/admin.html')
def Admin():
  return render_template("admin.html")

@app.route('/keeper.html')
def keeper():
  return render_template("keeper.html")

@app.route('/user.html')
def user():
  return render_template("user.html")

@app.route('/adduser?')
def createUserReq():
  return render_template("createUser.html")


@app.route('/admincrud',methods=['GET','POST'])
def Admincrud():
  user=request.form['username']
  passw=request.form['password']
  conn=sqlite3.connect('Database.db')
  c=conn.cursor()
  c.execute("select password from authentication where username=?",(user,) )
  row=c.fetchall()

  if row[0][0]==passw:
  	return render_template("admincrud.html")  
  else:
    return render_template("error.html")  	

@app.route('/removeUser',methods=['GET','POST'])
def remUser():
	return render_template("removeUser.html")

@app.route('/removeUserFin',methods=['GET','POST'])
def rem1User():
  conn=sqlite3.connect('Database.db')
  c=conn.cursor()
  cid = request.form['c_id']
  c.execute("DELETE FROM cust WHERE c_id=?",(cid,))
  conn.commit()
  c.close()
  conn.close()
  return ("SUCCESSFULLY DELETED!")

@app.route('/removeBookFin',methods=['GET','POST'])
def remBook():
  conn=sqlite3.connect('Database.db')
  c=conn.cursor()
  cid = request.form['b_id']
  c.execute("DELETE FROM bstore WHERE b_id=?",(cid,))
  conn.commit()
  c.close()
  conn.close()
  return ("SUCCESSFULLY DELETED!")


@app.route('/removeBook',methods=['GET','POST'])
def remBookReq():
	return render_template("removeBook.html")


@app.route('/createBook',methods=['GET','POST'])
def createBook():
	return render_template("addBook.html")

@app.route('/addBook', methods=['GET','POST'])
def addBook():
  conn=sqlite3.connect('Database.db')
  c=conn.cursor()
  bid=request.form['b_id']
  bname=request.form['b_name']
  auth=request.form['author_name']
  #purchased=request.form['ratings']
  count=request.form['book_count']
  pr=request.form['price']
  c.execute("INSERT INTO bstore( b_id ,b_name ,author_name ,ratings,book_count ,price) values (?,?,?,?,?,?)",(bid,bname,auth,'',count,pr))
  conn.commit()
  c.close()
  return render_template("status.html")


@app.route('/createUser',methods=['GET','POST'])
def createUser():
  	conn=sqlite3.connect('Database.db')
  	c=conn.cursor()
  	idm=request.form['c_id']
  	name=request.form['c_name']
  	password=request.form['c_pword']
  	purchased=request.form['c_purchased']
  	email=request.form['c_email']
  	category=request.form['c_cat']
  	c.execute("INSERT INTO cust( c_id ,c_name ,c_pword ,c_purchased,c_email ,c_cat) values (?,?,?,?,?,?)",(idm,name,password,purchased,email,category))
  	#row=c.fetchall()
  	conn.commit()
  	c.close()
  	return render_template("status.html")
if __name__=="__main__":
  app.run(debug=True)
