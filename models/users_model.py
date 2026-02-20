from pydantic import BaseModel
from datetime import datetime

class SignupModel(BaseModel):
    user_name: str
    user_email: str
    user_phone: str
    user_password: str

class LoginModel(BaseModel):
    user_email: str
    user_password: str

class Users(BaseModel):
    user_name: str
    user_email: str
    user_phone: str
    user_verfiycode: int
    user_approve: int
    user_password: str
    user_create: datetime | None = None
