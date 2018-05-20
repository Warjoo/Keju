from flask import Flask,request
from peneliti import namapeneliti as nmpl
app = Flask(__name__)

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

@app.route('/peneliti/<A>')
def home(A):
	return nmpl.hom(A)

@app.route('/peneliti/<B>')
def home(B):
	return nmpl.hom(B)

@app.route('/peneliti/<C>')
def home(C):
	return nmpl.hom(C)

@app.route('/peneliti/<D>')
def home(D):
	return nmpl.hom(D)
