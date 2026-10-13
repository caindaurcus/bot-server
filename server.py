from flask import Flask, request, abort
import requests
import os

app = Flask(__name__)

# ESTAS 2 COSAS LAS PONES EN RENDER COMO VARIABLES SECRETAS, NO AQUÍ
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN") 
GITHUB_USER = os.environ.get("GITHUB_USER")
REPO_NAME = "Bots"
FILE_NAME = "bot.py"
MI_CLAVE_SECRETA = "clave12345" # Cambia esto, esta clave la pondrás en tu APK

@app.route("/")
def home():
    return "Servidor activo"

@app.route("/get-bot")
def get_bot():
    clave = request.args.get("key")
    if clave != MI_CLAVE_SECRETA:
        return "Acceso denegado", 403
    
    url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/main/{FILE_NAME}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    r = requests.get(url, headers=headers)
    
    if r.status_code == 200:
        return r.text, 200, {'Content-Type': 'text/plain'}
    else:
        return f"Error: {r.status_code}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)