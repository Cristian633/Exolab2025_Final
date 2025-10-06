import os
from flask import Flask, send_from_directory, jsonify

# Puedes leer variables de entorno para futuras configuraciones:
PORT = int(os.getenv("PORT", "8000"))  # Azure inyecta $PORT en runtime

# Sirve archivos estáticos desde ./public en la raíz del sitio
app = Flask(__name__, static_folder="public", static_url_path="")

# Ruta raíz: index.html
@app.route("/")
def root():
    return send_from_directory(app.static_folder, "index.html")

# Archivos "estáticos" adicionales: /pagina2.html, /css/*, /js/*, imágenes, etc.
@app.route("/<path:path>")
def static_proxy(path: str):
    return send_from_directory(app.static_folder, path)

# ========= API de ejemplo =========
@app.get("/api/series")
def series():
    # Ejemplo simple; luego reemplaza por datos reales (BD/CSV/servicios)
    data = {
        "t": [1, 2, 3, 4, 5],
        "y": [10, 12, 9, 15, 14]
    }
    return jsonify(data)

# Ejemplo de “salud” del servicio
@app.get("/api/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    # Local: python app.py
    # En Azure: se usa gunicorn (ver Startup Command)
    app.run(host="0.0.0.0", port=PORT)
