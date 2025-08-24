from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Shivashish"},
    {"id": 2, "name": "Lovely"},
]

"""
GET, POST, PUT, DELETE
"""


@app.route("/")
def homepage():
    return render_template("index.html")


# get all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)


# Delete, Get, Put operation
@app.route("/users/<int:user_id>", methods=["GET", "DELETE", "PUT"])
def user_operations(user_id):
    if request.method == "GET":
        for user in users:
            if user["id"] == user_id:
                return jsonify(user)
        return jsonify({"Error": "User not found"}), 404

    if request.method == "DELETE":
        for user in users:
            if user["id"] == user_id:
                users.remove(user)
                return jsonify({"Message": "User deleted"})
        return jsonify({"Error": "User not found"}), 404

    if request.method == "PUT":
        data = request.get_json()
        for user in users:
            if user["id"] == user_id:
                user["name"] = data.get("name", user["name"])
                return jsonify(user)
    return jsonify({"Error": "User not found"})


# post a new user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()  # read json data sent by client
    new_user = {
        "id": len(users) + 1,  # make a new id
        "name": data.get("name"),  # get the name from request
    }
    users.append(new_user)
    return jsonify(users), 201


if __name__ == "__main__":
    app.run(debug=True, port=5000)
