from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm

app=Flask(__name__)
app.config['SECRET_KEY']='15huvd9098sjjikd'

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

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template("register.html",form=form,title="Register")

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.email.data == 'snehagupta@gmail.com' and form.password.data == 'sneha':
        flash('You have been logged in!', 'success')
        return redirect(url_for('home'))
    else:
        flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
    

if __name__=='__main__':
    app.run(debug=True)