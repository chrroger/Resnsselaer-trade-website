from flask import Flask, redirect, url_for, render_template, request, session, jsonify, make_response, send_from_directory


app = Flask(__name__)
db = database()
app.secret_key = 'SDD2020FALL'

@app.route('/',methods=["POST", "GET"])
def login():
    # when users enter rin and login
    if request.method == "POST":
        rin = request.form["rin"]
        name = request.form["name"]
    return


@app.route('/home',methods=["POST", "GET"])
def show_home():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run(host="127.0.0.0", port="5000")
