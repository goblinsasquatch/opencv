import cv2
from cv2 import CAP_PROP_FPS
from cv2 import CAP_PROP_FRAME_COUNT

vid_capture = cv2.VideoCapture('resources/video.mp4')

if not vid_capture.isOpened():
    print('Error opening file')
else:
    fps = int(vid_capture.get(CAP_PROP_FPS))
    print("Frame Rate : ", fps, "frames per second")

    frame_count = vid_capture.get(CAP_PROP_FRAME_COUNT)
    print("Frame count : ", frame_count)

while(vid_capture.isOpened()):
    # vid_capture.read() methods returns a tuple, first element is a bool
    # and the second is frame
    ret, frame = vid_capture.read()
    if ret == True:
        cv2.imshow('Frame', frame)
        # 20 is in milliseconds, try to increase the value, say 50 and observe
        key = cv2.waitKey(20)

        if key == ord('q'):
            break
    else:
        break

# Release the video capture object
vid_capture.release()
cv2.destroyAllWindows()
