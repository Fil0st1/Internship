from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage
users = {}

# Get all users
@app.get("/users")
def get_users():
    return jsonify(users)

# Get specific user
@app.get("/users/<user_id>")
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

# Create user
@app.post("/users")
def create_user():
    data = request.json
    user_id = data.get("id")
    if user_id in users:
        return jsonify({"error": "User already exists"}), 400

    users[user_id] = {"name": data.get("name"), "age": data.get("age")}
    return jsonify({"message": "User created"}), 201

# Update user
@app.put("/users/<user_id>")
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    users[user_id].update(data)
    return jsonify({"message": "User updated"})

# Delete user
@app.delete("/users/<user_id>")
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    del users[user_id]
    return jsonify({"message": "User deleted"})

if __name__ == "__main__":
    app.run(debug=True)
