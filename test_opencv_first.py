# Yujin.jpg 파일로 진행. 각 단계 마다 키를 눌러야지 진행되게 코딩.
import cv2
import numpy as np
# [1단계] opencv 버전 출력. 사진 출력. 사진의 너비와 높이 출력. 사진의 중심 좌표 출력.
print("버전은:"+ cv2.__version__)

img = cv2.imread("yujin.jpg")
cv2.imshow("yujin basic file", img)
yujin_height = img.shape[0]
yujin_width = img.shape[1]
yuzin_color_channel = img.shape[2]

if yuzin_color_channel == 3:
    yuzin_color_channel_text = "RGB"
else:
    yuzin_color_channel_text = "Unknown"
print("사진의 높이: {} , 사진의 너비: {} , 사진의 컬러 : {}".format(yujin_height, yujin_width, yuzin_color_channel_text))

center = (yujin_height//2, yujin_width//2) #나머지 반환. int형 출력.

print ("사진의 중심(x,y): ({},{})".format(center[0], center[1]))

cv2.waitKey(0)
cv2.destroyAllWindows()

# [1단계] jpg파일을 png파일로 변환하여 저장. 사진 중심의 색상 채널 값 출력. 사진 중심에 DOT화 하기, 점 부분만 따로 이미지 출력. 점 부분의 색 변환.
cv2.imwrite("yuzin_pngcvt.png", img)
print("파일을 png로 변환 완료! 해당 파일을 출력합니다!")

img_png = cv2.imread("yuzin_pngcvt.png")
cv2.imshow("png cvt photo", img_png)

(b, g, r) = img[center]
print("사진 중심의 RGB 값은-> RED: {}, GREEN: {}, BLUE: {}".format(r, g, b))

dot = img[center[0]-100:center[0]+100, center[1]-100:center[1]+100]

cv2.imshow("DOT", dot)

img[center[0]-100:center[0]+100, center[1]-100:center[1]+100] = (255,255,255)

cv2.imshow("dotted", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# [1단계] 사각형, 원, 선, 텍스트 각각 하나씩 그려서 출력.
cv2.rectangle(img, (100,100), (200,200), (255,0,255), thickness=5)

cv2.circle(img, (250,250), 50, (0,255,255), thickness=5)

cv2.line(img, (300,300), (500,500), (0,255,0), thickness=5)

cv2.putText(img, "yujin Hello!", (800,800), cv2.FONT_HERSHEY_COMPLEX, 5, (255,255,0), thickness=5)

cv2.imshow("DRAW", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# [1단계] 이미지를 위로,아래로,양옆으로 움직이게 해서 출력.
move = np.float32([[1, 0, +100], [0, 1, +100]]) # 변환 행렬. 좌우/상하
moved = cv2.warpAffine(img, move, (yujin_width, yujin_height)) 
cv2.imshow("right: +, left - down: +, up: - ", moved)

cv2.waitKey(0)
cv2.destroyAllWindows() 

# [1단계] 이미지를 회전. 이미지를 축소, 이미지를 확대, 이미지를 반전.

img = cv2.imread("yujin.jpg") #이미지 재 로딩

rotate = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated = cv2.warpAffine(img, rotate, (yujin_height, yujin_width))
cv2.imshow("90 degree clockwise", rotated)
cv2.waitKey(0)

def zoomdef(want_height): # 세로 크기 요청에 따라 원본 비율 그대로 가로x세로 값 리턴.
    ratio = want_height/img.shape[0]
    zoom = (int(img.shape[1]*ratio), int(want_height)) #가로x세로
    return zoom

# print(zoomdef(480))
# print(zoomdef(720)) #Debug

want_height = 1080
fhd = cv2.resize(img, zoomdef(want_height), interpolation=cv2.INTER_AREA)
cv2.imshow("FHD downscale", fhd)
cv2.waitKey(0)

want_height = 1440
qhd = cv2.resize(img, zoomdef(want_height), interpolation=cv2.INTER_NEAREST)
cv2.imshow("QHD upscale", qhd)
cv2.waitKey(0)


flipped = cv2.flip(img, 1)
cv2.imshow("flipped", flipped)

cv2.waitKey(0)
cv2.destroyAllWindows() 

# [1단계] 마스크를 만들고, 마스크와 마스크된 사진 출력.

mask = np.zeros((yujin_height, yujin_width), dtype = "uint8")

def zoom_center(now_height):
    (w, h) = zoomdef(now_height)
    return (w, h)

cv2.circle(mask, zoom_center(want_height), 100, (255,255,255), -1)

cv2.imshow("mask", mask)

masked = cv2.bitwise_and(img, img, mask = mask)

cv2.imshow("masked", masked)

cv2.waitKey(0)
cv2.destroyAllWindows() 

# [1단계] 각각의 색 영역별로 출력. 여러 필터 적용해서 출력.
(Blue, Green, Red) = cv2.split(img)
cv2.imshow("Blue", Blue)
cv2.imshow("Green", Green)
cv2.imshow("Red", Red)

cv2.waitKey(0)
cv2.destroyAllWindows() 
# ------------------------------
img = cv2.imread('yujin.jpg') #이미지 재 로딩

resize = cv2.resize(img, zoomdef(480))

gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)

hsv = cv2.cvtColor(resize, cv2.COLOR_BGR2HSV)

lab = cv2.cvtColor(resize, cv2.COLOR_BGR2LAB)

cv2.imshow('gray', gray)
cv2.imshow('hsv', hsv)
cv2.imshow('lab', lab)

cv2.waitKey(0)
cv2.destroyAllWindows() 

# [1단계] 각각의 색 영역별로 출력한 상태에 더 보기 편하도록 색 입혀서 출력. 
zeros = np.zeros(img.shape[:2], dtype = "uint8")

cv2.imshow('blue', cv2.resize(cv2.merge([Blue, zeros, zeros]), zoomdef(480)))
cv2.imshow('green', cv2.resize(cv2.merge([zeros, Green, zeros]), zoomdef(480)))
cv2.imshow('red', cv2.resize(cv2.merge([zeros, zeros, Red]), zoomdef(480)))

cv2.waitKey(0)
cv2.destroyAllWindows() 

# [1단계] 나눈 색 사진들을 조합하여 원본과 같은 사진 출력.
cv2.imshow('BGR', cv2.resize(cv2.merge((Blue,Green,Red)), zoomdef(480)))

cv2.waitKey(0)
cv2.destroyAllWindows() 