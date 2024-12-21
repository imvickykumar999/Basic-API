from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory database
database = {}

# Route to list all user IDs
@app.route('/')
def list_ids():
    return jsonify({"ids": list(database.keys())})

# Route to handle POST request
@app.route('/post/', methods=['POST'])
def submit():
    # Get data from the form
    name = request.form.get('name')
    email = request.form.get('email')

    if not name or not email:
        return jsonify({"error": "Name and email are required!"}), 400

    # Generate a unique ID and save the data
    user_id = str(uuid.uuid4())
    database[user_id] = {"name": name, "email": email}

    return jsonify({
        "message": "Data submitted successfully!",
        "user_id": user_id,
        "data": {
            "name": name,
            "email": email
        }
    })

# Route to retrieve data by ID
@app.route('/get/<user_id>', methods=['GET'])
def get_user(user_id):
    user_data = database.get(user_id)
    if not user_data:
        return jsonify({"error": "User not found!"}), 404

    return jsonify({
        "message": "User data retrieved successfully!",
        "data": user_data
    })

if __name__ == '__main__':
    app.run(debug=True)
