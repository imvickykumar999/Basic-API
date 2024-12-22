
># `Deployed CRUD`:
>
>![image](https://github.com/user-attachments/assets/c57c884e-43eb-4fcf-bd17-a656a2d45552)

- PUT is used to update an existing resource with a new version. It typically requires the entire resource data to be sent in the request.

```py
if not name or not email:
	return jsonify({"error": "Name and email are required!"}), 400
```

- PATCH is used to make partial updates to an existing resource. It only requires the fields that need to be updated to be sent in the request.

```py
if not name and not email:
	return jsonify({"error": "At least one field (name or email) is required!"}), 400
```
