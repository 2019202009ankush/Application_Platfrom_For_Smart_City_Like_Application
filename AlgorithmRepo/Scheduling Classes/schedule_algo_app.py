from flask import Flask, redirect, url_for ,render_template,request
# from test import i,name,age
from scheduling_algo import tststr

# print(i)

output={}
app = Flask(__name__)

@app.route("/schedule")

def dashboard():
	return render_template("schedule_algo_ui.html",tststr=tststr)


if __name__ == "__main__":
    app.run(port=5555, debug=True)