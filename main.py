from flask import Flask, render_template, redirect, url_for
from forms import LoginForm  # Import the form you created

app = Flask(__name__)
app.secret_key = "some secret string"  # Needed for CSRF protection


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():  # Check if the form is submitted and valid
        # Here you would typically handle the validated form data
        return redirect(url_for('home'))  # Redirect to home after submit
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)

