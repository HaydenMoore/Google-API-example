#!/usr/bin/python

#import flask library
from flask import Flask, render_template

#create app object
app = Flask(__name__)

#define routes
@app.route('/')
def run():
    return render_template('index.html')

#run server
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8003, passthrough_errors=True)