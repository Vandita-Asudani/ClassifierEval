from ultralytics import YOLO
model = YOLO("F:/Yolo5v/5best.pt", "v5")
prob = model.predict("F:\Yolo5v\920.jpg", save=True)

