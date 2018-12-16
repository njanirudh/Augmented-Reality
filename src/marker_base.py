from abc import ABC, abstractmethod

# All types of markers must have the following class signature
class MarkerBase(ABC):

    # Set everytime for new webcam frame
    @abstractmethod
    def set_input_image(self, input):
        pass

    # Parameters for the markers are set
    # Parameters are different for different markers
    @abstractmethod
    def set_json_parameters(self,params):
        pass

    # Setting Calibration parameters for finding the pose
    @abstractmethod
    def set_calib_parameters(self,cam_mat,dist_mat):
        pass

    # Function called for each frame
    @abstractmethod
    def process_image(self):
        pass

    # Get output image with detected marker and axis
    @abstractmethod
    def get_output_image(self):
        pass

    # Returns the transformation matrix and rotation matrix
    @abstractmethod
    def get_pose(self):
        pass