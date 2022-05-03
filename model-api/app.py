from fastapi import FastAPI, File, UploadFile, Form, Response
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

import io
import numpy as np
from PIL import Image
import tensorflow as tf

from utils import normalize_img, denormalize_img

with tf.device('/CPU:0'):
    model = tf.keras.models.load_model('models/smile_app_model_v1')

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
async def home():
    return {"data": "This is the Smile App API"}


@app.post('/smile')
async def smile(
        imageFile: UploadFile = File(...),
        originalWidth: int = Form(...),
        originalHeight: int = Form(...),
):
    img = Image.open(imageFile.file)
    img = np.array(img)
    img = normalize_img(img)
    img = np.expand_dims(img, axis=0)

    with tf.device('/CPU:0'):
        img = model(img)

    img = img[0].numpy()
    img = denormalize_img(img)
    img = Image.fromarray(img)
    img = img.resize((originalWidth, originalHeight))

    img_response = io.BytesIO()
    img.save(img_response, format="JPEG")
    img_response = img_response.getvalue()
    img_response = Response(content=img_response, media_type="image/jpeg")
    return img_response


if __name__ == '__main__':
    uvicorn.run(app)
