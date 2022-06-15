# APPLICATION FOR CAPTURING WEBCAM VIDEO STREAM

# LIBRARIES AND MODULES
# ---------------------

from PyQt5 import QtWidgets, uic # For the UI
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot # For threading and signaling between threads
from PyQt5.QtGui import QPixmap, QImage
import cv2 # For image handling

# CLASS DEFINITIONS
# -----------------

# VIDEO THREAD
class VideoThread(QThread):

    # Constructor
    def __init__(self):
        super().__init__()
        self.alive = True # For stopping the video

    # Signal to interact with the main app
    changePixmap = pyqtSignal(QImage)

    # The runner function -> starts the thread, the name of the method must be run
    def run(self):
        videoStream = cv2.VideoCapture(1, cv2.CAP_DSHOW)

        # Read the stream until stopped by main app
        while self.alive:
            ret, frame = videoStream.read()

            # Check if there is a frame to process
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.changePixmap.emit(rgbImage)

    def stop(self):
        self.alive = False

   
    
# APPLICATION (THREAD0)

class App(QtWidgets.QMainWindow):

    # Constructor
    def __init__(self):
        super().__init__()

        uic.loadUi('video.ui', self)

        # Define ui elements
        self.videoImage = self.videoStreamLabel
        self.start = self.startVideoButton
        self.stop = self.stopVideoButton
        self.still = self.takeStillButton

        

if __name__ == '__main__':
    pass