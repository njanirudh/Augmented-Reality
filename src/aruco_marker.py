import cv2
import numpy as np
import cv2.aruco as aruco

from src.marker_base import MarkerBase


class ArucoMarker(MarkerBase):

    in_image = None

    aruco_dict = None
    parameters = None

    json_params = None

    cam_mat = None
    dist_mat = None

    r_vec = None
    t_vec = None

    font = cv2.FONT_HERSHEY_SIMPLEX  # font for displaying text (below)

    def __init__(self):
        self.aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
        self.parameters = aruco.DetectorParameters_create()

    def set_json_parameters(self,params):
        self.json_params = params

    def set_calib_parameters(self,cam_mat,dist_mat):
        self.cam_mat = cam_mat
        self.dist_mat = dist_mat

    def process_image(self):
        gray = cv2.cvtColor(self.in_image, cv2.COLOR_BGR2GRAY)

        # lists of ids and the corners beloning to each id
        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, self.aruco_dict, parameters=self.parameters)

        if np.all(ids != None):

            # Estimate pose of each marker and return the values rvet and tvec-different from camera coefficients
            self.r_vec, self.t_vec, _ = aruco.estimatePoseSingleMarkers(corners[0], 0.05, self.cam_mat,
                                                            self.dist_mat)

            if(self.json_params["debug_draw"] == True ):
                aruco.drawAxis(self.in_image,  self.cam_mat, self.dist_mat,  self.r_vec[0], self.t_vec[0], 0.1)  # Draw Axis
                aruco.drawDetectedMarkers(self.in_image, corners)  # Draw A square around the markers

                cv2.putText(self.in_image, "Id: " + str(ids), (0, 64), self.font, 1, (0, 255, 0), 2, cv2.LINE_AA)


    def set_input_image(self, input):
        self.in_image = input

    def get_output_image(self):
        return self.in_image

    def get_pose(self):
        return self.t_vec , self.r_vec

if __name__ == "__main__":
    marker = ArucoMarker()

