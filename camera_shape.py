import time
import cv2
from cv2 import cvtColor
from robomaster import robot
from robomaster import camera
import numpy as np


if __name__ == '__main__':
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")

    ep_camera = ep_robot.camera

    # cv2
    target_img = cv2.imread('target_b.png', cv2.COLOR_BGR2HSV)

    ep_camera.start_video_stream(display=False, resolution=camera.STREAM_720P)
    while True:
        camera_img = ep_camera.read_cv2_image(strategy='newest')
        blurred_frame = cv2.GaussianBlur(camera_img, (5, 5), 0)
        hsv = cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([38, 86, 0])
        upper_blue = np.array([121, 255, 255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        _, contours = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        for contour in contours:
            cv2.drawContours(camera_img, contour, -1, (0, 255, 0), 3)

        cv2.imshow('cma', camera_img)
        cv2.waitKey(1)


    ep_robot.close()