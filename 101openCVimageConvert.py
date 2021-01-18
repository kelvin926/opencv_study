import cv2 #cv2 모듈 입력

print("OpenCV version:") 
print(cv2.__version__) #opencv 버전
 
img = cv2.imread("nomadProgramerIcon.png")
# imread : 이미지 입력 함수 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 # cvtcolor : 컬러 변경 함수

cv2.imshow("nomadProgramer", img) #이미지 쇼 (윈도우에)
cv2.imshow("nomadProgramer - gray", gray) #이미지 쇼 (윈도우에)
 
cv2.waitKey(0) #아무 키나 입력 (그 전까지는 아무런 진행 X)
cv2.destroyAllWindows() #활성화 된 윈도우 창 제거