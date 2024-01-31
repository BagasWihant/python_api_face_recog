import face_recognition
from mysql import connector as mysql
import koneksi
from flask import jsonify

def deteksi(photo,imgDb):
    inputFileImage= "face/"+imgDb
    referImage = face_recognition.load_image_file(photo)
    inputImage = face_recognition.load_image_file(inputFileImage)

    try:
        referEncode = face_recognition.face_encodings(referImage)[0]
    except IndexError as e:
        pass


    try:
        inputEncode = face_recognition.face_encodings(inputImage)[0]
    except IndexError as e:
        return jsonify('Wajah tidak terdeteksi')

    results = face_recognition.compare_faces([referEncode], inputEncode)

    return results[0]


def proses(id,file):

    con = koneksi.konek()

    con.mycursor.execute("SELECT * FROM orang where id=" + id)
    
    myresult = con.mycursor.fetchall()
    response = False
    nama =''
    for data in myresult:
        nama = data[1]
        cekWajah = deteksi(file,data[2])
        if cekWajah:
            response = True
            break
        else:
            response = False
    return [response,nama]



if __name__ == "__main__":
    proses()
