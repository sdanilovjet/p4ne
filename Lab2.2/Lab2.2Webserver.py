from flask import Flask,jsonify
import sys


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Справка об использовании"


@app.route('/python')
def python_page():
    return jsonify(repr(sys.__dict__))



#@app.route('/configs')
#def configs_page():



#@app.route('/config/hostname')
#def hostname_page():



if __name__=='__main__':
    app.run(debug=True)


