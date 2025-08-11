from ultralytics import YOLO
from PIL import Image
# Load a model
model = YOLO("yolo11n.pt")  # load an official model
# model = YOLO("path/to/best.pt")  # load a custom model

# Predict with the model
results = model("E:\\Github\\codingINCV\\Ultralytics\\image.png")  # predict on an image

# Access the results
for result in results:
    xywh = result.boxes.xywh  # center-x, center-y, width, height
    xywhn = result.boxes.xywhn  # normalized
    xyxy = result.boxes.xyxy  # top-left-x, top-left-y, bottom-right-x, bottom-right-y
    xyxyn = result.boxes.xyxyn  # normalized
    names = [result.names[cls.item()] for cls in result.boxes.cls.int()]  # class name of each box
    confs = result.boxes.conf  # confidence score of each box

# for item in result.names:
#     print(item)
# for r in results:
#     print(r.boxes)

def visualize():
    # Visualize the results
    for i, r in enumerate(results):
        # Plot results image
        im_bgr = r.plot()  # BGR-order numpy array
        im_rgb = Image.fromarray(im_bgr[..., ::-1])  # RGB-order PIL image

        # Show results to screen (in supported environments)
        r.show()

        # Save results to disk
        r.save(filename=f"results{i}.jpg")



visualize()