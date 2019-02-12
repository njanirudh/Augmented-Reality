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

        :param path:
        :return:
        """
        pass

    def get_calibration_from_file(self,path):
        """

        :param path:
        :return:
        """

        # FILE_STORAGE_READ
        cv_file = cv2.FileStorage(path, cv2.FILE_STORAGE_READ)

        # note we also have to specify the type to retrieve other wise we only get a
        # FileNode object back instead of a matrix
        self.__camera_matrix = cv_file.getNode("camera_matrix").mat()
        self.__dist_matrix = cv_file.getNode("dist_coeff").mat()

        print("camera_matrix : ", self.__camera_matrix.tolist())
        print("dist_matrix : ", self.__dist_matrix.tolist())

        cv_file.release()

    def get_camera_mat(self):
        """

        :return:
        """
        return self.__camera_matrix

    def get_dist_mat(self):
        """

        :return:
        """
        return self.__dist_matrix


