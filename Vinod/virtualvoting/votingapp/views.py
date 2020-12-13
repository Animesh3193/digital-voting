from django.shortcuts import render, redirect
import cv2
import numpy as np
from django.http import StreamingHttpResponse
import threading
from django.views.decorators.gzip import gzip_page
import argparse
from datetime import datetime
# from .models import RegistrationPerson
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import cv2 as cv
from pathlib import Path
import os


# Create your views here.
arr = ['BJP', 'TRS', 'Congress', 'TDP', 'AIADMK', 'SP', 'BSP', 'BJD', 'RJD', 'NCP']
globalcnt = dict()

# Create your views here.


def index(request):
    mydictionary = {
        "arr" : arr
    }
    return render(request,'index.html',context=mydictionary)

def getquery(request):
    q = request.GET['party']
    if q in globalcnt:
        # if already exist then increment the value
        globalcnt[q] = globalcnt[q] + 1
    else:
        # first occurrence
        globalcnt[q] = 1
    mydictionary = {
        "arr" : arr,
        "globalcnt" : globalcnt
    }
    return render(request,'index.html',context=mydictionary)

def sortdata(request):
    global globalcnt
    globalcnt = dict(sorted(globalcnt.items(),key=lambda x:x[1],reverse=True))
    mydictionary = {
        "arr" : arr,
        "globalcnt" : globalcnt
    }
    return render(request,'index.html',context=mydictionary)



def response(request):
    return render(request, 'response_page.html')

def register(request):
    if request.method=='POST':
        print(request.method)
        first_name = request.method.POST('name', None)
        last_name = request.method.POST('last_name', None)
        aadhar = request.method.POST('aadhar', None)
        Date_of_birth = request.method.POST('Date_of_birth', None)
        password = request.method.POST('password', None)
        password2 = request.method.POST('password2', None)
        return JsonResponse({'success': 'True'})
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        print('Submit button clicked')
        aadhar = request.POST.get('aadhar')
        password = request.POST.get('password')
        print('Aadgar', aadhar, 'Password', password)
        response = redirect('/livwin/')
        return response
    else:
        return render(request, 'login.html')

def capture_image(request):
    return render(request, 'capture_image.html')

def cast_vote(request):
    return render(request, 'voting_page.html')



# class VideoCamera(object):
#     def __init__(self):
#         self.video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#         (self.grabbed, self.frame) = self.video.read()
#         threading.Thread(target=self.update, args=()).start()
#
#     def __del__(self):
#         self.video.release()
#
#     def get_frame(self):
#         image = self.frame
#         ret, jpeg = cv2.imencode('.jpg', image)
#         return jpeg #.tobytes()
#
#     def update(self):
#         while True:
#             (self.grabbed, self.frame) = self.video.read()
#
#
# cam = VideoCamera()
#
# def gen(camera):
#     parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')
#     parser.add_argument('--face_cascade', help='Path to face cascade.',
#                         default='D:\\AWS_Project_Py\\FACE_DETECT_RECOGNIZE\\virtualvoting\\data\\haarcascades\\haarcascade_frontalface_alt.xml')
#     args, unknown_parms = parser.parse_known_args()
#     face_cascade_name = args.face_cascade
#     face_cascade = cv2.CascadeClassifier()
#     while True:
#         frame = cam.get_frame()
#         if frame is None:
#             print('--(!) No captured frame -- Break!')
#             break
#         imgUMat = np.float32(frame)
#         frame_gray = cv2.cvtColor(imgUMat, cv2.COLOR_BGR2GRAY)
#         frame_gray = cv2.equalizeHist(frame_gray)
#         bounding_box = []
#         #-- Detect faces
#         faces = face_cascade.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
#         for person in faces:
#             bounding_box = list(person)
#             frame = cv2.rectangle(frame,
#                                  (bounding_box[0], bounding_box[1]),
#                                  (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]),
#                                  (0, 255, 0),
#                                  2)
#         key = cv2.waitKey(1)
#         if key == ord('c'):
#             try:
#                 print('Coming Here capture')
#                 crop_img = frame[bounding_box[1]: bounding_box[1] + bounding_box[3],
#                            bounding_box[0]: bounding_box[0] + bounding_box[2]
#                            ]  # Crop from x, y, w, h -> 100, 200, 300, 400
#                 # Writing Image to BPM Format
#                 date = datetime.now().strftime('%m_%d_%YT%H_%M_%S')
#                 image_name = f"D:\\AWS_Project_Py\\FACE_DETECT_RECOGNIZE\\virtualvoting\\Saved_Images\\Register_{date}_.bmp"
#                 print(image_name)
#                 cv2.imwrite(image_name, crop_img)
#                 break
#             except Exception as e:
#                 print('No Image Captured')
#         elif key == ord('q'):
#             print('Coming Here Quit')
#             break
#         yield(b'--frame\r\n'
#               b'Content-Type: image/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n\r\n')
#
#
# @gzip_page
# def livefeed(request):
#     try:
#         return StreamingHttpResponse(gen(VideoCamera()), content_type="multipart/x-mixed-replace;boundary=frame")
#     except:  # This is bad! replace it with proper handling
#         pass



def get_parsed_arguments():
    BASE_DIR = Path(__file__).resolve().parent.parent
    front_face_cascade_join_path = BASE_DIR.joinpath('data', 'haarcascades', 'haarcascade_frontalface_alt.xml')
    path_to_haar_cascade_file = None
    if front_face_cascade_join_path.is_file():
        path_to_haar_cascade_file = str(front_face_cascade_join_path.resolve())
    parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')
    parser.add_argument('--face_cascade', help='Path to face cascade.', default=path_to_haar_cascade_file)
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
                image_name = f"Register_{date}_.bmp"
                image_path = None
                BASE_DIR = Path(__file__).resolve().parent.parent
                image_savefolder = BASE_DIR.joinpath('Saved_Images')
                if not image_savefolder.is_dir():
                    os.mkdir(image_savefolder)
                image_path = str(image_savefolder.joinpath(image_name).resolve())
                print(image_path)
                cv.imwrite(image_path, crop_img)
                break
            except Exception as e:
                print('No Image Captured')
        elif key == ord('q'):
            print('Coming Here Quit')
            break
    video_capture.release()
    cv.destroyAllWindows()

def livefeed_window(request):
    try:
        detect_and_display()
        print('Success')
        response = redirect('/votenow/')
        return response
    except Exception as e:
        print(e)


