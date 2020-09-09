from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key='secret'

@app.route('/')
def counter():
    if 'counter' not in session:
        session['counter']=1
    else:
        session['counter']+=1
    if 'actual' not in session:
        session['actual']=1
    else:
        session['actual']+=1
    return render_template("index.html")

@app.route("/add")
def add():
    session['counter']+=2
    return redirect("/")

@app.route("/clear")
def destroy_session():
    session.pop('counter')
    return redirect("/")

@app.route("/youdoyou", methods=['POST'])
def choose_number():
    session['counter']+=int(request.form['number'])
    return redirect("/")

if __name__ =="__main__":
    app.run(debug=True)