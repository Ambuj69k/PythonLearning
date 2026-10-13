## building url dynamically 
## variable rules and url binding

from flask import Flask

app=Flask(__name__)

@app.route('/')
def welcome():
    return 'welcome to my work folks'

if __name__=='main':
    app.run(debug=True)