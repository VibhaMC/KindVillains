import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import text_to_speech
import pyttsx3

def estimate_distance(pixel_width, known_width, focal_length):
    return (known_width * focal_length) / pixel_width

def object_detect():
    video = cv2.VideoCapture(0)
    label = []

    # Known width of the object in meters
    known_width = 0.2
    # Focal length of the camera in pixels
    focal_length = 500

    while True:
        ret, frame = video.read()
        bbox, label, conf = cv.detect_common_objects(frame)
        output_image = draw_bbox(frame, bbox, label, conf)

        for i, obj_label in enumerate(label):
            width = bbox[i][2]  # Width of the object's bounding box in pixels

            # Estimate distance
            distance = (known_width * focal_length) / width
            distance = round(distance, 2)

            print("Object:", obj_label)
            print("Distance:", distance, "meters")

            object_name = obj_label
            text_to_speech.text(object_name, str(distance))

        cv2.imshow("ObjDetect", output_image)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video.release()
    cv2.destroyAllWindows()


