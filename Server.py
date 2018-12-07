import sqlite3
import numpy as np
import face_recognition
import time
# Подключаемся к базе и создаем курсор
conn = sqlite3.connect('new2.db')
cur = conn.cursor()

# Создаем хранилище всех имеющихся лиц и их
baza_lic = []
imena = []
baza_lic_res = []
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




# Сравниваем наше лицо с лицами из базы в цикле, зависящем от количества имен
while True:
    # Получаем изображение для распознания

    known_image = face_recognition.load_image_file("new.png")
    fuck_encode = face_recognition.face_encodings(known_image)

    for i in range(len_imena):
        result = face_recognition.compare_faces(fuck_encode, baza_lic[i])
        if result == [True]:
            print(imena[i])
        time.sleep(3)