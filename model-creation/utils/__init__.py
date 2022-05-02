import tensorflow as tf


def normalize_img(img):
    img = tf.cast(img, dtype=tf.float32)
    # Map values in the range [-1, 1]
    return (img / 127.5) - 1.0


# def preprocess_test_image(img, label):
#     # Only resizing and normalization for the test images.
#     img = tf.image.resize(img, [input_img_size[0], input_img_size[1]])
#     img = normalize_img(img)
#     return img