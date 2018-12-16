import cv2
import numpy as np
import cv2.aruco as aruco

from src.marker_base import MarkerBase

MIN_MATCH_COUNT = 20

class NaturalFeatureMarker(MarkerBase):

    in_image = None
    marker_image = None

    json_params = None

    cam_mat = None
    dist_mat = None

    r_vec = None
    t_vec = None

    feature_detector = None

    marker_kp = None
    marker_desc = None

    input_kp = None
    input_desc = None

    def __init__(self):
        pass

    def set_json_parameters(self, params):
        self.json_params = params

        if(self.json_params["feature_type"] == "ORB"):
            self.feature_detector = cv2.ORB_create()

        if (self.json_params["feature_type"] == "AKAZE"):
            self.feature_detector = cv2.AKAZE_create()

        self.set_marker_image(self.json_params["marker_path"])


    def set_calib_parameters(self,cam_mat,dist_mat):
        self.cam_mat = cam_mat
        self.dist_mat = dist_mat


    def set_marker_image(self,path):
        self.marker_image = cv2.imread(path)
        self.marker_image = cv2.resize(self.marker_image , (640,480), fx=1.0, fy=1.0)
        self.marker_kp , self.marker_desc = self.feature_detector.detectAndCompute(self.marker_image,None)


    def set_input_image(self, input):
        self.in_image = input
        self.input_kp , self.input_desc = self.feature_detector.detectAndCompute(input,None)


    def process_image(self):
        if (self.json_params["matcher_type"] == "bfm"):
            self.run_bf_matcher()

        if (self.json_params["matcher_type"] == "flann"):
            self.run_flann_matcher()

    def run_bf_matcher(self):
        # BFMatcher with default params
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)
        matches = bf.knnMatch(self.marker_desc, self.input_desc, k=2)

        # Apply ratio test
        good = []
        for m, n in matches:
            if m.distance < 0.75 * n.distance:
                good.append([m])

        if len(good) > MIN_MATCH_COUNT:
            src_pts = np.float32([self.marker_kp[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
            dst_pts = np.float32([self.input_kp[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

            H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
            matchesMask = mask.ravel().tolist()

            h, w ,_ = self.in_image.shape
            pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
            dst = cv2.perspectiveTransform(pts, H)

            num, self.r_vec, self.t_vec, Ns = cv2.decomposeHomographyMat(H,self.cam_mat)

            if (self.json_params["debug_draw"] == True):

                aruco.drawAxis(self.in_image, self.cam_mat, self.dist_mat, self.r_vec[0], self.t_vec[0],
                               0.1)  # Draw Axis
                self.in_image = cv2.polylines(self.in_image, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)



    def run_flann_matcher(self):

        # FLANN parameters
        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)  # or pass empty dictionary
        flann = cv2.FlannBasedMatcher(index_params, search_params)

        matches = flann.knnMatch(np.asarray(self.marker_desc,np.float32), np.asarray(self.input_desc,np.float32), k=2)
        # Need to draw only good matches, so create a mask
        matchesMask = [[0, 0] for i in range(len(matches))]

        # store all the good matches as per Lowe's ratio test.
        good = []
        for m, n in matches:
            if m.distance < 0.7 * n.distance:
                good.append(m)

        if len(good) > MIN_MATCH_COUNT:
            src_pts = np.float32([self.marker_kp[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
            dst_pts = np.float32([self.input_kp[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

            H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

            matchesMask = mask.ravel().tolist()

            h, w ,_ = self.in_image.shape
            pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
            dst = cv2.perspectiveTransform(pts, H)

            num, self.r_vec, self.t_vec, Ns = cv2.decomposeHomographyMat(H,self.cam_mat)

            if (self.json_params["debug_draw"] == True):

                aruco.drawAxis(self.in_image, self.cam_mat, self.dist_mat, self.r_vec[1], self.t_vec[1],
                               0.1)  # Draw Axis
                self.in_image = cv2.polylines(self.in_image, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)


        else:
            matchesMask = None




    def get_output_image(self):
        return self.in_image

    def get_pose(self):
        return self.t_vec, self.r_vec


if __name__ == "__main__":
    marker = NaturalFeatureMarker()

