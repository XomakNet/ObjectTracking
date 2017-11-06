import csv
import cv2
import numpy as np

__author__ = 'Xomak'

color = np.array((84, 173, 105), dtype="uint8")

log = open("log.csv", "w")
csv_log = csv.writer(log, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
csv_log.writerow(['time', 'x', 'y'])
#"video.mp4"
video = cv2.VideoCapture(0)
tracking_active = video.isOpened()

while tracking_active:

    tracking_active, frame = video.read()
    if tracking_active:
        current_time = video.get(cv2.CAP_PROP_POS_MSEC)
        cv2.putText(frame, "Ms : " + str(int(current_time)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)

        mask = cv2.inRange(frame, color - 30, color + 30)
        circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=20, maxRadius=0)

        if circles is not None:
            i = circles[0][0]
            csv_log.writerow([current_time, i[0], i[1]])
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)

        frame = cv2.resize(frame, (960, 540))
        cv2.imshow("Tracking", frame)

        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27:
            tracking_active = False

log.close()
