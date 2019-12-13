#!/usr/bin/env python

import os
from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



@app.route("/")
def helloQuantum():
    return "hello Quantum"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 3000), debug=True)
