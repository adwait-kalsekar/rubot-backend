from ninja import NinjaAPI

from chat.api import router as chat_router
from genAI.api import router as genAI_router
from users.api import router as users_router

api = NinjaAPI()

api.add_router("chat/", chat_router)
api.add_router("genAI/", genAI_router)
api.add_router("users/", users_router)

@api.get("/")
def health_check(request):
    return {
        "page": "index",
        "status": "ok"
        }