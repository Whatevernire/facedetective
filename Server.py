import sqlite3
import numpy as np
import face_recognition
import time
import cv2
# Подключаемся к базе и создаем курсор
conn = sqlite3.connect('new2.db')
cur = conn.cursor()

# Создаем хранилище всех имеющихся лиц и их
baza_lic = []
imena = []
baza_lic_res = []
c4et4ik = True

# Выгружаем все имена из базы данных

cur.execute('''select count(names) from face''')
kolichestvo_imen = cur.fetchone()
len_imena = kolichestvo_imen[0]
cur.execute('''select names from face''')
for i in range(len_imena):
    imya = cur.fetchone()
    imena.append(imya[0])

# Выгружаем все коды людей из базы

cur.execute('''select count(code) from face''')
kolichestvo_imen = cur.fetchone()
len_imena = kolichestvo_imen[0]
cur.execute('''select code from face''')
for i in range(len_imena):
    # вытаскиваем код лица, в виде строки и затем подгоняем его под сравнялку нейросети
    code_lica = cur.fetchone()
    code_lica = code_lica[0]
    code_lica = code_lica[1:-1]
    code_lica = code_lica.split(',')
    for i in code_lica:
        i = float(i)
        baza_lic_res.append(i)
    asd = np.array(baza_lic_res)
    baza_lic_res = []
    baza_lic.append(asd)

faaace = []
faace_res = []

# Сравниваем наше лицо с лицами из базы в цикле, зависящем от количества имен
while True:
    # Получаем изображение для распознания
    start_time = time.time()
    # known_image = face_recognition.load_image_file("new.png")
    # known_image = cv2.resize(known_image,(0 , 0), fx=0.45, fy = 0.45)
    # # fuck_location = face_recognition.face_locations(known_image)
    # fuck_encode = face_recognition.face_encodings(known_image)
    # # print (fuck_encode)
    # face_imena = []
    # # for i in range(len_imena):
    # #     result = face_recognition.compare_faces(fuck_encode, baza_lic[i])
    # #     if result == [True]:
    # #         print(imena[i])
    # #         print(result)
    # #         print('''--- %seconds ----''' % (time.time()-start_time))
    # for face_encoda in fuck_encode:
    cur.execute('''select encode from encodings''')
    encode_from_bd = cur.fetchone()
    print(encode_from_bd)
    encode_from_bd = encode_from_bd[0]
    encode_from_bd = encode_from_bd[1:-1]
    encode_from_bd = encode_from_bd.split(',')
    for i in encode_from_bd:
        i = float(i)
        faace_res.append(i)
    asd = np.array(faace_res)
    faaace.append(asd)
    faace_res = []
    for face_encoda in faaace:
        face_recognition_try = face_recognition.compare_faces(baza_lic, face_encoda)
        imya_output = 'Unknown'
        if True in face_recognition_try:
            index_lica = face_recognition_try.index(True)
            name = imena[index_lica]
            print(name)
            # print('''--- %seconds ----''' % (time.time() - start_time))
        else: print(imya_output)
    faaace = []

    time.sleep(0.5)




