from ninja import Schema
from pydantic import EmailStr

class UserSchema(Schema):
    username: str
    email: EmailStr
    is_authenticated: bool
    
class UserCreateSchema(Schema):
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    password: str
    confirmPassword: str