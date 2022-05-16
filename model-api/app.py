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

origins = ["*"]

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


@app.post('/detect-faces')
async def detect_faces(
    imageFile: UploadFile = File(...),
):
    # TODO: api that scans image and detects faces. For each detected face call /smile to generate a smile
    # this will be the api called by the frontend
    # handle original position and resizing to 64x64 here
    return {"data": "temp"}

@app.post('/smile')
async def smile(
        imageFile: UploadFile = File(...)
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

    img_response = io.BytesIO()
    img.save(img_response, format="JPEG")
    img_response = img_response.getvalue()
    img_response = Response(content=img_response, media_type="image/jpeg")
    return img_response


if __name__ == '__main__':
    log_config = uvicorn.config.LOGGING_CONFIG
    log_config["formatters"]["access"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"
    log_config["formatters"]["default"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"
    uvicorn.run(app, host='0.0.0.0', port=8080, log_config=log_config)
