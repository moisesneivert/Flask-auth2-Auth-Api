from typing import Optional
from app.users.models import User
from app.extensions.db import db

class UserRepository:
    @staticmethod
    def get_by_username(username: str) -> Optional[User]:
        return User.query.filter_by(username=username).first()

    @staticmethod
    def create_user(username: str, password_hash: str) -> User:
        user = User(username=username, password_hash=password_hash)
        db.session.add(user)
        db.session.commit()
        return user
