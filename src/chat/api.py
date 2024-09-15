from ninja import Router

router = Router()

@router.get("/")
def get_chat(request):
    return {
        "page": "chat",
        "status": "ok"
        }