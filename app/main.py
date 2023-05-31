from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import base, mate_analysis

app = FastAPI()

origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(base.router)
app.include_router(mate_analysis.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
 	uvicorn.run(app, host="127.0.0.1", port=8000)
