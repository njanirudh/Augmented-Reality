from src.json_parser import JsonReader
from src.camera_calibration import CameraCalibration

from src.markers.aruco_marker import ArucoMarker
from src.markers.natural_feature_marker import NaturalFeatureMarker

import cv2


class AugmentedRealityService:
    """
    """

    def __init__(self):
        """

        """
        self.json_reader = JsonReader()
        self.camera_calib = CameraCalibration()
        self.camera = cv2.VideoCapture(0)
        self.marker_obj = None


    def set_service_parameter_json(self,path):
        """
        Sets the json file path and read the required value
        :param path:
        :return:
        """
        self.json_reader.read_from_file(path)

        calib_path = self.json_reader.get_value("calibration_path")
        self.camera_calib.get_calibration_from_file(calib_path)

        marker_type = self.json_reader.get_value("marker_type")
        self.set_marker(marker_type)


    def set_marker(self,type):
        """
        Creates a marker object depending on the json input
        :param type:
        :return:
        """

        marker_params = self.json_reader.get_value("marker_params")

        if (type == "aruco"):
            self.marker_obj = ArucoMarker()

        if (type == "nft"):
            self.marker_obj = NaturalFeatureMarker()

        self.marker_obj.set_json_parameters(marker_params)
        self.marker_obj.set_calib_parameters(self.camera_calib.camera_matrix,
                                             self.camera_calib.dist_matrix)



    def process_image(self, frame):
        """
        Function that runs to process each frame.
        :param frame:
        :return:
        """
        self.marker_obj.set_input_image(frame)
        self.marker_obj.process_image()
        self.marker_obj.get_pose()

        return  self.marker_obj.get_output_image()


    def run_service(self):
        """

        :return:
        """
        if not self.camera.isOpened():
            raise IOError("Cannot open webcam !")

        while True:
            ret, frame = self.camera.read()

            output = self.process_image(frame)

            cv2.imshow('AR', output)

            c = cv2.waitKey(30)
            if c == 27:
                break

