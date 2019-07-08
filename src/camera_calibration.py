import cv2

class CameraCalibration:
    """
    Class to read calibration matrix from file
    """

    def __init__(self):
        self.__camera_matrix = None
        self.__dist_matrix = None

    def calibrate_camera(self,path):
        """
        Code to calibrate the camera given a list of images for calibration.
        :param path: Path to the calibration images
        :return: None
        """
        pass

    def get_calibration_from_file(self,path):
        """
        Extract the calibration values from the path.
        :param path: Path to calibration file
        :return: None
        """

        # FILE_STORAGE_READ
        cv_file = cv2.FileStorage(path, cv2.FILE_STORAGE_READ)

        # Note :: We also have to specify the type to retrieve other wise we only get a
        # FileNode object back instead of a matrix
        self.__camera_matrix = cv_file.getNode("camera_matrix").mat()
        self.__dist_matrix = cv_file.getNode("dist_coeff").mat()

        print("camera_matrix : ", self.__camera_matrix.tolist())
        print("dist_matrix : ", self.__dist_matrix.tolist())

        cv_file.release()

    def get_camera_mat(self):
        """
        Returns the camera matrix
        :return: Returns the camera matrix
        """
        return self.__camera_matrix

    def get_dist_mat(self):
        """
        Returns the distorsion matrix
        :return: Returns the distorsion matrix
        """
        return self.__dist_matrix


