from dataclasses import dataclass

@dataclass(frozen=True)
class TokenResponse:
    access_token: str
    token_type: str = "Bearer"
