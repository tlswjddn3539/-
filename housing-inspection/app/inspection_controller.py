from infra.camera import Camera
from vision.inspector import Inspector

class InspectionController:

    def __init__(self):
        self.camera = Camera()
        self.inspector = Inspector()

    def run_inspection(self):

        frame = self.camera.capture()

        result = self.inspector.inspect(frame)

        return result
