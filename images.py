import cv2 as cv

# img = cv.imread('truck.jpg')
img = cv.imread('resources/demo.jpg')
# img = cv.resize(img, (0, 0), fx=0.25, fy=0.25)
# img = cv.rotate(img, cv.cv2.ROTATE_90_CLOCKWISE)

print(img.shape)
# cv.imwrite('truck2.jpg', img)

cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
