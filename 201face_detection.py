import cv2
import numpy as np



# print("OpenCV version:")
# print(cv2.__version__)

img = cv2.imread("image/marathon_01.jpg")
print("width: {} pixels".format(img.shape[1]))
print("height: {} pixels".format(img.shape[0]))
print("channels: {}".format(img.shape[2]))

(height, width) = img.shape[:2]

cv2.imshow("Original Image", img)

# ******************************************

face_cascade_name = '../opencv/haarcascades/haarcascade_frontalface_alt.xml' #face haar
eyes_cascade_name = '../opencv/haarcascades/haarcascade_eye_tree_eyeglasses.xml' #eyes haar

face_cascade = cv2.CascadeClassifier() #함수 지정 [face]
eyes_cascade = cv2.CascadeClassifier() #함수 지정 [eyes]

def detectAndDisplay(frame):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #그레이로 전환
    frame_gray = cv2.equalizeHist(frame_gray) #히스토그램 평활화 (히스토그램을 좀 더 평탄하게 만들어줌.)
    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray) #그레이 사진에 여러 크기의 사물 감지. = 감지 될 때마다 값 출력.
    for (x,y,w,h) in faces:
        center = ((x + w)//2, (y + h)//2) #얼굴 센터, x:시작, w:끝부분 느낌.
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 4) #얼굴부분 사각형 draw. 여기서 프레임에 여러번 draw하기 위해 자기 자신 언급.
        faceROI = frame_gray[y:y+h,x:x+w] #얼굴 부분 ROI 지정.
        #-- In each face, detect eyes - 각각의 얼굴 속 눈 감지.
        eyes = eyes_cascade.detectMultiScale(faceROI) #얼굴 부분 ROI에 여러 크기의 사물 감지 = 감지될 때마다 값 출력.
        for (x2,y2,w2,h2) in eyes:
            eye_center = ((x + x2 + w2)//2, (y + y2 + h2)//2) #눈 가운데.
            radius = int(round((w2 + h2)*0.25)) #반지름.
            frame = cv2.circle(frame, eye_center, radius, (255, 0, 0 ), 4) #눈 부분에 서클 draw.
        cv2.imshow('Capture - Face detection', frame)


#-- 1. Load the cascades
if not face_cascade.load(cv2.samples.findFile(face_cascade_name)):
    print('--(!)Error loading face cascade')
    exit(0)
if not eyes_cascade.load(cv2.samples.findFile(eyes_cascade_name)):
    print('--(!)Error loading eyes cascade')
    exit(0)



#************************************
detectAndDisplay(img)


cv2.waitKey(0)
cv2.destroyAllWindows()

