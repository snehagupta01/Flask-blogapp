from flask import Flask,render_template,url_for

app=Flask(__name__)

posts = [
    {
        'author' : 'sg1',
        'title' : 'tech1',
        'content' : 'abc',
        'date_posted' : 'Apri 25,2020'
    },
    {
        'author': 'sg2',
        'title' : 'tech1',
        'content' : 'abc2',
        'date_posted' : 'Apri 25,2020'
    }
]

@app.route("/")
def index():
    return "<h1>hello world</h1>"

@app.route("/home")
def home():
    return render_template("home.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title="Abt")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

@app.errorhandler(500) 
def internal_server_error(e):    
    return render_template("500.html"),500

if __name__=='__main__':
    app.run(debug=True)