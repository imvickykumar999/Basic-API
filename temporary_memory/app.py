from flask import Flask, request, jsonify, session
from functools import wraps

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Use a secure secret key for sessions

database = {}
next_id = 1  # Initialize the next available ID
users = {"admin": "password123"}  # Dummy credentials for login

# Decorator to enforce login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            return jsonify({"error": "Login required!"}), 401
        return f(*args, **kwargs)
    return decorated_function

# Route to handle login
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required!"}), 400

    if username in users and users[username] == password:
        session['logged_in'] = True
        return jsonify({"message": "Login successful!"})
    else:
        return jsonify({"error": "Invalid credentials!"}), 401

# Route to handle logout
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({"message": "Logged out successfully!"})

@app.route('/')
@login_required
def list_ids():
    return jsonify({"ids": list(database.keys())})

@app.route('/post/', methods=['POST'])
@login_required
def submit():
    global next_id  # Use the global variable
    name = request.form.get('name')
    email = request.form.get('email')

    if not name or not email:
        return jsonify({"error": "Name and email are required!"}), 400

    user_id = next_id
    next_id += 1  # Increment the next available ID
    database[user_id] = {"name": name, "email": email}

    return jsonify({
        "message": "Data submitted successfully!",
        "user_id": user_id,
        "data": {
            "name": name,
            "email": email
        }
    })

@app.route('/get/<int:user_id>', methods=['GET'])
@login_required
def get_user(user_id):
    user_data = database.get(user_id)
    if not user_data:
        return jsonify({"error": "User not found!"}), 404

    return jsonify({
        "message": "User data retrieved successfully!",
        "data": user_data
    })

@app.route('/update/<int:user_id>', methods=['PUT'])
@login_required
def update_user(user_id):
    name = request.form.get('name')
    email = request.form.get('email')

    if not name or not email:
        return jsonify({"error": "Name and email are required!"}), 400

    if user_id not in database:
        return jsonify({"error": "User not found!"}), 404

    database[user_id] = {"name": name, "email": email}

    return jsonify({
        "message": "User data updated successfully!",
        "data": {
            "name": name,
            "email": email
        }
    })

@app.route('/patch/<int:user_id>', methods=['PATCH'])
@login_required
def patch_user(user_id):
    if user_id not in database:
        return jsonify({"error": "User not found!"}), 404

    data = request.form
    name = data.get('name')
    email = data.get('email')

    if not name and not email:
        return jsonify({"error": "At least one field (name or email) is required!"}), 400

    if name:
        database[user_id]['name'] = name
    if email:
        database[user_id]['email'] = email

    return jsonify({
        "message": "User data updated successfully!",
        "data": database[user_id]
    })

@app.route('/delete/<int:user_id>', methods=['DELETE'])
@login_required
def delete_user(user_id):
    if user_id not in database:
        return jsonify({"message": "User not found!"}), 404

    del database[user_id]

    return jsonify({
        "message": "User data deleted successfully!"
    })

if __name__ == '__main__':
    app.run(debug=False)  # Setting False to avoid losing database data
