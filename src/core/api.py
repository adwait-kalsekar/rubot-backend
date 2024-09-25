from ninja import Schema
from ninja_extra import NinjaExtraAPI
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.controller import NinjaJWTDefaultController

from chat.api import router as chat_router
from genAI.api import router as genAI_router
from users.api import router as users_router

api = NinjaExtraAPI(version="1.0.0", docs_url='/docs/')

api.register_controllers(NinjaJWTDefaultController)

api.add_router("chat/", chat_router)
api.add_router("genAI/", genAI_router)
api.add_router("users/", users_router)

class UserSchema(Schema):
    username: str
    email: str
    is_authenticated: bool

@api.get("/")
def health_check(request):
    return {
        "page": "index",
        "status": "ok"
        }

@api.get('/me', response=UserSchema, auth=JWTAuth())
def me(request):
    return {
        "page": "me",
        "status": "ok"
        }