from ultralytics import YOLO
import os
# Load a model
model = YOLO('./runs/detect/train7/weights/best.pt')  # build a new model from scratch  

# get the path/directory
folder_dir = "./License Plate Recognition.v4-resized640_aug3x-accurate.yolov8/test/images"

# Run inference on the source
model.predict(source="./data/train/image/Car-20License-20Plate-20Detection-20_-20Kaggle_jpg.rf.f0b8d1aeb37dad6753b77d067bd4a59d.jpg",save=True,save_crop=True)