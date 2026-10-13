from flask import Flask,redirect,url_for
### this simply create wsgi application 
app= Flask(__name__)

@app.route('/')
def welcome():
    return'Welcome to my youtube channel'




@app.route('/members')
def members():
    return'welcome to my world'

@app.route('/Pass/<int:score>')
def passed(score):
    return f"you have passed with score {score}"
@app.route('/failed/<int:score>')
def failed(score):
    return f"you have failed with score {score}"

"""
jab hume success pe ya fir failure pe hum simply url banana hota hai 
to hum redirect ka use karte uske saat url banane ke liye hum url_for ka use karte hai simply
"""
@app.route('/results/<int:score>')
def result(score):
    result=''
    if score<35:
        result="failed"
    else:
        result="Pass"
    return redirect(url_for(result,score=score))

if __name__=='__main__':
    app.run(debug=True)