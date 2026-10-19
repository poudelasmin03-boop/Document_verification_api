from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from router.user import router as user_router
from router.upload_document import router as request_document

app = FastAPI()


origin = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_headers=["*"],
    allow_origins=origin,
    allow_methods=["*"],
)


app.include_router(user_router)
app.include_router(request_document)


@app.get("/")
def home_views():
    return {"message": "Welcome to our home page"}
