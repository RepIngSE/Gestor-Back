from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
    EMAIL: EmailStr 
    PASSWORD: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    role: int
    document: str
