from dataclasses import dataclass

@dataclass(frozen=True)
class LoginRequest:
    username: str
    password: str

    @staticmethod
    def from_dict(data: dict) -> "LoginRequest":
        if not isinstance(data, dict):
            raise ValueError("Invalid payload")

        username = data.get("username")
        password = data.get("password")

        if not isinstance(username, str) or not username.strip():
            raise ValueError("username is required")

        if not isinstance(password, str) or not password.strip():
            raise ValueError("password is required")

        return LoginRequest(username=username.strip(), password=password)
