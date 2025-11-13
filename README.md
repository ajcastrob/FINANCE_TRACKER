# 💰 Finance Tracker

### Tu asistente personal de finanzas con Inteligencia Artificial

Gestiona tus ingresos y egresos de forma inteligente con visualizaciones interactivas y análisis conversacional powered by Google Gemini.

---

## 🎯 ¿Qué es Finance Tracker?

Finance Tracker es una aplicación moderna de gestión financiera personal que combina:

- 📊 **Visualizaciones Interactivas** - Gráficos dinámicos con Plotly y Matplotlib
- 🤖 **Chatbot con IA** - Análisis conversacional usando Google Gemini
- 📱 **Interfaz Moderna** - Diseño multi-página con Streamlit
- 💾 **Gestión Simple** - Almacenamiento en CSV, fácil de usar

---

## ✨ Características Destacadas

### 🏠 Dashboard Financiero

Visualiza tu situación financiera completa de un vistazo:

- Balance total en tiempo real
- Métricas del mes actual
- Últimas 5 transacciones
- Gráficos comparativos interactivos

### 💬 Chatbot Inteligente (AdamBot)

Interactúa con tus finanzas en lenguaje natural:

**Comandos Rápidos:**

- `/resumen` → Vista general de tus finanzas
- `/mes` → Análisis del mes actual
- `/semana` → Últimos 7 días
- `/analisis` → Insights con IA

**Preguntas Naturales:**

- "¿Cuál es mi balance actual?"
- "¿Cuánto gasté la semana pasada?"
- "¿En qué categoría gasto más?"

### 📈 Análisis Avanzados

- Gráficos de tendencia temporal
- Comparativas por categorías
- Filtros por rangos de fechas
- Detección de patrones de gasto

---

## 🚀 Inicio Rápido

```bash
# 1. Clona el repositorio
git clone https://github.com/tu-usuario/finance_tracker.git
cd finance_tracker

# 2. Instala dependencias
pip install -r requirements.txt

# 3. Configura tu API Key de Gemini
# Crea .streamlit/secrets.toml y agrega:
# GEMINI_API_KEY = "tu_api_key"

# 4. ¡Lanza la app!
streamlit run app.py
```

---

## 🛠️ Tecnologías

| Tech              | Uso                   |
| ----------------- | --------------------- |
| **Python 3.12**   | Lenguaje base         |
| **Streamlit**     | Framework web         |
| **Google Gemini** | IA conversacional     |
| **Pandas**        | Análisis de datos     |
| **Plotly**        | Gráficos interactivos |

---

## 📸 Vista Previa

### Dashboard Principal

> Visualiza tus métricas financieras con gráficos modernos e interactivos

### Chatbot con IA

> Pregunta en lenguaje natural y obtén análisis inteligentes

### Filtros Avanzados

> Analiza períodos específicos con gráficos de tendencia

---

## 🎯 ¿Para quién es?

✅ **Personas** que quieren controlar sus gastos personales  
✅ **Freelancers** que necesitan tracking simple de ingresos/egresos  
✅ **Estudiantes** aprendiendo gestión financiera  
✅ **Desarrolladores** buscando un proyecto base con IA

---

## 🌟 Por qué Finance Tracker

| Característica        | Finance Tracker            | Otras Apps            |
| --------------------- | -------------------------- | --------------------- |
| **Open Source**       | ✅ Gratis y personalizable | ❌ Cerrado            |
| **IA Conversacional** | ✅ Chatbot con Gemini      | ❌ Solo reportes      |
| **Privacidad**        | ✅ Datos en tu máquina     | ❌ En la nube         |
| **Personalizable**    | ✅ Código abierto          | ❌ Limitado           |
| **Moderno**           | ✅ Stack actual            | ⚠️ Tecnología antigua |

---

## 📦 Instalación Completa

### Requisitos Previos

