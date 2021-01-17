import cv2

print("OpenCV version:")
print(cv2.__version__)
 
img = cv2.imread("nomadProgramerIcon.png")
print("width: {} pixels".format(img.shape[1])) # shape 배열 -> 0: 너비, 1: 높이, 2: RGB 채널(3)
print("height: {} pixels".format(img.shape[0]))
print("channels: {}".format(img.shape[2]))
 
cv2.imshow("nomadProgramer", img)
 
cv2.waitKey(0)
cv2.imwrite("nomadProgramerIcon.jpg", img) # 이미지(png) 파일을 jpg 파일로 변환 [ imwrite : 이미지 쓰기 ]
cv2.destroyAllWindows()