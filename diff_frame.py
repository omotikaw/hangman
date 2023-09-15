import cv2
import numpy as np
cap = cv2.VideoCapture("movie/m1.mp4")
ret, frame = cap.read()
h, w, ch = frame.shape
# 背景差分用の背景
frame_back = np.zeros((h,w,ch), dtype=np.float32)
while True:
    ret, frame = cap.read()
    if ret == False:
        break
    # 現在のフレームと背景とで差分を取る
    frame_diff = cv2.absdiff(frame.astype(np.float32), frame_back)
    # 背景を少しずつ現在のフレームに近づけたものを新たな背景とする
    cv2.accumulateWeighted(frame, frame_back, 0.03)
    cv2.imshow("img", frame_diff.astype(np.uint8))
    if cv2.waitKey(10) == 27:
        break
cv2.destroyAllWindows()