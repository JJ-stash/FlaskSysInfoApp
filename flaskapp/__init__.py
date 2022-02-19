from flask import Flask, render_template
from flaskapp.getAll import *

app = Flask(__name__)

@app.route("/")
def first():
	sys_data = getAll()
	return render_template('/one.html', sys_data = sys_data, title = 'Root')

@app.route("/ps")
def second():
	ps_data = getAll()['Procs']
	return render_template('/two.html', ps_data = ps_data, title = 'PS')