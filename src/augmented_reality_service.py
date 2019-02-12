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
        self.__json_reader = JsonReader()
        self.__camera_calib = CameraCalibration()
        self.__camera = cv2.VideoCapture(0)
        self.__marker_obj = None


    def set_service_parameter_json(self,path):
        """
        Sets the json file path and read the required value
        :param path:
        :return:
        """
        self.__json_reader.read_from_file(path)

        calib_path = self.__json_reader.get_value("calibration_path")
        self.__camera_calib.get_calibration_from_file(calib_path)

        marker_type = self.__json_reader.get_value("marker_type")
        self.set_marker(marker_type)


    def set_marker(self,type):
        """
        Creates a marker object depending on the json input
        :param type:
        :return:
        """

        marker_params = self.__json_reader.get_value("marker_params")

        if (type == "aruco"):
            self.__marker_obj = ArucoMarker()

        if (type == "nft"):
            self.__marker_obj = NaturalFeatureMarker()

        self.__marker_obj.set_json_parameters(marker_params)
        self.__marker_obj.set_calib_parameters(self.__camera_calib.__camera_matrix,
                                               self.__camera_calib.__dist_matrix)


    def process_image(self, frame):
        """
        Function that runs to process each frame.
        :param frame:
        :return:
        """
        self.__marker_obj.set_input_image(frame)
        self.__marker_obj.process_image()
        self.__marker_obj.get_pose()


    def run_service(self):
        """

        :return:
        """
        if not self.__camera.isOpened():
            raise IOError("Cannot open webcam !")

        while True:
            ret, frame = self.__camera.read()

            self.process_image(frame)
            output = self.get_output()

            cv2.imshow('AR', output)

            c = cv2.waitKey(30)
            if c == 27:
                break

    def get_output(self):
        """

        :return:
        """
        return self.__marker_obj.get_output_image()

