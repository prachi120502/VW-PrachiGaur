from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    username = request.cookies.get("username")
    visit_count = request.cookies.get("visit_count")

    if visit_count:
        visit_count = int(visit_count)
    else:
        visit_count = 0

    if request.method == "POST":
        username = request.form.get("username")

    if request.method == "GET":
        visit_count += 1

    response = make_response(
        render_template("index.html", username=username, visit_count=visit_count)
    )

    if username:
        response.set_cookie("username", username)

    response.set_cookie("visit_count", str(visit_count), max_age=60*60*24)

    return response


if __name__ == "__main__":
    app.run(debug=True)