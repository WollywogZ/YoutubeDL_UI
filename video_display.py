#scrapping for the time being, but might return to it sometime

import cv2


class MyVideoCapture:
    def __init__(self, video_source=0):
        # Try to open video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("dead link dumbass", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
        self.window.mainloop()

    # def get_frame(self):
    #     if self.vid.isOpened():
    #         ret, frame = self.vid.read()
    #         if ret:
    #             return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    #         else:
    #             return (ret, None)
    #     else:
    #         return (ret, None)