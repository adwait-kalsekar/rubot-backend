from ninja import Router
from ninja_jwt.authentication import JWTAuth
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .schemas import UserCreateSchema, UserSchema

router = Router()

@router.get("/")
def get_users(request):
    return {
        "page": "users",
        "status": "ok"
        }
    
@router.post("/")
def create_user(request, payload: UserCreateSchema):
    # Check if passwords match
    if payload.password != payload.confirmPassword:
        return {"error": "Passwords do not match"}

    # Create the user
    user = User.objects.create(
        first_name=payload.first_name,
        last_name=payload.last_name,
        username=payload.username,
        email=payload.email,
        password=make_password(payload.password),  # Hash the password before saving
    )
    
    return {"success": f"User {user.username} created successfully"}
    
@router.get('/me', response=UserSchema, auth=JWTAuth())
def me(request):
    return {
        "page": "me",
        "status": "ok"
        }