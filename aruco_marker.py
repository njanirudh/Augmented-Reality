import cv2
import numpy as np
import cv2.aruco as aruco

from marker_base import MarkerBase

class ArucoMarker(MarkerBase):

    in_image = None
    def __init__(self):
        pass

    def set_json_parameters(self,params):
        pass

    def process_image(self):
        gray = cv2.cvtColor(self.in_image, cv2.COLOR_BGR2GRAY)
        aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
        parameters = aruco.DetectorParameters_create()

        # lists of ids and the corners beloning to each id
        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

        aruco.drawDetectedMarkers(self.in_image, corners)  # Draw A square around the markers



    def set_input_image(self, input):
        self.in_image = input

    def get_output_image(self):
        return self.in_image

if __name__ == "__main__":
    marker = ArucoMarker()

