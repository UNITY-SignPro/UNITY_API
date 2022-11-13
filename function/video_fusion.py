import cv2
import os.path
from function.DataManage import search_link
import time

def checkVideo(words):
    # C:\Users\dlalsdn\Desktop\Project\TeamUntiy_Front\public\tmp_video

    # __videopath__ = os.path.abspath(f'./tmp_video/{" ".join(words)}.avi')
    __videopath__ = os.path.abspath(f'C:/Users/dlalsdn/Desktop/Project/TeamUntiy_Front/public/tmp_video/{" ".join(words)}.mp4')
    if not os.path.isfile(__videopath__):
        makeVideo(words)
    return __videopath__

def makeVideo(words):
    # __videopath__ = os.path.abspath(f'./tmp_video/{" ".join(words)}.avi')
    __videopath__ = os.path.abspath(f'C:/Users/dlalsdn/Desktop/Project/TeamUntiy_Front/public/tmp_video/{" ".join(words)}.mp4')

    # __filename__ = f'./tmp_video/{" ".join(words)}.avi'
    out = cv2.VideoWriter(__videopath__, cv2.VideoWriter_fourcc(*'mp4v'), 30, (700, 466))
    # out = cv2.VideoWriter(__videopath__, cv2.VideoWriter_fourcc(*'mp4v'), 29.97002997002997, (700, 466))
    for idx in range(len(words)):
        cap = cv2.VideoCapture(search_link(words[idx])[1])
        # print(cap.get(cv2.CAP_PROP_FPS))
        frame_pass = False if cap.get(cv2.CAP_PROP_FPS) < 30 else True; frame_cnt = 0
        while True:
            ret,frame = cap.read()
            frame_cnt += 1
            if not ret: break
            if frame_pass and frame_cnt % 2 == 1: continue
            out.write(frame)

# makeVideo(['호박', '홍콩', '가마'])
# ENDED_TIME = time.time()
# print('Working Time: ', ENDED_TIME - STARTED_TIME)

