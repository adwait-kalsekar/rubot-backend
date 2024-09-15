from ninja import Router

router = Router()

@router.get("/")
def get_genAI(request):
    return {
        "page": "genAI",
        "status": "ok"
        }