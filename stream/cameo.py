import cv2
import filters
from managers import WindowManager, CaptureManager

class Cameo(object):
    def __init__(self, camera):
        self._windowManager = WindowManager(f'Cameo+{camera}', self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture(camera), self._windowManager, True)
        #self._curveFilter = filters.BGRPortraCurveFilter()

    def run(self):
        """Run the main loop."""         
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame
            if frame is not None:
                # TODO: Filter the frame (Chapter 3).
                filters.strokeEdges(frame, frame)
            
            #self._curveFilter.apply(frame, frame)
            self._captureManager.exitFrame()
            self._windowManager.processEvents()

    def onKeypress(self, keycode):
        """
        Handle a keypress.
        space -> Take a screenshot.
        tab -> Start/stop recording a screencast.
        escape -> Quit.
        """         
        if keycode == 32: # space
            self._captureManager.writeImage('../sources/screenshot.png')
        elif keycode == 9: # tab
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('../sources/screencast.avi')
            else:
                self._captureManager.stopWritingVideo()         
        elif keycode == 27: # escape
            self._windowManager.destroyWindow()


if __name__=="__main__":
    x = Cameo(1)
    y = Cameo(2)

    x.run()
    y.run()




