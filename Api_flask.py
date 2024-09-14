from flask import Flask, jsonify, request, redirect, url_for, make_response, session

# flask CORS
from flask_cors import CORS

app = Flask(__name__)

app.secret_key = "arisha awan key"

# this will enable flask cors for whole application
CORS(app)


@app.route("/get_data/<int:user_id>", methods=["GET"])
def get_data(user_id):

    response = {
        "message": f"send this data{user_id}",
        "data": {
            # query string
            "key1": request.args.get("name", "Arisha"),
            "key2": request.args.get("email", "hashir@email.com"),
        },
    }
    return jsonify(response)


@app.route("/fetch_data", methods=["GET"])
def fetch_data():
    response = get_data()
    data = response.get_json()
    if isinstance(data, dict):
        return response
    return jsonify({"message": "this is a bad request", "data": {}}), 400


@app.route("/post_data", methods=["POST"])
def post_data():

    if not request.get_json():
        return jsonify({"message": "bad request", "data": {}}), 400

        # response={
        #     'mesaage':"data recieved succesfully",
        #     'data':{'key1':'value1','key2':'value2'}
        # }
    return jsonify(request.json), 201


@app.route("/user/<string:username1>")
def profile(username1):
    return f"User: {username1}"


@app.route("/go-to-profile/<username>")
def go_to_profile(username):
    # Use url_for to generate the URL for the profile view
    # username1 this argument name should be match with the
    # argument name of the function in which we are passing
    profile_url = url_for("profile", username1=username)
    #     <body>
    #     <h1>Welcome!</h1>
    #     <p>Go to <a href="{{ url_for('profile', username1='arisha') }}">Arisha's Profile</a></p>
    # </body>
    return redirect(profile_url)


# cookies work here
@app.route("/set_cookie")
def set_cookie():
    resp = make_response("Cookie is set")
    resp.set_cookie(
        "username", "arisha", max_age=60 * 60 * 24
    )  # Set cookie to expire in one day
    resp.set_cookie("email", "arisha@awan")
    return resp


@app.route("/get_cookie")
def get_cookie():
    username = request.cookies.get("username")  # Retrieve the cookie
    email = request.cookies.get("email")
    if username:
        return f"Welcome back, {username} ,,{email}!"
    else:
        return "No cookie found!"


@app.route("/delete_cookie")
def delete_cookie():
    resp = make_response("Cookie has been deleted")
    resp.delete_cookie("username")  # Delete the cookie
    return resp


# sessionnnnnnnn
@app.route("/")
def index():
    # Check if the user is logged in by checking the session
    if "username" in session:
        username = session["username"]
        return f'Logged in as {username} <br><a href="/logout">Logout</a>'
    return 'You are not logged in <br><a href="/login">Login</a>'


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Assume we have a form that submits a 'username' field
        session["username"] = request.form["username"]
        return redirect(url_for("index"))
    return """
        <form method="post">
            <p><input type="text" name="username">
            <p><input type="submit" value="Login">
        </form>
    """


@app.route("/logout")
def logout():
    # Remove the username from the session if it's there
    session.pop("username", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
