from flask import Flask,request,Response,jsonify
from peneliti import namapeneliti as nmpl
import scholarly.json

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

@app.route('/peneliti/<Chris>', methods=[POST])
def Coba(Chris)
    return str(nmpl.C(Chris))
@app.route('/peneliti/<Juliffer>', methods=[POST])
def Coba1(Juliffer)
    return str(nmpl.D(Juliffer))
@app.route('/peneliti/<Roza>', methods=[POST])
def Coba2(Roza)
    return str(nmpl.E(Roza))
@app.route('/peneliti/<Manish Singh>', methods=[POST])
def Coba3(Manish Singh)
    return str(nmpl.A(Manish Singh))
@app.route('/peneliti/<Oussama Khatib>', methods=[POST])
def Coba4(Oussama Khatib)
    return str(nmpl.B(Oussama Khatib))
