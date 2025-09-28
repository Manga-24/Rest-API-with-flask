from flask import Flask, request, jsonify

app = Flask(__name__)

# [cite_start]The task hints to store users in a dictionary or in-memory list[cite: 9].
users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"}
}
next_id = 3

# [cite_start]The task requires GET/POST/PUT/DELETE routes[cite: 6].
# This route handles GET requests to retrieve all users.
@app.route("/users", methods=["GET"])
def get_users():
    """Returns all users."""
    return jsonify(list(users.values()))

# This route handles GET requests for a specific user.
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    """Returns a single user by ID."""
    user = users.get(user_id)
    # [cite_start]The task mentions status codes like 200 and 404[cite: 18].
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# This route handles POST requests to create a new user.
@app.route("/users", methods=["POST"])
def create_user():
    """Creates a new user."""
    global next_id
    # [cite_start]The task asks what request.json is[cite: 17]. It's used here to get the JSON data.
    data = request.json
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Invalid user data"}), 400
    
    new_user = {"name": data["name"], "email": data["email"]}
    users[next_id] = new_user
    next_id += 1
    return jsonify(new_user), 201

# This route handles PUT requests to update a user.
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    """Updates an existing user."""
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    data = request.json
    if "name" in data:
        user["name"] = data["name"]
    if "email" in data:
        user["email"] = data["email"]
        
    return jsonify(user)

# This route handles DELETE requests to remove a user.
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """Deletes a user."""
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404

# This block allows the app to be run directly.
# [cite_start]The task asks how to run a Flask app[cite: 19].
if __name__ == "__main__":
    app.run(debug=True)