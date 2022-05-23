import robomaster
import time
from robomaster import robot
from robomaster import camera
import cv2

# 1. x=200 y=75
# 2. x=200 y=200
# 3. x=100 y =100
# 4. x=0   y=200
poses = [[200, 75], [200, 200], [100, 100], [0, 200]]


if __name__ == '__main__':
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")

    ep_chassis = ep_robot.chassis

    # 指定麦轮速度
    speed = 30
    slp = 0.5

    # camera setup 
    ep_camera= ep_robot.camera
    # print(list(ep_camera.conf))
    ep_camera.start_video_stream(display=False)

    # arm setup
    ep_arm = ep_robot.robotic_arm
    ep_arm.recenter().wait_for_completed()

    ep_arm.moveto(x = 150, y = 150).wait_for_completed()

    i = 0
    while True:
        i += 1
        camera_img = ep_camera.read_cv2_image(strategy='newest')
        cv2.imshow('img', camera_img)
        cv2.waitKey(1)
        cv2.imwrite(f'scan/5_16_Day2_Images/{i}.jpg', camera_img)
        ep_chassis.drive_wheels(w1=30, w2=30, w3=30, w4=30)
        time.sleep(0.1)