def get_roi(image):

    h, w = image.shape[:2]

    roi = image[0:h, 0:w]

    return roi
