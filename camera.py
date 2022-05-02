# -*-coding:utf-8-*-
# Copyright (c) 2020 DJI.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import time
import cv2
from object_detector import *
from robomaster import robot, camera, robotic_arm
import numpy as np

if __name__ == '__main__':
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")

    ep_gripper = ep_robot.gripper
    ep_camera = ep_robot.camera

    ep_camera.start_video_stream(display=False)
    obj1 = cv2.createBackgroundSubtractorMOG2()
    obj2 = cv2.createBackgroundSubtractorKNN()
    
    #de obj
    detector = HomogeneousBgDetector()
    while True:
        img = ep_camera.read_cv2_image()
        contours = detector.detect_objects(img)
        # Draw objects boundaries
        for cnt in contours:
            # Get rect
            rect = cv2.minAreaRect(cnt)
            (x, y), (w, h), angle = rect
            # Display rectangle
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
            cv2.polylines(img, [box], True, (255, 0, 0), 2)
        cv2.imshow("sfd",img)
        cv2.waitKey(1)
        
        ## masks
        # mask1 = obj1.apply(img)
        # # mask2 = obj2.apply(img)
        # cv2.imshow("obj1", mask1)
        # # cv2.imshow("obj2", mask2)
        # cv2.waitKey(1)




    cv2.destroyAllWindows()
    ep_camera.stop_video_stream()
    # ep_camera.start_video_stream(display=True, resolution=camera.STREAM_720P)
    # while True: 
    #     ep_gripper.open(power=100)
    #     time.sleep(2)
    #     ep_gripper.close(power=100)
    #     time.sleep(2)
    
    # while True:
    #     time.sleep(10)
    # ep_camera.stop_video_stream()

    # ep_robot.close()