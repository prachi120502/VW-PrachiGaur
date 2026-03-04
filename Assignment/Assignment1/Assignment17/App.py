from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("form.html")


@app.route("/submit", methods=["POST"])
def submit():

    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    error = None

    # Validation 1: Empty fields
    if not name or not email or not password:
        error = "Fields should not be blank"

    # Validation 2: Email must contain @
    elif "@" not in email:
        error = "Email should contain @ symbol"

    # Validation 3: Password length
    elif len(password) < 5 or len(password) > 8:
        error = "Password must be between 5 and 8 characters"

    if error:
        return render_template("form.html", error=error)

    return render_template("show.html", name=name, email=email)


if __name__ == "__main__":
    app.run(debug=True)