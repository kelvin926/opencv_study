import cv2
import numpy as np

model_name = './model/res10_300x300_ssd_iter_140000.caffemodel'
prototxt_name = './model/deploy.prototxt.txt'
min_confidence = 0.3
file_name = "./image/marathon_01.jpg"

def detectAndDisplay(frame):
    model = cv2.dnn.readNetFromCaffe(prototxt_name, model_name)

    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
            (300, 300), (104.0, 177.0, 123.0))

    model.setInput(blob)
    detections = model.forward()

    print(detections[0, 0])
    print(detections.shape[2])

    for i in range(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]

            if confidence > min_confidence:
                    box = detections[0, 0, i, 3:7] * np.array([width, height, width, height])
                    (startX, startY, endX, endY) = box.astype("int")
                    print(i, confidence,detections[0, 0, i, 3], startX, startY, endX, endY)
     
                    text = "{:.2f}%".format(confidence * 100)
                    y = startY - 10 if startY - 10 > 10 else startY + 10
                    cv2.rectangle(frame, (startX, startY), (endX, endY),
                            (0, 255, 0), 2)
                    cv2.putText(frame, text, (startX, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    cv2.imshow("Face Detection by dnn", frame)
    
    
print("OpenCV version:")
print(cv2.__version__)
 
img = cv2.imread(file_name)
print("width: {} pixels".format(img.shape[1]))
print("height: {} pixels".format(img.shape[0]))
print("channels: {}".format(img.shape[2]))

(height, width) = img.shape[:2]

cv2.imshow("Original Image", img)

detectAndDisplay(img)

cv2.waitKey(0)
cv2.destroyAllWindows()
