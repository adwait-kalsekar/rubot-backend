from ninja import Schema
from pydantic import EmailStr

class UserSchema(Schema):
    username: str
    email: EmailStr
    is_authenticated: bool