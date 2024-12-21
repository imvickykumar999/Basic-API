# `Postman Collection`

```json
{
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
```

You can import it into Postman to interact with your Flask API. Here's how to use it:

### Steps to Import Postman Collection
1. **Open Postman**:
   - Launch the Postman application on your system.

2. **Import the Collection**:
   - Click on the "Import" button in the top-left corner.
   - Choose the "Raw Text" option or paste the JSON content into the import box.
   - Alternatively, save the JSON content as a `.json` file (e.g., `collection.json`) and upload it in the "Import" window.

3. **Collection Details**:
   - After importing, you will see a collection named `LocalHost` with the following requests:
     - **`GetAll`**: Fetches all user IDs.
     - **`GetByID`**: Fetches data for a specific user ID (replace the hardcoded ID in the URL with the desired one).
     - **`Post`**: Submits data (`name` and `email`).

4. **Run the Requests**:
   - Open each request and click the "Send" button to test the API.

### Notes:
- For the `GetByID` request, ensure to replace the `user_id` in the path with an actual `user_id` returned from the `Post` request.
- You can modify the `Post` request's form-data values (`name` and `email`) as needed to test with different inputs.

This setup enables seamless testing of your Flask API using Postman. Let me know if you need further assistance!
