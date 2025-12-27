from app.core.security import verify_password, generate_token
from app.users.repository import UserRepository

def authenticate_user(username: str, password: str, config) -> str:
    user = UserRepository.get_by_username(username)

    if not user:
        raise ValueError("Invalid credentials")

    if not verify_password(password, user.password_hash):
        raise ValueError("Invalid credentials")

    return generate_token(
        user_id=user.id,
        secret=config["SECRET_KEY"],
        minutes=config["TOKEN_EXPIRATION_MINUTES"]
    )
