import cv2
import numpy as np

N = 100

orig_img = cv2.imread('resources/demo.jpg')
img = cv2.resize(orig_img, (0, 0), fx=0.5, fy=0.5)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(
    img, maxCorners=N, qualityLevel=0.1, minDistance=5)

corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(orig_img, (x, y), 5, (255, 0, 0), -1)

print(img.shape)
# cv.imwrite('truck2.jpg', img)

cv2.imshow('image', orig_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
