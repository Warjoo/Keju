from flask import Flask,request,jsonify
from peneliti import namapeneliti as nmpl
import scholarly,json
from flask_mysqldb import MySQL 
import pymysql

db = pymysql.connect("localhost", "root", "", "affiliasicitedby")

app = Flask(__name__)
mysql = MySQL(app)

@app.route('/<gurih>')
def hello_world(gurih):
    return gurih

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/crot', methods=['POST'])
def login():
	return request.form['anu']

@app.route('/peneliti/<Rutgers>',methods=['POST'])
def coba(Rutgers):
		search_query = scholarly.search_author('Rutgers')
		return str(next(search_query))

@app.route('/aff')
def bisa():
	cursor = db.cursor()
	sql = "SELECT * FROM searchpost"
	cursor.execute(sql)
	results = cursor.fetchall()
	return str(results)



