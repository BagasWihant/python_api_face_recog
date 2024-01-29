import face_recognition
from mysql import connector as mysql
import cv2
import koneksi

def deteksi(id, photo):
    id = 1
    # inputFileImage= "face/ref_1.jpg"

    referImage = face_recognition.load_image_file(photo)
    inputImage = face_recognition.load_image_file(photo)

    referEncode = face_recognition.face_encodings(referImage)[0]
    inputEncode = face_recognition.face_encodings(inputImage)[0]

    results = face_recognition.compare_faces([referEncode], inputEncode)

    results[0]

def tes():
    text =[]
    con = koneksi.konek()

    con.mycursor.execute("SELECT * FROM orang")

    myresult = con.mycursor.fetchall()
    for x in myresult:

        text.append(x)

    print(text)
    return text

if __name__ == "__main__":
    tes()
