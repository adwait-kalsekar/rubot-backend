from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController
from django.conf import settings

from chat.api import router as chat_router
from genAI.api import router as genAI_router
from users.api import router as users_router

if (settings.DEPLOYMENT_ENV == 'production'):
    api = NinjaExtraAPI(version="1.0.0", docs=None)
else:
    api = NinjaExtraAPI(version="1.0.0", docs_url='/docs/')

api.register_controllers(NinjaJWTDefaultController)

api.add_router("chat/", chat_router)
api.add_router("genAI/", genAI_router)
api.add_router("users/", users_router)

@api.get("/")
def health_check(request):
    return {
        "page": "index",
        "status": "ok"
        }

