from flask import Flask, render_template, request, send_file
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Chargement de la clé privée
with open("keys/private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None)

# Chargement de la clé publique
with open("keys/public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        data = file.read()
        
        # Signature du document
        signature = private_key.sign(
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        
        sig_path = os.path.join(UPLOAD_FOLDER, "signature.bin")
        with open(sig_path, "wb") as f:
            f.write(signature)
            
        return send_file(sig_path, as_attachment=True)
    return render_template("index.html")

@app.route("/verify", methods=["GET", "POST"])
def verify():
    message = None
    if request.method == "POST":
        file = request.files["file"]
        signature_file = request.files["signature"]
        
        data = file.read()
        sig = signature_file.read()
        
        try:
            # Vérification de la signature [cite: 18, 19]
            public_key.verify(
                sig,
                data,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            message = "Signature VALIDE"
        except Exception:
            message = "Signature NON valide"
            
    return render_template("verify.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)