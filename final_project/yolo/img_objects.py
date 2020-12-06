# Resources used:
# https://pjreddie.com/darknet/yolo/
# https://github.com/pjreddie/darknet/
# https://docs.opencv.org/master/d6/d0f/group__dnn.html
# https://docs.opencv.org/master/db/deb/tutorial_display_image.html
# https://numpy.org/doc/stable/reference/generated/numpy.argmax.html
# https://arxiv.org/pdf/1506.02640v5.pdf (Research Paper about YOLO)
# https://arxiv.org/pdf/1405.0312.pdf (Research Paper about COCO)

import cv2
import time
import numpy as np


def img_object_detection(img_path):
    """Running YOLO on an image to detect objects
    :param img_path: path of image to analyse
    :return: object(s) detected
    :rtype: list
    """

    # Files from Darknet
    config = "final_project/yolo/cfg/yolov3.cfg"
    weights = "final_project/yolo/weights/yolov3.weights"

    # Reads network model stored in Darknet model files
    # OpenCV dnn module is used to load YOLO network
    net = cv2.dnn.readNetFromDarknet(config, weights)

    # Using Common Objects in Context (COCO) Labels
    # (https://cocodataset.org/)
    coco_label = (
        open("final_project/yolo/coco/coco.names").read().strip().split("\n")
    )

    # Reads image from provided path
    read_img = cv2.imread(img_path)

    # Get the number of rows and columns of the image
    img_row, img_col = read_img.shape[:2]

    # Creating a 4-dimensional blob from image
    # SwapRB to True increase classification accuracy
    blob = cv2.dnn.blobFromImage(read_img, (1 / 255), (416, 416), swapRB=True)

    # Putting blob as the input of the network
    net.setInput(blob)

    # Getting each layer name
    layer_name = net.getLayerNames()
    layer_name = [layer_name[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    # Timing network output
    time_start = time.perf_counter()
    print("Starting YOLO analysis...")
    outputs = net.forward(layer_name)
    time_stop = time.perf_counter() - time_start
    print(f"YOLO ran for: {time_stop:.2f}s")

    grid, probabilities, labels = [], [], []

    # Find each single output
    # This for loop is based on information from darknet's code and opencv
    for output in outputs:

        # Find each single detection in output
        for detection in output:

            # Get probability score and label of the detection
            score = detection[5:]
            label = np.argmax(score)
            prob = score[label]

            # Selecting only detections that are superior to 50% probability
            # Anything below 50% is ignored as probability is too low
            # You can increase this to higher or lower probability if needed
            if prob > 0.5:

                # Working on each bounding box of the grid created by YOLO
                grid_box = detection[:4] * np.array([img_col, img_row, img_col, img_row])
                (X, Y, width, height) = grid_box.astype("int")
                x = X - (width / 2)
                y = Y - (height / 2)

                # Appending to the lists
                probabilities.append(float(prob))
                labels.append(label)
                grid.append([int(x), int(y), int(width), int(height)])

    # Performs Non Maximum Suppression given boxes and corresponding scores.
    # This filters the boxes in the image grid.
    # It keeps only the ones with the highest probability
    NMS = cv2.dnn.NMSBoxes(grid, probabilities, 0.5, 0.5)

    # If at least one object has been detected
    if len(NMS) > 0:

        # List objects where it stores the coco labels detected in the image
        objects = []

        # Add each object detected to the list objects
        for i in NMS.flatten():
            objects += [
                f"{coco_label[labels[i]]}"
            ]
        # Potential for future improvement if needed: regroup same labels together + add a count for them

        # How many objects were found
        print("YOLO found", len(objects), "objects")
        # List all objects found even if the label is the same
        # e.g. if two dogs are detected it will list dog twice
        print("The objects are:\n", objects)
        return objects

    # If no object has been detected
    else:
        print("No object detected in the picture.")
        return None
