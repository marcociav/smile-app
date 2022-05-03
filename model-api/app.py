from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
# import tensorflow as tf


app = FastAPI(
    title="Smile App API"
)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://marcociav.github.io/",
    "https://marcociav.github.io/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get('/')
def home():
    return {"data": "This is the Smile App API"}


@app.post('/smile')
def smile():
    return {"data": "This will be the Smile App Output"}


if __name__ == '__main__':
    uvicorn.run(app)
