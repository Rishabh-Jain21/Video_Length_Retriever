import os
import cv2
import datetime
import argparse
from concurrent.futures import Future, ThreadPoolExecutor
from typing import List

# Function to get length of one video in seconds
def get_length(filename)->float:
    cap = cv2.VideoCapture(filename)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration:float = frame_count/fps
    return duration


parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', type=str, metavar='',
                    required=True, help="Folder Path")

args = parser.parse_args()
total_time: float = 0.0  # Variable to store total time of all videos


start_path: str = args.path
with ThreadPoolExecutor(max_workers=5) as executor:
    processes: List[Future] = []
    for dirpath, dirname, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if fp.lower().endswith(('.avi', '.mpg', '.mpeg', '.wmv', '.mov', '.divx', '.mp4', '.m4v', '.asf')):
                try:
                    # appending the future object in a list which will be used later to add total time
                    processes.append(executor.submit(get_length, fp))
                except:
                    pass
time_lst: List[float] = list(map(lambda x: x.result(), processes))
total_time = sum(time_lst) #adding all the vallues
conversion = datetime.timedelta(seconds=total_time) # converting seconds to readable format
print(conversion)
