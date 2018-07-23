from json_parser import JsonReader

from aruco_marker import ArucoMarker
from natural_feature_marker import NaturalFeatureMarker

import cv2

class AugmentedRealityService:

    json_reader = None
    camera = None

    marker_obj = None

    def __init__(self):
        self.json_reader = JsonReader()
        self.camera = cv2.VideoCapture(0)

    def set_service_parameter_json(self,path):
        self.json_reader.read_from_file(path)

        marker_type = self.json_reader.get_value("marker_type")
        self.set_marker(marker_type)



    def set_calibration(self,type):
        pass

    def set_marker(self,type):

        marker_params = self.json_reader.get_value("marker_params")

        if (type == "aruco"):
            self.marker_obj = ArucoMarker()

        if (type == "nft"):
            self.marker_obj = NaturalFeatureMarker()

        self.marker_obj.set_json_parameters(marker_params)


    def process_image(self, frame):
        pass


    def run_service(self):
        if not self.camera.isOpened():
            raise IOError("Cannot open webcam !")

        while True:
            ret, frame = self.camera.read()

            self.process_image(frame)

            cv2.imshow('AR', frame)

            c = cv2.waitKey(30)
            if c == 27:
                break

