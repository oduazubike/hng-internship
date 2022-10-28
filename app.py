from flask import Flask, jsonify

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "super-secret"


@app.route("/user", methods=["GET"])
def user():
    user_dict = {
        "slackUsername": "zubic",
        "backend": True,
        "age": 26,
        "bio": "I am a passionate developer with never ending desire to learn and work. "
               "I develop Rest APIs and Web Applications backend"
    }

    return jsonify(user_dict)


if __name__ == "__main__":
    app.run(debug=True)