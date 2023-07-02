import os
import cv2
import numpy as np
import pygame as pygame
from ultralytics import YOLO


net = YOLO("yolov8n.pt")

classes = [
    'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck',
    'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench',
    'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra',
    'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis',
    'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard',
    'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon',
    'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog',
    'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table',
    'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave',
    'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
    'teddy bear', 'hair drier', 'toothbrush'
]

# play "alarm.mp4"
pygame.init()
pygame.mixer.init()
alarm_played = False
pygame.mixer.music.load(os.path.abspath('alarm2.mp3'))

COLORS = np.random.uniform(0, 255, size=(len(classes), 3))

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # reading frames from webcam
    if not ret:
        break

    outs = net(frame, task='detect', iou=0.6, conf=0.3, show=True, save_conf=True, classes=[15,16,57,59], boxes=True)

    pred_classes = [classes[int(i.item())] for i in outs[0].boxes.cls]
    pred_bbox = [i.tolist() for i in outs[0].boxes.xywh]
    pred_conf = [i.item() for i in outs[0].boxes.conf]


    length = len(pred_classes)
    dog_boxes = []
    couch_boxes = []
    dog_flag, couch_bed_flag = 0, 0

    for i in range(length):
        if pred_classes[i] in ['dog', 'cat']:
            dog_boxes.append((round(pred_bbox[i][0]), round(pred_bbox[i][1]), round(pred_bbox[i][0] + pred_bbox[i][2]), round(pred_bbox[i][1] + pred_bbox[i][3])))
            dog_flag = 1
        elif pred_classes[i] in ['couch', 'bed']:
            couch_boxes.append((round(pred_bbox[i][0]), round(pred_bbox[i][1]), round(pred_bbox[i][0] + pred_bbox[i][2]), round(pred_bbox[i][1] + pred_bbox[i][3])))
            couch_bed_flag = 1

    if alarm_played and (dog_flag == 0 or couch_bed_flag == 0):
        pygame.mixer.music.stop()
        alarm_played = False
        # dog_boxes = [(0, 0, 0, 0)]
        # couch_boxes = [(0, 0, 0, 0)]

    for dog_box in dog_boxes:
        for couch_box in couch_boxes:
            if dog_box[3] < couch_box[3] - ((couch_box[3] - couch_box[1]) * 0.4) and ((dog_box[0] > couch_box[0] and dog_box[0] < couch_box[2]) or (dog_box[2] > couch_box[0] and dog_box[2] < couch_box[2])):
                while not alarm_played:
                    pygame.mixer.music.play(-1)  # play in a loop
                    alarm_played = True


    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()
