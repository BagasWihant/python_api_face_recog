from flask import Flask, jsonify, abort, request, url_for
import deteksiWajah
import os
import datetime 
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'face'
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024

diijinkan = set(["png", "jpg", "jpeg"])


def allowed(file):
    return "." in file and file.rsplit(".", 1)[1].lower() in diijinkan


@app.route("/tes/<id>", methods=["GET"])
def get_tes(id):
    return deteksiWajah.tes(id)


@app.route("/cekPhoto", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify("salah")

    file = request.files["file"]
    if file.filename == "":
        return jsonify("tidak ada poto")

    if file and allowed(file.filename):
        id = request.form.get("id")
        photo = file 

        saiki = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        ext = file.filename.split(".")[1]
        namaFile = "Usr" + id + "_" + saiki + "." + ext
        file.save(os.path.join(UPLOAD_FOLDER,namaFile))
        res = deteksiWajah.proses(id, photo)
        
        if res[0]:            
            return jsonify(True)
        else:
            os.remove('face/'+namaFile)
            return jsonify(False),400

    return jsonify("Maaf belum beruntung")


if __name__ == "__main__":
    app.run(debug=False)
