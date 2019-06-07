from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = '66634234'


@app.route("/")
def count():
    print("page viewed")
    if 'count' in session:
        print('key exists!')
        session['count'] += 1

    else:
        print("key 'key_name' does NOT exist")
        session['count'] = 1

    return render_template("index.html")

@app.route("/destroy_session")
def reset():
    session.clear()		# clears all keys
    session.pop('count', None)
    return redirect("/")		

if __name__=="__main__":
    app.run(debug=True)