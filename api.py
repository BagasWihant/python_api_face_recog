from flask import Flask, jsonify
import deteksiWajah

app = Flask(__name__)
@app.route('/tes', methods=['GET'])
def get_tes():
    return deteksiWajah.tes()
    

if __name__ == '__main__':
    app.run(debug=True)