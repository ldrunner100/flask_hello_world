from flask import Flask
from os import environ

app = Flask(__name__)

#@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"

@app.route("/hello/<name>")
def hi_person(name):
    return "Hello {}!".format(name.title())

@app.route("/hello/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())
    
@app.route("/hello/<fname>/<lname>")
def jedi_name(fname, lname):
    jd_nm = lname[0:2] + fname[0:1]
    html = """
    <h1>
        Hello {} {}!
    </h1>
    <p>
        Your Jedi name shall forever be : 
    </p>
    
    <h1>
        {}!
    </h1>
    """
    return html.format(fname.title(), lname.title(), jd_nm.title())
    
if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))