- Python 3.12 o superior
- API Key de Google Gemini (gratis en [Google AI Studio](https://aistudio.google.com))
- Conexión a internet (solo para el chatbot)

### Pasos de Instalación

#### 1️⃣ Clonar el Repositorio

```bash
git clone https://github.com/tu-usuario/finance_tracker.git
cd finance_tracker
```

#### 2️⃣ Entorno Virtual

```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

#### 3️⃣ Instalar Dependencias

```bash
pip install -r requirements.txt
```

#### 4️⃣ Configurar API Key de Gemini

**Obtener la API Key:**

1. Ve a [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Inicia sesión con tu cuenta de Google
3. Crea una nueva API Key
4. Copia la clave generada

**Configurar en el proyecto:**

```bash
# Crear carpeta de configuración
mkdir .streamlit

# Crear archivo de secrets
touch .streamlit/secrets.toml

# Agregar tu API Key (abre el archivo y edita)
echo 'GEMINI_API_KEY = "tu_api_key_aquí"' > .streamlit/secrets.toml
```

⚠️ **Nota**: El archivo `secrets.toml` está en `.gitignore` por seguridad.

#### 5️⃣ Ejecutar la Aplicación

**Opción 1: Aplicación Web (Recomendada)**

```bash
streamlit run app.py
```

Se abrirá automáticamente en `http://localhost:8501`

**Opción 2: Versión CLI**

```bash
python main.py
```

---

## 💡 Guía de Uso

### 📝 Registrar una Transacción

1. Ve a **"Registrar transacción"** en el menú lateral
2. Completa el formulario:
   - Fecha de la transacción
   - Cantidad (sin símbolos, solo números)
   - Categoría (Ingresos o Egresos)
   - Descripción breve
3. Haz clic en **"Guardar transacción"**
4. ¡Listo! Tu transacción se guarda automáticamente

### 📊 Ver Dashboard

1. Abre **"Resumen financiero"**
2. Visualiza:
   - Balance total
   - Ingresos y egresos totales
   - Gráfico comparativo
   - Resumen del mes actual
   - Últimas 5 transacciones

### 🔍 Filtrar Transacciones

1. Ve a **"Filtrar transacción"**
2. Selecciona:
   - Fecha de inicio
   - Fecha final
3. Haz clic en **"Ver resumen"**
4. Obtén:
   - Tabla de transacciones del período
   - Métricas calculadas
   - Gráfico de tendencia temporal

### 💬 Usar el Chatbot

1. Abre **"Asistente Chatbot"**
2. Escribe un comando rápido:
   - `/resumen` - Vista general
   - `/mes` - Análisis mensual
   - `/semana` - Últimos 7 días
   - `/analisis` - Análisis con IA
   - `/ayuda` - Lista de comandos
3. O haz preguntas naturales:
   - "¿Cuánto gasté esta semana?"
   - "¿Cuál es mi balance?"
   - "Analiza mis finanzas"

---

## 🏗️ Arquitectura del Proyecto

```
finance_tracker/
│
├── 📂 assets/              # Recursos estáticos
│   └── logo.png
│
├── 📂 chatbot/             # Paquete del chatbot IA
│   ├── chatbot_gemini.py   # Conversación con Gemini
│   ├── comandos.py         # Comandos rápidos
│   ├── contexto.py         # Extracción de contexto
│   └── chatbot_analisis.py # Análisis proactivo
│
├── 📂 graficos/            # Módulo de visualizaciones
│   └── graficos.py         # Funciones de gráficos
│
├── 📂 pages/               # Páginas de la aplicación
│   ├── resumen.py          # Dashboard principal
│   ├── transaccion.py      # Formulario de registro
│   ├── filtro.py           # Filtros de transacciones
│   └── chat.py             # Interfaz del chatbot
│
├── 📄 app.py               # Entrada principal (web)
├── 📄 csv_file.py          # Gestión de persistencia
├── 📄 data_entry.py        # Validación de datos
├── 📄 main.py              # CLI - Línea de comandos
├── 📄 version_cli.py       # CLI alternativa
│
├── 📄 finanzas_personales.csv  # Base de datos (auto-generado)
├── 📄 requirements.txt     # Dependencias
├── 📄 README.md            # Este archivo
└── 📄 .gitignore           # Archivos ignorados por Git
```

### Principios de Arquitectura

Este proyecto sigue **Clean Architecture**:

- ✅ **Separación de responsabilidades** - Cada módulo tiene un propósito único
- ✅ **Modularidad** - Código organizado en paquetes reutilizables
- ✅ **Escalabilidad** - Fácil agregar nuevas funcionalidades
- ✅ **Testability** - Funciones puras y desacopladas

---

## 📊 Formato de Datos

### Estructura del CSV

El archivo `finanzas_personales.csv` se genera automáticamente:

| Campo         | Tipo   | Descripción             | Ejemplo         |
| ------------- | ------ | ----------------------- | --------------- |
| `fecha`       | Date   | Fecha de la transacción | 2025-01-15      |
| `cantidad`    | Float  | Monto de la transacción | 150.50          |
| `categoria`   | String | "Ingresos" o "Egresos"  | Ingresos        |
| `descripcion` | String | Descripción breve       | Salario mensual |

### Ejemplo de datos:

```csv
fecha,cantidad,categoria,descripcion
2025-01-15,3000.00,Ingresos,Salario
2025-01-16,50.00,Egresos,Supermercado
2025-01-17,120.00,Egresos,Gasolina
```

---

## 🗺️ Roadmap

### ✅ Versión 1.0 (Actual)

- [x] Dashboard con métricas en tiempo real
- [x] Chatbot conversacional con Gemini
- [x] Comandos rápidos (/resumen, /mes, /semana)
- [x] Gráficos interactivos con Plotly
- [x] Filtros por fecha
- [x] Arquitectura multi-página
- [x] Gráficos de tendencia temporal

### 🚧 Versión 2.0 (Próximamente)

- [ ] Editar y eliminar transacciones
- [ ] Categorías personalizables (subcategorías)
- [ ] Migración a SQLite
- [ ] Exportar reportes a PDF
- [ ] Gráficos de comparación mensual
- [ ] Búsqueda avanzada de transacciones

### 🔮 Versión 3.0 (Futuro)

- [ ] Autenticación multi-usuario
- [ ] Sincronización en la nube
- [ ] Metas de ahorro y presupuestos
- [ ] Notificaciones automáticas
- [ ] App móvil (PWA)
- [ ] Integración con APIs bancarias

---

## 🐛 Solución de Problemas

### Error: "Module 'streamlit' not found"

```bash
pip install -r requirements.txt
```

### Error: "Invalid API Key"

1. Verifica que tu API Key esté en `.streamlit/secrets.toml`
2. Asegúrate de que el formato sea: `GEMINI_API_KEY = "tu_key"`
3. Reinicia la aplicación

### El chatbot no responde

1. Verifica tu conexión a internet
2. Revisa que tengas créditos en tu cuenta de Google AI
3. Asegúrate de que el modelo esté disponible

### CSV corrupto o errores de datos

```bash
# Eliminar el CSV y empezar de nuevo
rm finanzas_personales.csv
# Se creará uno nuevo al iniciar la app
```

### Error: "st.set_page_config must be the first Streamlit command"

Este error es conocido y está documentado. La app funciona correctamente a pesar de la advertencia.

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Si quieres mejorar este proyecto:

### Cómo Contribuir

1. **Fork** el repositorio
2. **Crea** una rama para tu feature:
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit** tus cambios:
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push** a la rama:
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Abre** un Pull Request

### Áreas de Contribución

- 🐛 Reportar bugs
- ✨ Proponer nuevas features
- 📝 Mejorar documentación
- 🎨 Mejorar UI/UX
- 🧪 Agregar tests
- 🌍 Traducciones

---

## 📊 Stats del Proyecto

- 🏗️ **Arquitectura**: Multi-página modular con Streamlit
- 📦 **Módulos**: 15+ archivos organizados
- 🤖 **IA**: Google Gemini 2.0 Flash
- 📈 **Gráficos**: Plotly + Matplotlib
- 🔧 **Código**: Clean Architecture
- ⚡ **Performance**: Optimizado y rápido
- 🎯 **Líneas de código**: ~2,000+

---

## 🎓 Ideal para Aprender

Este proyecto es perfecto si estás aprendiendo:

- ✅ **Python avanzado** - POO, módulos, paquetes
- ✅ **Streamlit** - Framework web moderno
- ✅ **Integración con APIs de IA** - Google Gemini
- ✅ **Manipulación de datos** - Pandas
- ✅ **Visualizaciones interactivas** - Plotly, Matplotlib
- ✅ **Arquitectura de software** - Clean Architecture
- ✅ **Git y control de versiones** - Workflow profesional
- ✅ **Documentación** - README, comentarios, docstrings

---

## 🔧 Configuración Avanzada

### Personalizar el Tema de Streamlit

Edita `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#1C1C1E"
secondaryBackgroundColor = "#2C2C2E"
textColor = "#FFFFFF"
font = "sans serif"

[server]
headless = true
port = 8501
```

### Cambiar el Modelo de IA

En `chatbot/chatbot_gemini.py`:

```python
# Para más precisión (más lento y costoso)
model = genai.GenerativeModel("gemini-1.5-pro")

# Para velocidad (recomendado)
model = genai.GenerativeModel("gemini-1.5-flash")

# Experimental (más nuevo)
model = genai.GenerativeModel("gemini-2.0-flash-exp")
```

---

## 📞 Contacto y Soporte

**Jose Castro**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/josé-castro-b600791a4/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/tu-usuario)

### ¿Necesitas ayuda?

- 📧 Abre un [Issue](https://github.com/tu-usuario/finance_tracker/issues)
- 💬 Contacta por LinkedIn
- 📖 Lee la [documentación completa](./README.md)

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

```
MIT License

Copyright (c) 2025 Jose Castro

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 🙏 Agradecimientos

Un agradecimiento especial a:

- [Streamlit](https://streamlit.io/) - Por el increíble framework web interactivo
- [Google AI](https://ai.google.dev/) - Por la API de Gemini y el modelo de IA
- [Plotly](https://plotly.com/) - Por las visualizaciones interactivas hermosas
- [Pandas](https://pandas.pydata.org/) - Por la manipulación de datos eficiente
- La comunidad open source 💚 - Por inspiración y recursos

---

## ⭐ Soporte al Proyecto

Si este proyecto te fue útil, considera:

- ⭐ **Darle una estrella** en GitHub
- 🐛 **Reportar bugs** abriendo un issue
- 💡 **Sugerir features** en discussions
- 🤝 **Contribuir** con pull requests
- 📢 **Compartir** con otros desarrolladores
- ☕ **Invitarme un café** (opcional)

---

## 📈 Métricas del Repositorio

![GitHub stars](https://img.shields.io/github/stars/tu-usuario/finance_tracker?style=social)
![GitHub forks](https://img.shields.io/github/forks/tu-usuario/finance_tracker?style=social)
![GitHub issues](https://img.shields.io/github/issues/tu-usuario/finance_tracker)
![GitHub license](https://img.shields.io/github/license/tu-usuario/finance_tracker)

---

<div align="center">

## 🚀 ¡Comienza Ahora!

**[📥 Descargar](https://github.com/tu-usuario/finance_tracker/archive/refs/heads/main.zip) • [📖 Documentación](./README.md) • [🐛 Reportar Bug](https://github.com/tu-usuario/finance_tracker/issues) • [💡 Sugerir Feature](https://github.com/tu-usuario/finance_tracker/issues)**

---

### Hecho con ❤️ y ☕ por [Jose Castro](https://www.linkedin.com/in/josé-castro-b600791a4/)

**⭐ Si te gusta el proyecto, considera darle una estrella ⭐**

_Última actualización: NOVIEMBRE 2025_

</div>
