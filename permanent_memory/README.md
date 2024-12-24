# API Documentation

## Base URL
`https://vickscrudapi.pythonanywhere.com`

---

## Methods

### **Login**
**Endpoint**: `https://vickscrudapi.pythonanywhere.com/login`  
**Method**: `POST`  
**Command**:
```bash
curl -X POST https://vickscrudapi.pythonanywhere.com/login \
     -d "username=admin" \
     -d "password=password123" \
     -c cookies.txt
```
- **`-c cookies.txt`**: Saves session cookies to a file for future authenticated requests.

---

### **Logout**
**Endpoint**: `https://vickscrudapi.pythonanywhere.com/logout`  
**Method**: `POST`  
**Command**:
```bash
curl -X POST https://vickscrudapi.pythonanywhere.com/logout \
     -b cookies.txt
```
- **`-b cookies.txt`**: Sends the saved session cookies for authentication.

---

### **List All User IDs**
**Endpoint**: `https://vickscrudapi.pythonanywhere.com/`  
**Method**: `GET`  
**Command**:
```bash
curl -X GET https://vickscrudapi.pythonanywhere.com/ \
     -b cookies.txt
```

---

### **Submit User Data**
**Endpoint**: `https://vickscrudapi.pythonanywhere.com/post/`  
**Method**: `POST`  
**Command**:
```bash
curl -X POST https://vickscrudapi.pythonanywhere.com/post/ \
     -b cookies.txt \
     -d "name=John Doe" \
     -d "email=johndoe@example.com"
```

---

### **Get User by ID**
**Endpoint**: `https://vickscrudapi.pythonanywhere.com/get/<user_id>`  
**Method**: `GET`  
**Command**:
```bash
curl -X GET https://vickscrudapi.pythonanywhere.com/get/1 \
     -b cookies.txt
```

---

### **Update User**
**Endpoint**: `https://vickscrudapi.pythonanywhere.com/update/<user_id>`  
**Method**: `PUT`  
**Command**:
```bash
curl -X PUT https://vickscrudapi.pythonanywhere.com/update/1 \
     -b cookies.txt \
     -d "name=Jane Doe" \
     -d "email=janedoe@example.com"
```

---

### **Patch User**
**Endpoint**: `https://vickscrudapi.pythonanywhere.com/patch/<user_id>`  
**Method**: `PATCH`  
**Command**:
```bash
curl -X PATCH https://vickscrudapi.pythonanywhere.com/patch/1 \
     -b cookies.txt \
     -d "name=John Smith"
```

---

### **Delete User**
**Endpoint**: `https://vickscrudapi.pythonanywhere.com/delete/<user_id>`  
**Method**: `DELETE`  
**Command**:
```bash
curl -X DELETE https://vickscrudapi.pythonanywhere.com/delete/1 \
     -b cookies.txt
```

---

### **Error Handler (404)**
If you try to access an invalid endpoint, you'll receive a response like:
```bash
curl -X GET https://vickscrudapi.pythonanywhere.com/invalid-endpoint
```

**Response**:
```json
{
    "error": "Endpoint not found!",
    "valid_endpoints": {
        "/": ["GET"],
        "/login": ["POST"],
        "/logout": ["POST"],
        "/post/": ["POST"],
        "/get/<user_id>": ["GET"],
        "/update/<user_id>": ["PUT"],
        "/patch/<user_id>": ["PATCH"],
        "/delete/<user_id>": ["DELETE"]
    }
}
``` 

Replace `<user_id>` with the desired user ID (e.g., `1`) when making requests.
