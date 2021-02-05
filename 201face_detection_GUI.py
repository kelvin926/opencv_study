import cv2
import numpy as np
from tkinter import *
from PIL import Image #OpenCV의 numpy 형식 이미지를 표시하려면 PIL 모듈을 사용
from PIL import ImageTk
from tkinter import filedialog

face_cascade_name = '../opencv/haarcascades/haarcascade_frontalface_alt.xml'
eyes_cascade_name = '../opencv/haarcascades/haarcascade_eye_tree_eyeglasses.xml'
file_name = 'image/marathon_01.jpg'
title_name = 'Haar cascade object detection'
frame_width = 500

def selectFile():
    file_name =  filedialog.askopenfilename(initialdir = "./image",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    print('File name : ', file_name) #파일 리딩 부분.
    read_image = cv2.imread(file_name)
    (height, width) = read_image.shape[:2] #세로, 가로
    frameSize = int(sizeSpin.get()) #조절바로 받은 값
    ratio = frameSize / width #비율 
    dimension = (frameSize, int(height * ratio))
    read_image = cv2.resize(read_image, dimension, interpolation = cv2.INTER_AREA) #리사이징
    image = cv2.cvtColor(read_image, cv2.COLOR_BGR2RGB) #RGB화
    image = Image.fromarray(image) #PIL.Image 모듈의 fromarray 함수를 활용해 Numpy 배열을 Image 객체로 변환
    imgtk = ImageTk.PhotoImage(image=image) #PIL.ImageTk 모듈의 PhotoImage 함수를 활용해 tkinter와 호환되는 객체로 변환
    detectAndDisplay(read_image)



def detectAndDisplay(frame):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)
    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        
        center = (x + w//2, y + h//2)
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 4)
        faceROI = frame_gray[y:y+h,x:x+w]
        #-- In each face, detect eyes
        eyes = eyes_cascade.detectMultiScale(faceROI)
        for (x2,y2,w2,h2) in eyes:
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.25))
            frame = cv2.circle(frame, eye_center, radius, (255, 0, 0 ), 4)
    #cv2.imshow('Capture - Face detection', frame)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    imgtk = ImageTk.PhotoImage(image=image)
    detection.config(image=imgtk)
    detection.image = imgtk
    

#main
main = Tk()
main.title(title_name)
main.geometry()

#이미지 읽고, 리사이징 하는 부분.
read_image = cv2.imread("image/marathon_01.jpg")
(height, width) = read_image.shape[:2]
ratio = frame_width / width
dimension = (frame_width, int(height * ratio))
read_image = cv2.resize(read_image, dimension, interpolation = cv2.INTER_AREA)


image = cv2.cvtColor(read_image, cv2.COLOR_BGR2RGB)
image = Image.fromarray(image) #numpy객체를 image객체로 변환.(cv로 읽어드린 이미지는 numpy타입이므로.) [PIL타입]
imgtk = ImageTk.PhotoImage(image=image)

face_cascade_name = '../opencv/haarcascades/haarcascade_frontalface_alt.xml' #face
eyes_cascade_name = '../opencv/haarcascades/haarcascade_eye_tree_eyeglasses.xml' #eyes

face_cascade = cv2.CascadeClassifier() #분류기 대입
eyes_cascade = cv2.CascadeClassifier() #분류기 대입

#-- 1. Load the cascades
if not face_cascade.load(cv2.samples.findFile(face_cascade_name)):
    print('--(!)Error loading face cascade')
    exit(0)
if not eyes_cascade.load(cv2.samples.findFile(eyes_cascade_name)):
    print('--(!)Error loading eyes cascade')
    exit(0)



label=Label(main, text=title_name)
label.config(font=("Courier", 18))
label.grid(row=0,column=0,columnspan=4)

sizeLabel=Label(main, text='Frame Width : ')                
sizeLabel.grid(row=1,column=0)

sizeVal  = IntVar(value=frame_width)
sizeSpin = Spinbox(main, textvariable=sizeVal,from_=0, to=2000, increment=100, justify=RIGHT)
sizeSpin.grid(row=1, column=1)

Button(main,text="File Select", height=2,command=lambda:selectFile()).grid(row=1, column=2, columnspan=2, sticky=(W, E))

detection=Label(main, image=imgtk)
detection.grid(row=2,column=0,columnspan=4)

detectAndDisplay(read_image)

main.mainloop()
