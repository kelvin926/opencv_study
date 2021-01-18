import cv2
import numpy as np

print("OpenCV version:")
print(cv2.__version__)
 
img = cv2.imread("nomadProgramerIcon.png")
print("width: {} pixels".format(img.shape[1]))
print("height: {} pixels".format(img.shape[0]))
print("channels: {}".format(img.shape[2]))

(height, width) = img.shape[:2] # 높이, 너비 값 배열 0~1 번째 값 가져 옴.
center = (width // 2, height // 2) # 몫을 반환하는 나누셈, 센터를 구함.
# print("센터는 {} 입니다".format(center))

cv2.imshow("nomadProgramer", img)

move = np.float32([[1, 0, 100], [0, 1, 100]]) # 넘파이 행렬.(수치 해석을 위함.) float32 : 부동소수형 / 앞 부분은 위,아래 조정 값 (+:아래) / 뒷부분은 양 옆 조정 값.(+:오른쪽)
# 2X3의 이차원 행렬. [[1,0,x축이동],[0,1,y축이동]] 형태의 float32 type의 numpy array.

moved = cv2.warpAffine(img, move, (width, height)) # (이미지, 변환 행렬(move), 출력 이미지 사이즈.) warpAffine : 이미지의 위치 변경하는 변환.
cv2.imshow("아래로: +, 위로: - and 오른쪽: +, 왼쪽 - ", moved) #주의!!!! 반환 값 잘 확인하기.

rotate = cv2.getRotationMatrix2D(center, 90, 1.0) #(중앙 좌표, 시계 반대 방향(+)각도, 확대 정도(xx배).)
rotated = cv2.warpAffine(img, rotate, (width, height)) # (이미지, 변환 행렬(rotate), 출력 이미지 사이즈.) warpAffine : 이미지의 위치 변경하는 변환.
cv2.imshow("Rotated clockwise degrees", rotated) #주의!!!! 반환 값 잘 확인하기.

ratio = 200.0 / width # 목표 픽셀의 너비 상대 비율을 ratio.
dimension = (200, int(height * ratio)) # 원본 비율을 맞추기 위해, 너비에 적용된 배율만큼 세로에도 적용 함.

resized = cv2.resize(img, dimension, interpolation = cv2.INTER_AREA) # 리사이즈. (이미지, 목표 사진 해상도, 보간법[약간 사이즈를 늘리고 줄일 때 픽셀 처리 방법.])

# INTER_AREA: 픽셀영역 관계를 이용한 resampleing방법 원래 크기 보다 줄여줄 때 유용하다. 

# INTER_LINEAR: (default value) bilinear

# INTER_NEAREST: nearest_neighbor(size 크게 할때)

# INTER_CUBIC: 4x4 픽셀에 적용된다. (bicubic interpolation)

# INTER_LANCZOS4: 8x8 픽셀에 적용된다. (LANCZOS4 interpolation)

cv2.imshow("Resized", resized)

flipped = cv2.flip(img, 1) # 좌우 반전 :1, 상하 반전: 0, 둘 다: 0
cv2.imshow("Flipped Horizontal 1, Vertical 0, both -1 ", flipped)

cv2.waitKey(0)
cv2.destroyAllWindows()
