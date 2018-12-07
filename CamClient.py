import face_recognition
import cv2
import time

video_capture = cv2.VideoCapture(0)


face_locations = []

while True:

    # Взятие кадра с видео
    ret, frame = video_capture.read()

    # Уменьшение кадра до 1/4 для быстрого распознования лица
    small_frame = cv2.resize(frame, (0, 0), fx=1, fy=1)

    # Конвертация изображения из BGR color (which OpenCV uses) в RGB color (с которым работает библиотека)
    rgb_small_frame = small_frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_small_frame)
    if face_locations.__len__() == 1:
        cv2.imwrite('new.png',rgb_small_frame)
        print('foto sdelano')
        time.sleep(3)


