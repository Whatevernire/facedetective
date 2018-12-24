import face_recognition
import cv2
import time
import sqlite3


conn = sqlite3.connect('new2.db')
cur = conn.cursor()

k=0
nol = 0
odin = 1
dva = 2
tri = 3
video_capture = cv2.VideoCapture(0)


face_locations = []

def main():
    while True:

        # Взятие кадра с видео
        ret, frame = video_capture.read()

        # Уменьшение кадра до 1/4 для быстрого распознования лица
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Конвертация изображения из BGR color (which OpenCV uses) в RGB color (с которым работает библиотека)
        rgb_small_frame = small_frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_small_frame)
        if face_locations.__len__() >= 1:
            print('обнаружил лица')
            fuck_encode = face_recognition.face_encodings(rgb_small_frame)
            k = 0
            for face_encoda in fuck_encode:
                print('начинаю добавлять фото в бд')
                text_encoda = str(face_encoda.tolist())
                # cur.execute('''insert into encodings values (?)''', (text_encoda))
                print(type(text_encoda))
                if k == 3:
                    cur.execute('''update encodings set encode = (?) where number = (?)''', (text_encoda,tri,))
                    k=+1
                if k == 2:
                    cur.execute('''update encodings set encode = (?) where number = (?)''', (text_encoda,dva,))
                    k=+1
                if k == 1:
                    cur.execute('''update encodings set encode = (?) where number = (?)''', (text_encoda,odin,))
                    k=+1
                if k == 0:
                    cur.execute('''update encodings set encode = (?) where number = (?)''', (text_encoda,nol,))
                    k=+1
                conn.commit()
                time.sleep(0.5)
                print('фото добавлено')
                if k >= 3:
                    k = 0
                    break
            k=0



if __name__ == "__main__":
    main()
