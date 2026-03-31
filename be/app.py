from flask import Flask, request, jsonify
from flask_cors import CORS  # 🔥 tambahkan ini
import pickle

app = Flask(__name__)
CORS(app)  # 🔥 tambahkan ini

model = pickle.load(open("model.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    umur = data["umur"]
    berat = data["berat"]
    tinggi = data["tinggi"]

    # Hitung IMT
    tinggi_m = tinggi / 100
    imt = berat / (tinggi_m ** 2)

    # Kategori
    if imt < 18:
        status = "Tidak Sehat"
    elif 18 <= imt <= 25:
        status = "Sehat (Normal)"
    else:
        status = "Berlebih"

    return jsonify({
        "status": status,
        "imt": round(imt, 2)
    })

if __name__ == "__main__":
    app.run(debug=True)