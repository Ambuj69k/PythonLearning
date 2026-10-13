### integrate html with flask
### http verb get and post simpy 
"""
is poore section me hum simply ye sikhenge ki html 
file kaise render karte hai instead of writing whole html
file in route it self
ek aur chij hai agar posted value ko read karne ke liye kuch karna hota hai
hum request library import karte hai simply
"""

from flask import Flask,redirect,url_for,render_template
from flask import request

app=Flask(__name__)

@app.route('/')
def welcome():
   return render_template('index.html')
"""yaha par humne kya kiya simply render_template ka use karke apni html file ko
simply call kar liya
"""



@app.route('/submit',methods=['POST','GET'])
def submit():
    result=''
    if request.method=='POST':
          science=float(request.form['science'])
          hindi=float(request.form['hindi'])
          english=float(request.form['english'])
          maths=float(request.form['maths'])
          average=(science+hindi+english+maths)/4

          if average>35:
             result='passed'
             return redirect(url_for(result,score=int(average)))
          else:
             result='failed'
             return redirect(url_for(result,score=int(average)))


@app.route('/pass/<int:score>')
def passed(score):
    return render_template('pass.html',score=score)

@app.route('/fail/<int:score>')
def failed(score):
    return render_template('fail.html',score=score)

if __name__=='__main__':
    app.run(debug=True)