# Analizador de Correos con IA

Este proyecto permite leer correos de Microsoft Outlook usando Microsoft Graph y analizarlos con OpenAI para generar un resumen y asignar prioridad.

---

## 🔹 Requisitos previos

1. **Python 3.10+**

2. Instalar librerías necesarias:

pip install requests beautifulsoup4 openai python-dotenv

3. Crear cuentas necesarias

Microsoft Entra / Azure
Crear cuenta de prueba gratuita: https://www.microsoft.com/es-cl/security/business/identity-access/microsoft-entra-id

Crear una aplicación en: https://entra.microsoft.com/#view/Microsoft_AAD_IAM/EntraLanding.ReactView
Debes obtener: Tenant ID, Client ID y Client Secret

Dar permisos Mail.Read para poder leer correos

Microsoft 365 / Exchange
Obtener prueba gratuita: https://www.microsoft.com/es-cl/microsoft-365/business/microsoft-365-business-standard-one-month-trial

OpenAI https://platform.openai.com/api-keys

4. Configurar variables de entorno
Crear archivo .env en la raiz del proyecto con las credenciales

# Microsoft Graph
TENANT_ID=TU_TENANT_ID
CLIENT_ID=TU_CLIENT_ID
CLIENT_SECRET=TU_CLIENT_SECRET
MAILBOX=TU_MAILBOX

# OpenAI
OPENAI_API_KEY=TU_OPENAI_API_KEY

## 🔹 Estructura del proyecto
analizador-correos-ia/
│
├─ main.py # Script principal que ejecuta la lectura y análisis de correos
├─ README.md # Documentación del proyecto
├─ config_template.env # Plantilla de configuración sin exponer claves
├─ .gitignore # Ignora .env y archivos de caché de Python
└─ .env # Archivo con tus credenciales (no subir a GitHub)
