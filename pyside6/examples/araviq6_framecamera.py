"""
Camera example with blurring pipeline on QVideoframe.

The processor receives video frame from the video sink of media capture session,
and emits processed video frame.

https://github.com/JSS95/araviq6/blob/master/doc/source/examples/PySide6/frame.camera.py
"""

import cv2  # type: ignore[import]
import numpy as np
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow
from PySide6.QtMultimedia import QCamera, QMediaCaptureSession, QVideoFrame, QVideoSink
from PySide6.QtMultimediaWidgets import QVideoWidget
from araviq6 import VideoFrameWorker, VideoFrameProcessor


class BlurWorker(VideoFrameWorker):
    def processArray(self, array: np.ndarray) -> np.ndarray:
        return cv2.GaussianBlur(array, (0, 0), 25)


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._camera = QCamera()
        self._captureSession = QMediaCaptureSession()
        self._cameraVideoSink = QVideoSink()
        self._frameProcessor = VideoFrameProcessor()
        self._blurWorker = BlurWorker()
        self._videoWidget = QVideoWidget()

        # set up the pipeline
        self._captureSession.setCamera(self._camera)
        self._captureSession.setVideoSink(self._cameraVideoSink)
        self._cameraVideoSink.videoFrameChanged.connect(
            self._frameProcessor.processVideoFrame
        )
        self._frameProcessor.videoFrameProcessed.connect(self.displayVideoFrame)

        self._frameProcessor.setWorker(self._blurWorker)
        self.setCentralWidget(self._videoWidget)

        self._camera.start()

    @Slot(QVideoFrame)
    def displayVideoFrame(self, frame: QVideoFrame):
        self._videoWidget.videoSink().setVideoFrame(frame)

    def closeEvent(self, event):
        self._frameProcessor.stop()
        super().closeEvent(event)


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
    app.quit()
