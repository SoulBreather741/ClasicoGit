import dataset
import sqlalchemy
import time
db = dataset.connect('postgres://gekfeekpdeldpr:b9aeb07051bb27207f972128b045e2e0a2a20b07be2d2c86147914fe538b7043@ec2-54-204-32-145.compute-1.amazonaws.com:5432/dchaerkmjsv0dn', engine_kwargs={'poolclass':sqlalchemy.pool.NullPool})

def signup(name, code, phonenumber, firsthalfB,firsthalfR, secondhalfB,secondhalfR,finalB,finalR,corner):
	table = db["users"]
	entry = {"name": name, "code" : code, "phonenumber" : phonenumber, "firsthalfB" : firsthalfB,"firsthalfR":firsthalfR, "secondhalfB" : secondhalfB,"secondhalfR":secondhalfR,"finalB":finalB,"finalR":finalR,"corner":corner }
	generatedid = table.insert(entry)
	if generatedid > 0:
		return True
	return False

def getUserByCode(code):
	table = db["users"]
	user = table.find_one(code=code)
	return user

def allUsers():
	table = db['users']
	return table.all()

def delete(code):
	table = db['users']
	table.delete(code=code)
