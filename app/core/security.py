from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import jwt

def hash_password(password: str) -> str:
    return generate_password_hash(password)

def verify_password(password: str, hashed: str) -> bool:
    return check_password_hash(hashed, password)

def generate_token(user_id: int, secret: str, minutes: int) -> str:
    payload = {
        "sub": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=minutes)
    }
    return jwt.encode(payload, secret, algorithm="HS256")
