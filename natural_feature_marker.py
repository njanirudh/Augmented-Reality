import cv2
import numpy as np

from marker_base import MarkerBase

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

        if (self.json_params["feature_type"] == "FAST"):
            self.feature_detector = cv2.FastFeatureDetector_create()

        if (self.json_params["feature_type"] == "AKAZE"):
            self.feature_detector = cv2.AKAZE_create()

        self.set_marker_image(self.json_params["marker_path"])


    def set_calib_parameters(self,cam_mat,dist_mat):
        self.cam_mat = cam_mat
        self.dist_mat = dist_mat

    def process_image(self):
        if (self.json_params["matcher_type"] == "knn"):
            self.run_bf_matcher()

        if (self.json_params["matcher_type"] == "flann"):
            self.run_flann_matcher()

    def run_bf_matcher(self):
        # BFMatcher with default params
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(self.marker_desc, self.input_desc, k=2)
        # Apply ratio test
        good = []
        for m, n in matches:
            if m.distance < 0.75 * n.distance:
                good.append([m])

        if (self.json_params["debug_draw"] == True):
            # cv2.drawMatchesKnn expects list of lists as matches.
            self.in_image = cv2.drawMatchesKnn(self.marker_image, self.marker_kp,
                                           self.in_image, self.input_kp, good, self.in_image, flags=2)

    def run_flann_matcher(self):

        # FLANN parameters
        FLANN_INDEX_KDTREE = 2
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)  # or pass empty dictionary
        flann = cv2.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(np.asarray(self.marker_desc,np.float32), np.asarray(self.input_desc,np.float32), k=2)
        # Need to draw only good matches, so create a mask
        matchesMask = [[0, 0] for i in range(len(matches))]
        # ratio test as per Lowe's paper
        for i, (m, n) in enumerate(matches):
            if m.distance < 0.7 * n.distance:
                matchesMask[i] = [1, 0]

        if (self.json_params["debug_draw"] == True):
            draw_params = dict(matchColor=(0, 255, 0),
                           singlePointColor=(255, 0, 0),
                           matchesMask=matchesMask,
                           flags=0)
            self.in_image = cv2.drawMatchesKnn(self.marker_image, self.marker_kp,
                                           self.in_image, self.input_kp, matches,self.in_image, **draw_params)

    def set_marker_image(self,path):
        self.marker_image = cv2.imread(path)
        self.marker_image = cv2.resize(self.marker_image , (0,0), fx=0.5, fy=0.5)
        self.marker_kp , self.marker_desc = self.feature_detector.detectAndCompute(self.marker_image,None)

    def set_input_image(self, input):
        self.in_image = input
        self.input_kp , self.input_desc = self.feature_detector.detectAndCompute(input,None)

    def get_output_image(self):
        return self.in_image

    def get_pose(self):
        return self.t_vec, self.r_vec


if __name__ == "__main__":
    marker = NaturalFeatureMarker()

