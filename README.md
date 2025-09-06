# Analizador de Correos con IA

Este proyecto permite leer correos de Microsoft Outlook usando Microsoft Graph y analizarlos con OpenAI para generar un resumen y asignar prioridad.

---

## 🔹 Requisitos previos

1. **Python 3.10+**

2. Instalar librerías necesarias:

pip install requests beautifulsoup4 openai python-dotenv

3. Crear cuentas necesarias

### Microsoft Entra / Azure

- Crear cuenta de prueba gratuita:  
  [https://www.microsoft.com/es-cl/security/business/identity-access/microsoft-entra-id](https://www.microsoft.com/es-cl/security/business/identity-access/microsoft-entra-id)

- Crear una aplicación en:  
  [https://entra.microsoft.com/#view/Microsoft_AAD_IAM/EntraLanding.ReactView](https://entra.microsoft.com/#view/Microsoft_AAD_IAM/EntraLanding.ReactView)

- Dar permisos `Mail.Read` para poder leer correos

Pasos para configurar la aplicación en Microsoft Entra Admin Center:
1. Ir a App registrations y crear una nueva aplicación.
2. En Certificates & Secrets, crear un `Client Secret` y guardar el Value (solo se muestra una vez)
3. En API Permissions, hacer clic en Add a permission -> Microsoft Graph -> Application permissions -> seleccionar `Mail.Read`
4. Dar consent al permiso para tu organización si es necesario.

- Debes obtener:  
  `Tenant ID`, `Client ID` y `Client Secret` (el value que guardaste)

### Microsoft 365 / Exchange

- Obtener prueba gratuita:  
  [https://www.microsoft.com/es-cl/microsoft-365/business/microsoft-365-business-standard-one-month-trial](https://www.microsoft.com/es-cl/microsoft-365/business/microsoft-365-business-standard-one-month-trial)

### OpenAI

- Obtener API key en:  
  [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)

4. Configurar variables de entorno  
Crear archivo `.env` en la raíz del proyecto con las credenciales:

# Microsoft Graph

TENANT_ID=TU_TENANT_ID_AQUI

CLIENT_ID=TU_CLIENT_ID_AQUI

CLIENT_SECRET=TU_CLIENT_SECRET_AQUI

MAILBOX=TU_MAILBOX_AQUI

# OpenAI
OPENAI_API_KEY=TU_OPENAI_API_KEY_AQUI
