# API Documentation with Cookie Management

This API requires authentication using a login mechanism. Cookies are used to manage the user session, and they must be passed with subsequent requests to authenticated endpoints.

---

## Authentication

### Login
**Method:** `POST`  
**URL:** `/login`  
**Description:** Authenticates the user and creates a session. Cookies will be returned in the response and must be saved for subsequent requests.  
**Request Parameters:**  
- `username` (required): The username.  
- `password` (required): The password.  

**Example cURL:**
```bash
curl -X POST -c cookies.txt http://127.0.0.1:5000/login -d "username=admin" -d "password=password123"
```

**Response:**
```json
{
  "message": "Login successful!"
}
```

- The `-c cookies.txt` option saves the cookies (including the session cookie) to a file named `cookies.txt`.

---

### Logout
**Method:** `POST`  
**URL:** `/logout`  
**Description:** Logs out the user and clears the session.  

**Example cURL:**
```bash
curl -X POST -b cookies.txt http://127.0.0.1:5000/logout
```

**Response:**
```json
{
  "message": "Logged out successfully!"
}
```

- The `-b cookies.txt` option sends the stored cookies with the request to authenticate the logout operation.

---

## User Management Endpoints

### List All User IDs
**Method:** `GET`  
**URL:** `/`  
**Description:** Lists all user IDs with their access paths.  

**Example cURL:**
```bash
curl -X GET -b cookies.txt http://127.0.0.1:5000/
```

**Response:**
```json
{
  "ids": ["/get/1", "/get/2"]
}
```

---

### Create User
**Method:** `POST`  
**URL:** `/post/`  
**Description:** Adds a new user to the database.  
**Request Parameters:**  
- `name` (required): The user's name.  
- `email` (required): The user's email.  

**Example cURL:**
```bash
curl -X POST -b cookies.txt http://127.0.0.1:5000/post/ -d "name=John Doe" -d "email=johndoe@example.com"
```

**Response:**
```json
{
  "message": "Data submitted successfully!",
  "user_id": 1,
  "data": {
    "name": "John Doe",
    "email": "johndoe@example.com"
  }
}
```

---

### Retrieve User by ID
**Method:** `GET`  
**URL:** `/get/<user_id>`  
**Description:** Retrieves the data of a user by their ID.  

**Example cURL:**
```bash
curl -X GET -b cookies.txt http://127.0.0.1:5000/get/1
```

**Response:**
```json
{
  "message": "User data retrieved successfully!",
  "data": {
    "name": "John Doe",
    "email": "johndoe@example.com"
  }
}
```

---

### Update User
**Method:** `PUT`  
**URL:** `/update/<user_id>`  
**Description:** Updates the user's data entirely.  
**Request Parameters:**  
- `name` (required): The updated name.  
- `email` (required): The updated email.  

**Example cURL:**
```bash
curl -X PUT -b cookies.txt http://127.0.0.1:5000/update/1 -d "name=Jane Doe" -d "email=janedoe@example.com"
```

**Response:**
```json
{
  "message": "User data updated successfully!",
  "data": {
    "name": "Jane Doe",
    "email": "janedoe@example.com"
  }
}
```

---

### Partially Update User
**Method:** `PATCH`  
**URL:** `/patch/<user_id>`  
**Description:** Updates one or more fields of the user's data.  
**Request Parameters (optional):**  
- `name`: The updated name.  
- `email`: The updated email.  

**Example cURL:**
```bash
curl -X PATCH -b cookies.txt http://127.0.0.1:5000/patch/1 -d "email=newemail@example.com"
```

**Response:**
```json
{
  "message": "User data updated successfully!",
  "data": {
    "name": "Jane Doe",
    "email": "newemail@example.com"
  }
}
```

---

### Delete User
**Method:** `DELETE`  
**URL:** `/delete/<user_id>`  
**Description:** Deletes the user's data by ID.  

**Example cURL:**
```bash
curl -X DELETE -b cookies.txt http://127.0.0.1:5000/delete/1
```

**Response:**
```json
{
  "message": "User data deleted successfully!"
}
```

---

## Notes
1. **Authentication Required:** All routes except `/login` and `/logout` require the user to be logged in.
2. **Cookie Handling:** Use `-c` to save cookies and `-b` to pass them in subsequent requests.
3. **Session Management:** Ensure cookies are used properly to maintain the session across requests.
4. **Security:** Use HTTPS in production to secure cookie transmission.
