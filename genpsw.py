import secrets
import string

def generate_password(length=8):
    charset = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(charset) for _ in range(length))

# Example usage
for _ in range(5):
    print(generate_password())
