# ------------------------------------------------------------------------------/
#   Assignment: Counter
#       Objectives:
#          Practice using session to store data about a particular client's history with the app
#          Be able to check whether a session exists
#          Be able to initialize a session
#          Be able to modify a session
#
# ------------------------------------------------------------------------------/

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = '42'

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    # session['count'] = str(int(session['count']) + 1)
    session['count'] += 1

    return render_template("index.html", count=session['count'])

@app.route('/destroy', methods=['POST'])
def destroy():
    session.clear()
    return redirect('/')

@app.route('/add', methods=['POST'])
def add():
    session['count'] += 1
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)
