import cv2
from infra.config import TEMPLATE_PATH, THRESHOLD
from vision.preprocess import preprocess

class Inspector:

    def __init__(self):

        self.template = cv2.imread(TEMPLATE_PATH, 0)

    def inspect(self, frame):

        gray = preprocess(frame)

        result = cv2.matchTemplate(gray, self.template, cv2.TM_CCOEFF_NORMED)

        _, max_val, _, _ = cv2.minMaxLoc(result)

        if max_val > THRESHOLD:
            return True
        else:
            return False
