"""
Webcam code taken from PyImageSearch
https://www.pyimagesearch.com/2015/12/21/increasing-webcam-fps-with-python-and-opencv/
"""

from threading import Thread
import cv2

class WebcamVideoStream:

    def __init__(self, src=0):
        """
        Initialize the video camera stream and read the first frame
        from the stream.
        """

        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()

        # initialize the variable used to indicate if the thread should
        # be stopped
        self.stopped = False

    def start(self):
        """
        Start the thread to read frames from the video stream
        :return: Returns the object instance
        """
        Thread(target=self.update, args=()).start()
        return self

    def isOpened(self):
        """
        Checks if the camera stream is opened or not.
        :return: Boolean
        """
        return self.stream.isOpened()

    def update(self):
        """
        Keep looping infinitely until the thread is stopped.
        :return: None
        """
        while True:
            # if the thread indicator variable is set, stop the thread
            if self.stopped:
                return

            # otherwise, read the next frame from the stream
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
        """
        Return the frame most recently read.
        :return: Returns the current frame from the camera
        """
        return self.frame

    def stop(self):
        """
        Indicate that the thread should be stopped.
        :return: None
        """
        self.stopped = True

if __name__ == "__main__":
    webcam = WebcamVideoStream().start()

    while True:
        frame = webcam.read()
        cv2.imshow("Frame", frame)

        c = cv2.waitKey(30)
        if c == 27:
            break