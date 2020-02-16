from flask import Flask, render_template, request,redirect
import db

app = Flask(__name__)
app.secret_key = "'drtrjndfhdfhb45y3478hbdfe4t84hhudh78dre8t8yefy87erhbfudydsytreuyueruy777748fhdfuyg78h'"


@app.route('/')
def index():
	return render_template('index.html')

@app.route("/", methods=['POST','GET'])
def SigninForm():
	if request.method == 'POST':
		form = request.form
		name = form['name']
		code = form['code']
		phonenumber = form['phonenumber']
		firsthalfB = form['firsthalfB']
		firsthalfR = form['firsthalfR']
		secondhalfB = form['secondhalfB']
		secondhalfR = form['secondhalfR']
		finalB=form['finalB']
		finalR=form['finalR']
		corner=form['corner']
		user = db.getUserByCode(code)
		if(user != None):
			db.delete(code)
			db.signup(name,code,phonenumber,firsthalfB,firsthalfR,secondhalfB,secondhalfR,finalB,finalR,corner)
			return render_template('success.html')
		if(user == None):
			return render_template('cdexist.html')
		
		return "something went wrong"

@app.route("/showall")
def showall():
	allusers = db.allUsers()
	userlist = list(allusers)
	return render_template("showall.html", users = userlist)

@app.route("/showall", methods=['POST','GET'])
def showall_del():
	if request.method == 'POST':
		form = request.form
		code = form['code']
		user = db.getUserByCode(code)
		if(user != None):
			db.delete(code)
			return redirect('/showall')
		
		
		return "something went wrong"


@app.route("/admin")
def adminFares():
	return render_template("admin.html")

@app.route("/admin", methods=['POST','GET'])
def admin():
	if request.method == 'POST':
		form = request.form
		code = form['code']
		user=db.getUserByCode(code)
		if(user != None):
			return render_template('codexist.html')
		if(db.signup(None,code,None,None,None,None,None,None,None,None)):
			return render_template('admin.html')
		return "something went wrong"

if __name__ == '__main__':
	app.run(debug=True)