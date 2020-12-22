import os
import cv2
import datetime


def get_length(filename):
    cap = cv2.VideoCapture(filename)
    # OpenCV2 version 2 used "CV_CAP_PROP_FPS"
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count/fps
    return duration


total_time = float(0)

start_path = r'H:\Course\Archive-5981\Online Account Cracking Course'
for dirpath, dirname, filenames in os.walk(start_path):
    for f in filenames:
        fp = os.path.join(dirpath, f)
        if fp.lower().endswith(('.avi', '.mpg', '.mpeg', '.wmv', '.mov', '.divx', '.mp4', '.m4v', '.asf')):
            total_time += get_length(fp)


conversion = datetime. timedelta(seconds=total_time)
print(conversion)
