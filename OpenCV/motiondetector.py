import cv2,time
first_frame = None
video = cv2.VideoCapture(0)
while True:
    check,frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)
    if first_frame is None:
        first_frame = gray
        continue
    delta_frame = cv2.absdiff(first_frame,gray)
    thresh_delta = cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)
    thresh_delta = cv2.dilate(thresh_delta, None, iterations=0 )
    (_,cnts,_) = cv2.findContours(thresh_delta.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in cuts:
        if cv2.contourArea(contour) < 1000:
            continue

