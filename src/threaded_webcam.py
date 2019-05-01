"""
Webcam code taken from PyImageSearch
https://www.pyimagesearch.com/2015/12/21/increasing-webcam-fps-with-python-and-opencv/
"""

from threading import Thread
import cv2


class WebcamVideoStream:

    def __init__(self, src=0):
        # initialize the video camera stream and read the first frame
        # from the stream
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()

        # initialize the variable used to indicate if the thread should
        # be stopped
        self.stopped = False

    def start(self):
        # start the thread to read frames from the video stream
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        # keep looping infinitely until the thread is stopped
        while True:
            # if the thread indicator variable is set, stop the thread
            if self.stopped:
                return

            # otherwise, read the next frame from the stream
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
        # return the frame most recently read
        return self.frame

    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True

if __name__ == "__main__":
    webcam = WebcamVideoStream().start()

    while True:
        frame = webcam.read()
        cv2.imshow("Frame", frame)

        c = cv2.waitKey(30)
        if c == 27:
            break