# 📦 Proyecto Ferramas - API con integración Transbank

## 🧾 Descripción

Este proyecto es una API REST desarrollada en **Python** que gestiona funcionalidades del sistema Ferramas e incluye integración con **Transbank Webpay Plus** para pagos electrónicos.

---

## ⚙️ Tecnologías utilizadas

- Python 3.11+
- FastAPI
- SQLite (o base de datos compatible)
- Transbank SDK (`transbank-sdk`)
- Uvicorn (servidor ASGI)

---

## 📁 Estructura del proyecto
api_ferramas/
├── api/
│ ├── db/
│ ├── models/
│ ├── routes/
│ ├── services/
│ └── utils/
├── app.py
├── requirements.txt
└── README.md



---

## 🚀 ¿Cómo ejecutar este proyecto?


1. Clona el repositorio

git clone https://github.com/Mvrtin23/ferramas_api.git
cd ferramas_api

2. Crea y activa un entorno virtual

python -m venv venv
source venv/bin/activate  * En Mac/Linux

venv\Scripts\activate     * En Windows

3. Instala las dependencias
pip install -r requirements.txt

4. Ejecuta el servidor
uvicorn app:app --reload
![image](https://github.com/user-attachments/assets/91701695-dd64-4aa7-bbba-5c4bf199c88d)

💳 Funcionalidad Transbank
1. Crear Transaccion
   POST /crear_pago
{
  "amount": 10000,
  "session_id": "sesion123",
  "buy_order": "orden123",
  "return_url": "http://localhost:8000/retorno_pago"
}

2. Confirmar Transacción
   POST /retorno_pago
token_ws=<token>


📌 Requisitos para otro entorno
Python 3.11 o superior

Conexión a internet

Cuenta Transbank (para producción)

Base de datos (MySql o alternativa)

👨‍💻 Autores

-Martín Muñoz
-Jorge Galaz

GitHub: Mvrtin23

