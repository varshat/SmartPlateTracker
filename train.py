from ultralytics import YOLO
# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model
results = model.train(data="License Plate Recognition.v4-resized640_aug3x-accurate.yolov8/data.yaml", epochs=5)  # train the model