# Post method
'''
curl -X POST http://127.0.0.1:5000/post/ -d "name=John Doe" -d "email=johndoe@example.com"
'''

# Get method
'''
curl -X GET http://127.0.0.1:5000/
'''

# Update method
'''
curl -X PUT http://127.0.0.1:5000/update/1 -d "name=Jane Doe" -d "email=janedoe@example.com"
'''

# Get by ID method
'''
curl -X GET http://127.0.0.1:5000/get/1
'''

# Patch method
'''
curl -X PATCH http://127.0.0.1:5000/patch/1 -d "email=newemail@example.com"
'''
