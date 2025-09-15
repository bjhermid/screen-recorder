import numpy as np
import cv2
import mss
import time


class ScreenRecorder:
    def __init__(self, output_file: str, fps: int = 30):
        self.output_file = output_file
        self.fps = fps
        self.running = False

    def start(self):
        self.running = True
        sct = mss.mss()
        monitor = sct.monitors[1]

        width = monitor['width']
        height = monitor['height']

        fourcc = cv2.VideoWriter.fourcc(*'mp4v')
        out = cv2.VideoWriter(self.output_file, fourcc,
                              self.fps, (width, height))

        while self.running:
            frame = np.array(sct.grab(monitor))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
            out.write(frame)
            time.sleep(1 / self.fps)

        out.release()

    def stop(self):
        self.running = False
        print(
            f"\n Perekaman layar selesei. File disimpan di {self.output_file}")
        cv2.destroyAllWindows()
