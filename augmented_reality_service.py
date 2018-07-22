from json_parser import JsonReader
import cv2

class AugmentedRealityService:

    json_reader = None
    camera = None

    def __init__(self):
        self.json_reader = JsonReader()
        self.camera = cv2.VideoCapture(0)

    def process_image(self, frame):
        pass

    def set_service_parameter_json(self,path):
        pass

    def set_calibration_obj(self, calib_obj):
        pass

    def set_marker_obj(self , marker_obj):
        pass

    def set_3d_obj(self):
        pass

    def set_video_obj(self):
        pass

    def run_service(self):
        if not self.camera.isOpened():
            raise IOError("Cannot open webcam")

        while True:
            ret, frame = self.camera.read()

            self.process_image(frame)

            cv2.imshow('AR', frame)

            c = cv2.waitKey(1)
            if c == 27:
                break

