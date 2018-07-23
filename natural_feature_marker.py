import cv2

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

        if(params["feature_type"] == "ORB"):
            self.feature_detector = cv2.ORB_create()

        if (params["feature_type"] == "FAST"):
            self.feature_detector = cv2.FastFeatureDetector_create()

        if (params["feature_type"] == "AKAZE"):
            self.feature_detector = cv2.AKAZE_create()

        self.set_marker_image(params["marker_path"])


    def set_calib_parameters(self,cam_mat,dist_mat):
        self.cam_mat = cam_mat
        self.dist_mat = dist_mat

    def process_image(self):

        # BFMatcher with default params
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(self.marker_desc, self.input_desc, k=2)
        # Apply ratio test
        good = []
        for m, n in matches:
            if m.distance < 0.75 * n.distance:
                good.append([m])
        # cv2.drawMatchesKnn expects list of lists as matches.
        self.in_image = cv2.drawMatchesKnn(self.marker_image, self.marker_kp,
                                            self.in_image , self.input_kp, good, self.in_image ,flags=2)

    def set_marker_image(self,path):
        self.marker_image = cv2.imread(path)
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

