import cv2  # python-opencv
import numpy as np
import json

width, height = 1250, 125
x1, y1 = 0, 0
x2, y2 = 200, 400
image = np.ones((height, width)) * 255

line_thickness = 4
with open('Lines\public\image.json') as f:
    img = json.load(f)
    time = 173
    for i in range(time):
        j = img['image']['lines'][i]
        cv2.line(image, (j['from']['x'], j['from']['y']), (j['to']['x'], j['to']['y']), (0, 255, 0), thickness=line_thickness)

cv2.imshow("foo",image)
cv2.waitKey()
cv2.imwrite('imaginary_ctf\Round16\Lines\output.jpg', image)

