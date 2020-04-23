from flask import Flask, redirect, url_for ,render_template,request
# from test import i,name,age

# from ac_temp import run
# import ac_temp

# print(display)
# print(i)


output=None
app = Flask(__name__)

@app.route("/dashboard")

def dashboard():
	file=open("display.txt","r+")
	display=file.read()
	print("out_put 	RECEIVED",display)
	return render_template("ui_ac_control.html",name=display)


if __name__ == "__main__":
    app.run(port=4555, debug=True)