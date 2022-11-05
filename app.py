from flask import Flask, jsonify
from flask_restful import reqparse

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


@app.route("/operation", methods=["POST"])
def operation():
    parser = reqparse.RequestParser()
    parser.add_argument('operation_type', type=str)
    parser.add_argument('x', type=int)
    parser.add_argument('y', type=int)

    data = parser.parse_args()
    ope_var = data["operation_type"]
    x_var = data["x"]
    y_var = data["y"]

    addition = ["addition", "add", "Addition", "Add", "+"]
    subtraction = ["subtraction", "Subtract", "subtract", "minus", "Subtraction", "Minus", "-"]
    multiplication = ["Multiplication", "Multiply", "multiply", "multiplication", "*"]

    if ope_var in addition:
        result = x_var + y_var
        resp_dict = {
            "slackUsername": "zubic",
            "result": result,
            "operation_type": "addition"
        }

        return resp_dict, 200

    if ope_var in subtraction:
        result = x_var - y_var
        resp_dict = {
            "slackUsername": "zubic",
            "result": result,
            "operation_type": "subtraction"
        }

        return resp_dict, 200

    if ope_var in multiplication:
        result = x_var * y_var
        resp_dict = {
            "slackUsername": "zubic",
            "result": result,
            "operation_type": "multiplication"
        }

        return resp_dict, 200



if __name__ == "__main__":
    app.run(debug=True)