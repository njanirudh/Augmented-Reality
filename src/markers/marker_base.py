from abc import ABC, abstractmethod

class MarkerBase(ABC):
    """
    All types of markers must have
    the following class signature
    """
    def __init__(self):
        pass

    @abstractmethod
    def set_input_image(self, input):
        """
        Set everytime for new webcam frame
        :param input:
        :return:
        """
        pass

    @abstractmethod
    def set_json_parameters(self,params):
        """
        Parameters for the markers are set
        Parameters are different for different markers
        :param params:
        :return:
        """
        pass

    @abstractmethod
    def set_calib_parameters(self,cam_mat,dist_mat):
        """
        Setting Calibration parameters for finding the pose
        :param cam_mat:
        :param dist_mat:
        :return:
        """
        pass

    @abstractmethod
    def process_image(self):
        """
        Function called for each frame
        :return:
        """
        pass

    @abstractmethod
    def get_output_image(self):
        """
        Get output image with detected
        marker and axis
        :return:
        """
        pass

    @abstractmethod
    def get_pose(self):
        """
        Returns the transformation matrix
        and rotation matrix
        :return:
        """
        pass