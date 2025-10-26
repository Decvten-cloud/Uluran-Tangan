from werkzeug.security import generate_password_hash, check_password_hash

# Test password
password = "test123"
hashed_password = generate_password_hash(password)
print(f"Hashed password: {hashed_password}")

# Verify password
if check_password_hash(hashed_password, password):
    print("Password is correct!")
else:
    print("Password is incorrect!")
