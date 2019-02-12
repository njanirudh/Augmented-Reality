import cv2
import numpy as np
import cv2.aruco as aruco

from src.markers.marker_base import MarkerBase

MIN_MATCH_COUNT = 20

class NaturalFeatureMarker(MarkerBase):

    def __init__(self):
        super().__init__()

        self.__in_image = None
        self.__json_params = None

        self.__cam_mat = None
        self.__dist_mat = None

        self.__r_vec = None
        self.__t_vec = None

        self.__marker_image = None
        self.__feature_detector = None

        self.__marker_kp = None
        self.__marker_desc = None

        self.__input_kp = None
        self.__input_desc = None

    def set_json_parameters(self, params):
        self.__json_params = params

        if(self.__json_params["feature_type"] == "ORB"):
            self.__feature_detector = cv2.ORB_create()

        if (self.__json_params["feature_type"] == "AKAZE"):
            self.__feature_detector = cv2.AKAZE_create()

        self.set_marker_image(self.__json_params["marker_path"])


    def set_calib_parameters(self,cam_mat,dist_mat):
        self.__cam_mat = cam_mat
        self.__dist_mat = dist_mat


    def set_marker_image(self,path):
        self.__marker_image = cv2.imread(path)
        self.__marker_image = cv2.resize(self.__marker_image, (640, 480), fx=1.0, fy=1.0)
        self.__marker_kp , self.__marker_desc = self.__feature_detector.detectAndCompute(self.__marker_image, None)


    def set_input_image(self, input):
        self.in_image = input
        self.__input_kp , self.__input_desc = self.__feature_detector.detectAndCompute(input, None)


    def process_image(self):
        if (self.__json_params["matcher_type"] == "bfm"):
            self.run_bf_matcher()

        if (self.__json_params["matcher_type"] == "flann"):
            self.run_flann_matcher()

    def run_bf_matcher(self):
        # BFMatcher with default params
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)
        matches = bf.knnMatch(self.__marker_desc, self.__input_desc, k=2)

        # Apply ratio test
        good = []
        for m, n in matches:
            if m.distance < 0.75 * n.distance:
                good.append([m])

        if len(good) > MIN_MATCH_COUNT:
            src_pts = np.float32([self.__marker_kp[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
            dst_pts = np.float32([self.__input_kp[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

            H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
            matchesMask = mask.ravel().tolist()

            h, w ,_ = self.in_image.shape
            pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
            dst = cv2.perspectiveTransform(pts, H)

            num, self.r_vec, self.t_vec, Ns = cv2.decomposeHomographyMat(H, self.__cam_mat)

            if (self.__json_params["debug_draw"] == True):

                aruco.drawAxis(self.in_image, self.__cam_mat, self.__dist_mat, self.r_vec[0], self.t_vec[0],
                               0.05)  # Draw Axis
                self.in_image = cv2.polylines(self.in_image, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)



    def run_flann_matcher(self):

        # FLANN parameters
        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)  # or pass empty dictionary
        flann = cv2.FlannBasedMatcher(index_params, search_params)

        matches = flann.knnMatch(np.asarray(self.__marker_desc, np.float32), np.asarray(self.__input_desc, np.float32), k=2)
        # Need to draw only good matches, so create a mask
        matchesMask = [[0, 0] for i in range(len(matches))]

        # store all the good matches as per Lowe's ratio test.
        good = []
        for m, n in matches:
            if m.distance < 0.7 * n.distance:
                good.append(m)

        if len(good) > MIN_MATCH_COUNT:
            src_pts = np.float32([self.__marker_kp[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
            dst_pts = np.float32([self.__input_kp[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

            H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

            matchesMask = mask.ravel().tolist()

            h, w ,_ = self.in_image.shape
            pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
            dst = cv2.perspectiveTransform(pts, H)

            num, self.r_vec, self.t_vec, Ns = cv2.decomposeHomographyMat(H, self.__cam_mat)
            print(self.__in_image.shape)

            if (self.__json_params["debug_draw"] == True):

                aruco.drawAxis(self.in_image, self.__cam_mat, self.__dist_mat, self.r_vec[1], self.t_vec[1],
                               0.1)  # Draw Axis
                self.in_image = cv2.polylines(self.in_image, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)


    def get_output_image(self):
        return self.__in_image

    def get_pose(self):
        return self.__t_vec, self.__r_vec


if __name__ == "__main__":
    marker = NaturalFeatureMarker()

