from ultralytics import YOLO
model = YOLO("F:\Yolo8v\8best.pt", "v8")
prob = model.predict("F:\Yolo8v\920.jpg", save=True)

