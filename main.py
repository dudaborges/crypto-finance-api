from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()

@app.router.get('/')
def first():
    return 'Hello World'

app.include_router(prefix='/first', router=router)