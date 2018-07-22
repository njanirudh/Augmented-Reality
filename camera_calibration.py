import cv2

class CameraCalibration:

    default_camera_mat = None
    default_dist_mat = None

    def __init__(self):
        # Setting default calibration Values
        cv_file = cv2.FileStorage("/data/calibration.yaml", cv2.FILE_STORAGE_READ)

        # note we also have to specify the type to retrieve other wise we only get a
        # FileNode object back instead of a matrix
        self.default_camera_mat = cv_file.getNode("camera_matrix").mat()
        self.default_dist_mat = cv_file.getNode("dist_coeff").mat()

    def get_default_calibration(self):
        pass

    def calibrate_camera(self,path):
        pass

    def get_calibration_from_file(self,path):
        # FILE_STORAGE_READ
        cv_file = cv2.FileStorage(path, cv2.FILE_STORAGE_READ)

        # note we also have to specify the type to retrieve other wise we only get a
        # FileNode object back instead of a matrix
        camera_matrix = cv_file.getNode("camera_matrix").mat()
        dist_matrix = cv_file.getNode("dist_coeff").mat()

        print("camera_matrix : ", camera_matrix.tolist())
        print("dist_matrix : ", dist_matrix.tolist())

        cv_file.release()

        return camera_matrix,dist_matrix


