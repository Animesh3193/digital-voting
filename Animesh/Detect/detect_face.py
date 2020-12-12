import cv2 as cv
import argparse
from datetime import datetime


def get_parsed_arguments():
    parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')
    parser.add_argument('--face_cascade', help='Path to face cascade.',
                        default='data\\haarcascades\\haarcascade_frontalface_alt.xml')
    parser.add_argument('--camera', help='Camera divide number.', type=int, default=0)
    args, unknown_parms = parser.parse_known_args()
    return args.face_cascade, args.camera


def detect_and_display():
    face_cascade = cv.CascadeClassifier()
    face_cascade_name, camera_device = get_parsed_arguments()
    # -- 1. Load the cascades
    if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
        print('--(!)Error loading face cascade')
        exit(0)

    # -- 2. Read the video stream
    video_capture = cv.VideoCapture(camera_device)
    if not video_capture.isOpened:
        print('--(!)Error opening video capture')
        exit(0)

    while True:
        ret, frame = video_capture.read()
        if frame is None:
            print('--(!) No captured frame -- Break!')
            break
        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame_gray = cv.equalizeHist(frame_gray)
        bounding_box = []
        #-- Detect faces
        faces = face_cascade.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        for person in faces:
            bounding_box = list(person)
            frame = cv.rectangle(frame,
                                 (bounding_box[0], bounding_box[1]),
                                 (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]),
                                 (0, 255, 0),
                                 2)
            cv.imshow('Capture - Face detection', frame)
        key = cv.waitKey(1)
        if key == ord('c'):
            try:
                print('Coming Here capture')
                crop_img = frame[bounding_box[1]: bounding_box[1] + bounding_box[3],
                           bounding_box[0]: bounding_box[0] + bounding_box[2]
                           ]  # Crop from x, y, w, h -> 100, 200, 300, 400
                # Writing Image to BPM Format
                date = datetime.now().strftime('%m_%d_%YT%H_%M_%S')
                image_name = f"Saved_Images\\Register_{date}_.bmp"
                print(image_name)
                cv.imwrite(image_name, crop_img)
                break
            except Exception as e:
                print('No Image Captured')
        elif key == ord('q'):
            print('Coming Here Quit')
            break
    video_capture.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    detect_and_display()