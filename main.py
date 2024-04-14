from flask import Flask, render_template, redirect, url_for
from forms import LoginForm

app = Flask(__name__)
app.secret_key = "some secret string"


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
