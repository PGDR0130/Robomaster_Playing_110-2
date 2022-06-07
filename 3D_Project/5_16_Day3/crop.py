import cv2

x=0
y=0

w=1280
h=630

i = 1
while (i <= 1005):
    img = cv2.imread(f"{i}.jpg")
    cropImg = img[y:y+h, x:x+w]

    cv2.imwrite(f'{i}.jpg', cropImg)
    i += 1
    print(i)
