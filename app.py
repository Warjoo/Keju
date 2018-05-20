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
def home(E):
	return nmpl.hom(A)

@app.route('/peneliti/<B>')
def home(F):
	return nmpl.hom(B)

@app.route('/peneliti/<C>')
def home(G):
	return nmpl.hom(C)

@app.route('/peneliti/<D>')
def home(H):
	return nmpl.hom(D)
