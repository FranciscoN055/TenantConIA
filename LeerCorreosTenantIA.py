import requests
from bs4 import BeautifulSoup
import sys
import os
from openai import OpenAI
from dotenv import load_dotenv

# 🔹 Forzar UTF-8 en consola
sys.stdout.reconfigure(encoding='utf-8')

# 🔹 Cargar variables desde .env
load_dotenv()

TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
MAILBOX = os.getenv("MAILBOX")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 🔹 Configuración OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

def obtener_token():
    url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope": "https://graph.microsoft.com/.default"
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    r = requests.post(url, data=data, headers=headers)
    if r.status_code == 200:
        return r.json()["access_token"]
    else:
        print("ERROR Error token:", r.text)
        return None

def limpiar_html(html):
    """Convierte HTML en texto plano con BeautifulSoup"""
    if not html:
        return ""
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text(separator="\n").strip()

def analizar_con_ia(texto):
    """Usa OpenAI para resumir y clasificar prioridad"""
    prompt = f"""
    Eres un asistente que analiza correos electrónicos.
    Texto del correo:
    {texto}

    Devuelve un JSON con:
    - resumen (máx 2 líneas)
    - prioridad (Urgente, Alta, Media o Baja)
    """
    respuesta = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )
    return respuesta.output[0].content[0].text

def leer_correos():
    token = obtener_token()
    if not token:
        return
    
    url = f"https://graph.microsoft.com/v1.0/users/{MAILBOX}/messages?$top=5"
    headers = {"Authorization": f"Bearer {token}"}
    
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        mails = r.json().get("value", [])
        for m in mails:
            remitente = m["from"]["emailAddress"]["address"]
            asunto = m["subject"]
            cuerpo_html = m.get("body", {}).get("content", "")
            cuerpo_texto = limpiar_html(cuerpo_html)

            print("De:", remitente)
            print("Asunto:", asunto)
            print("Cuerpo (recortado a 200 chars):")
            print(cuerpo_texto[:200], "..." if len(cuerpo_texto) > 200 else "")

            # 🔹 Pasar a IA
            analisis = analizar_con_ia(cuerpo_texto)
            print("Análisis IA:", analisis)
            print("-" * 80)
    else:
        print("ERROR Error leyendo correos:", r.status_code, r.text)

if __name__ == "__main__":
    leer_correos()
