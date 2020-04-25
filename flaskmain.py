from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    return "<h1>hello world</h1>"

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/user")
def user():
    return "<h1>Profile page</h1>"

@app.errorhandler(404)
def page_not_found(e):
    return "<h2>Page not found</h2>",404

@app.errorhandler(500) 
def internal_server_error(e):    
    return "<h1>Internal server error</h1>", 500

if __name__=='__main__':
    app.run(debug=True)