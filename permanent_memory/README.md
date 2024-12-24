# API Documentation

## Base URL
`https://vickscrudapi.pythonanywhere.com`

---

## Methods

### 1. POST Method
Use this method to create a new user record.

**Endpoint:**
`/post/`

**Request:**
```bash
curl -X POST https://vickscrudapi.pythonanywhere.com/post/ \
-d "name=John Doe" \
-d "email=johndoe@example.com"
```

**Parameters:**
- `name` (string): The name of the user.
- `email` (string): The email address of the user.

---

### 2. GET Method
Retrieve all user records.

**Endpoint:**
`/`

**Request:**
```bash
curl -X GET https://vickscrudapi.pythonanywhere.com/
```

---

### 3. UPDATE Method
Update an existing user record by ID.

**Endpoint:**
`/update/<id>`

**Request:**
```bash
curl -X PUT https://vickscrudapi.pythonanywhere.com/update/1 \
-d "name=Jane Doe" \
-d "email=janedoe@example.com"
```

**Parameters:**
- `name` (string): The updated name of the user.
- `email` (string): The updated email address of the user.

---

### 4. GET by ID Method
Retrieve a user record by its ID.

**Endpoint:**
`/get/<id>`

**Request:**
```bash
curl -X GET https://vickscrudapi.pythonanywhere.com/get/1
```

---

### 5. PATCH Method
Partially update a user record by ID.

**Endpoint:**
`/patch/<id>`

**Request:**
```bash
curl -X PATCH https://vickscrudapi.pythonanywhere.com/patch/1 \
-d "email=newemail@example.com"
```

**Parameters:**
- `email` (string): The new email address of the user.

---

## Notes
- Replace `<id>` with the actual user ID you want to access or update.
- Ensure the required parameters are provided for each method.
- The API uses standard HTTP status codes to indicate success or errors.
