from flask import Flask           # import flask
app = Flask(__name__)             # create an app instance
i1=0

@app.route("/")                   # at the end point /
def hello():
    str1 ="helll"+i1                      # call method hello
    return str1         # which returns "hello world"

if __name__ == "__main__":        # on running python app.py
    app.run()  