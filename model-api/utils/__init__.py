import numpy as np


def normalize_img(img):
    img = img.astype(np.float32)
    img = (img / 127.5) - 1.0
    # Map values in the range [-1, 1]
    return img


def denormalize_img(img):
    img = img * 127.5 + 127.5
    img = img.astype(np.uint8)
    return img

# def preprocess_test_image(img, label):
#     # Only resizing and normalization for the test images.
#     img = tf.image.resize(img, [input_img_size[0], input_img_size[1]])
#     img = normalize_img(img)
#     return img