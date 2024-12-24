from flask import Flask, request, jsonify, session
from functools import wraps
import sqlite3, secrets

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True  # Enable pretty printing for JSON

app.secret_key = secrets.token_hex(32)  # 32 bytes for a secure key
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

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
# @login_required
def list_ids():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM users')
    ids = [row[0] for row in cursor.fetchall()]
    conn.close()
    return jsonify({"ids": ids})

@app.route('/post/', methods=['POST'])
@login_required
def submit():
    name = request.form.get('name')
    email = request.form.get('email')

    if not name or not email:
        return jsonify({"error": "Name and email are required!"}), 400

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    user_id = cursor.lastrowid
    conn.commit()
    conn.close()

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
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, email FROM users WHERE id = ?', (user_id,))
    user_data = cursor.fetchone()
    conn.close()

    if not user_data:
        return jsonify({"error": "User not found!"}), 404

    return jsonify({"name": user_data[0], "email": user_data[1]})

@app.route('/update/<int:user_id>', methods=['PUT'])
@login_required
def update_user(user_id):
    name = request.form.get('name')
    email = request.form.get('email')

    if not name or not email:
        return jsonify({"error": "Name and email are required!"}), 400

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET name = ?, email = ? WHERE id = ?', (name, email, user_id))
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return jsonify({"error": "User not found!"}), 404

    return jsonify({"message": "User updated successfully!"})

@app.route('/patch/<int:user_id>', methods=['PATCH'])
@login_required
def patch_user(user_id):
    name = request.form.get('name')
    email = request.form.get('email')

    if not name and not email:
        return jsonify({"error": "At least one of name or email is required!"}), 400

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    if name:
        cursor.execute('UPDATE users SET name = ? WHERE id = ?', (name, user_id))
    if email:
        cursor.execute('UPDATE users SET email = ? WHERE id = ?', (email, user_id))
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return jsonify({"error": "User not found!"}), 404

    return jsonify({"message": "User updated successfully!"})

@app.route('/delete/<int:user_id>', methods=['DELETE'])
@login_required
def delete_user(user_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return jsonify({"error": "User not found!"}), 404

    return jsonify({"message": "User deleted successfully!"})

@app.errorhandler(404)
def not_found_error(error):
    valid_endpoints = {
        rule.rule: list(rule.methods)
        for rule in app.url_map.iter_rules()
        if rule.endpoint != 'static'
    }
    return jsonify({
        "error": "Endpoint not found!",
        "valid_endpoints": valid_endpoints
    }), 404

if __name__ == '__main__':
    app.run(debug=True) # Setting True will enable debug mode
