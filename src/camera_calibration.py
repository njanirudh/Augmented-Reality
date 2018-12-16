import cv2

# Class to read calibration matrix from file
class CameraCalibration:

    camera_matrix = None
    dist_matrix = None

    def __init__(self):
        pass

    def calibrate_camera(self,path):
        pass

    def get_calibration_from_file(self,path):
        # FILE_STORAGE_READ
        cv_file = cv2.FileStorage(path, cv2.FILE_STORAGE_READ)

        # note we also have to specify the type to retrieve other wise we only get a
        # FileNode object back instead of a matrix
        self.camera_matrix = cv_file.getNode("camera_matrix").mat()
        self.dist_matrix = cv_file.getNode("dist_coeff").mat()

        print("camera_matrix : ", self.camera_matrix.tolist())
        print("dist_matrix : ", self.dist_matrix.tolist())

        cv_file.release()

    def get_camera_mat(self):
        return self.camera_matrix

    def get_dist_mat(self):
        return self.dist_matrix


