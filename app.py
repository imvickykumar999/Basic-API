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

postman = {
	"info": {
		"_postman_id": "227c3640-af0c-454c-917c-e6ab940bd478",
		"name": "LocalHost",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "21359648"
	},
	"item": [
		{
			"name": "GetAll",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:5000",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000"
				}
			},
			"response": []
		},
		{
			"name": "GetByID",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:5000/get/867b5d70-be76-44a6-aa8c-d60c2e5e2a33",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"get",
						"867b5d70-be76-44a6-aa8c-d60c2e5e2a33"
					]
				}
			},
			"response": []
		},
		{
			"name": "Post",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "formdata",
					"formdata": [
						{
							"key": "name",
							"value": "ABC",
							"type": "text"
						},
						{
							"key": "email",
							"value": "xyz@bol7.com",
							"type": "text"
						}
					]
				},
				"url": {
					"raw": "http://127.0.0.1:5000/post/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"post",
						""
					]
				}
			},
			"response": []
		}
	]
}
