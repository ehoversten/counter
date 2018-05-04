# ------------------------------------------------------------------------------/
#   Assignment: Counter
#       Objectives:
#          Practice using session to store data about a particular client's history with the app
#          Be able to check whether a session exists
#          Be able to initialize a session
#          Be able to modify a session
#
# ------------------------------------------------------------------------------/

from flask import Flask, render_template, redirect, session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__=="__main__":

    app.run(debug=True)
