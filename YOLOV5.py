# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 16:15:41 2023

@author: shrey
"""

# Hare Rama, Hare Krishna
# how to access the camera using opencv


import cv2
from ultralytics import YOLO
import torch

model = YOLO("yolo-Weights/yolov8s.pt")

# First, save an mp4
# Can I do it on a video?

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]

vid = cv2.VideoCapture(r"C:\Users\shrey\Downloads\TrainYOLO\video1.mp4")
fourCC    = int(vid.get(cv2.CAP_PROP_FOURCC))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = vid.get(cv2.CAP_PROP_FPS)
output_file_path = r"C:\Users\shrey\Downloads\TrainYOLO\outputvideo.mp4"
width = int(vid.get(3)) # gets the width
height =int(vid.get(4)) # gets the height

# problem with cv2.get(CAP_PROP_FRAME_WIDTH), vid.get(cv2.get(CAP_PROP_FRAME_WIDTH))
out = cv2.VideoWriter(output_file_path, fourcc, fps, (width, height))
# the third argument controls the frames per second


# cap.set(3, 480)
# cap.set(4, 640)

while (vid.isOpened()):
    ret, frame = vid.read()
    
    result = model(frame, stream = True) # detecting objects using YOLO method.
    
    for r in result:             # different property in each one
        boxes = r.boxes # finding every bounding box in the image
        
        for every_box in boxes:
            x1, y1, x2, y2 = every_box.xyxy[0]  # coordinates of the first (most) confident bounding box.
            
            # convert the coordinates to integers
            
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # has to be an integer
            
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
            
            
            class_name = (int) (every_box.cls[0])
            
            confidence_score = every_box.conf[0]
            
            confidence_score_percent = torch.round(torch.tensor([confidence_score * 100.0]), decimals = 0).item()
            
            boxText = f"{classNames[class_name]}: {confidence_score_percent}%"
            
            
            org = (x1, y1)  # coordinates of bottom left corner of the text string
            font = cv2.FONT_HERSHEY_COMPLEX
            fontScale = 0.6
            color = (0, 255, 255)
            thickness = 0.5
            
            cv2.putText((frame), boxText, org, font, fontScale, color)
            
    out.write(frame)
    cv2.imshow("Webcam", frame)
    
    if (cv2.waitKey(1) == ord('q')):
        break
    
vid.release()
out.release()
cv2.destroyAllWindows()
    

    
    


    
    

