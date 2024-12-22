from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

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
def list_ids():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM users')
    ids = [row[0] for row in cursor.fetchall()]
    conn.close()
    return jsonify({"ids": ids})

@app.route('/post/', methods=['POST'])
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
def delete_user(user_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return jsonify({"error": "User not found!"}), 404

    return jsonify({"message": "User deleted successfully!"})

if __name__ == '__main__':
    app.run(debug=True) # Setting True will enable debug mode
