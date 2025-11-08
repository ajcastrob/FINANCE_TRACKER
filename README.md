# 📊 Gestor de Finanzas Personales con Asistente de IA

Este proyecto es una aplicación para el seguimiento de finanzas personales que permite registrar ingresos y egresos, visualizar resúmenes financieros y obtener análisis a través de un asistente de chatbot impulsado por la API de Gemini de Google.

## ✨ Características Principales

- **Doble Interfaz:**
  - **Línea de Comandos (CLI):** Una interfaz simple para registrar transacciones y ver resúmenes directamente en la terminal.
  - **Aplicación Web Interactiva:** Una interfaz gráfica moderna construida con Streamlit para una experiencia de usuario más rica.
- **Gestión de Transacciones:** Registra fácilmente tus ingresos y egresos con fecha, cantidad, categoría y descripción.
- **Visualización de Datos:**
  - Filtra transacciones por rango de fechas.
  - Muestra resúmenes tabulares de tus finanzas.
  - Genera gráficos de torta para visualizar la distribución de tus ingresos y egresos.
- **Asistente de Chatbot con IA:**
  - Haz preguntas en lenguaje natural sobre tus datos financieros (ej: "¿cuánto gasté la semana pasada?").
  - El chatbot utiliza la API de Gemini de Google para entender tus preguntas y analizar los datos del CSV en tiempo real.

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3
- **Interfaz Web:** Streamlit
- **Análisis de Datos:** Pandas
- **Modelo de IA:** Google Gemini Pro
- **Visualización:** Matplotlib
- **Formato de Datos:** CSV

## 🚀 Guía de Instalación

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local.

### 1. Clonar el Repositorio

```bash
git clone <URL-DEL-REPOSITORIO>
cd <NOMBRE-DEL-DIRECTORIO>
```

### 2. Crear un Entorno Virtual (Recomendado)

```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar Dependencias

El proyecto incluye un archivo `requirements.txt` para facilitar la instalación de las librerías necesarias.

```bash
pip install -r requirements.txt
```
*Si no tienes el archivo `requirements.txt`, puedes crearlo con `pip freeze > requirements.txt` después de instalar las librerías manualmente (`pandas`, `streamlit`, `matplotlib`, `google-generativeai`, `tabulate`).*

### 4. Configurar la API Key de Gemini

Para que el chatbot funcione, necesitas una clave de API de Google Gemini.

a. **Obtén tu clave:** Ve a [Google AI Studio](https://aistudio.google.com/app/apikey) y genera una nueva clave.

b. **Guárdala de forma segura:**
   - Crea una carpeta llamada `.streamlit` en la raíz del proyecto.
   - Dentro de `.streamlit`, crea un archivo llamado `secrets.toml`.
   - Añade tu clave al archivo de la siguiente manera:
     ```toml
     # .streamlit/secrets.toml
     GEMINI_API_KEY = "AQUI_VA_TU_CLAVE_API"
     ```

## Usage

Puedes ejecutar el proyecto de dos maneras:

### 1. Ejecutar la Aplicación Web (Recomendado)

Para la experiencia completa con la interfaz gráfica y el chatbot:

```bash
streamlit run app.py
```

### 2. Ejecutar la Versión de Línea de Comandos (CLI)

Para una interacción rápida desde la terminal:

```bash
python3 main.py
```
