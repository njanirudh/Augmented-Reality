import cv2

from marker_base import MarkerBase

class NaturalFeatureMarker(MarkerBase):

    in_image = None

    def __init__(self):
        pass

    def set_json_parameters(self, params):
        pass

    def set_calib_parameters(self,cam_mat,dist_mat):
        pass

    def process_image(self):
        pass

    def set_input_image(self, input):
        self.in_image = cv2.cvtColor(input, cv2.COLOR_RGB2GRAY)

    def get_output_image(self):
        return self.in_image

if __name__ == "__main__":
    marker = NaturalFeatureMarker()

