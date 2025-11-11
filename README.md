# 📊 Gestor de Finanzas Personales con Asistente de IA

Una aplicación moderna de seguimiento financiero personal con inteligencia artificial, construida con Streamlit y Google Gemini. Registra transacciones, visualiza tendencias y obtén análisis inteligentes de tus finanzas mediante un chatbot conversacional.

---

## ✨ Características Principales

### 🖥️ **Interfaz Multi-Página Moderna**

- **Dashboard Financiero**: Visualiza tu situación financiera completa de un vistazo
- **Registro de Transacciones**: Formulario intuitivo para agregar ingresos y egresos
- **Filtros Avanzados**: Analiza transacciones por rangos de fechas
- **Chatbot con IA**: Asistente conversacional para análisis financiero en lenguaje natural

### 💰 **Gestión de Finanzas**

- Registro fácil de ingresos y egresos
- Categorización de transacciones
- Cálculo automático de balance y ahorros
- Métricas en tiempo real

### 📊 **Visualizaciones Interactivas**

- Gráficos de barras comparativos con Plotly
- Gráficos de torta para distribución mensual
- Gráficos de tendencia temporal con Matplotlib
- Dashboard responsive y profesional

### 🤖 **Asistente de IA (AdamBot)**

- **Comandos rápidos**:
  - `/resumen` - Resumen general de finanzas
  - `/mes` - Análisis del mes actual
  - `/semana` - Últimos 7 días
  - `/analisis` - Análisis proactivo con IA
  - `/ayuda` - Mostrar comandos disponibles
- **Conversación natural**: Haz preguntas como "¿Cuánto gasté la semana pasada?"
- **Memoria conversacional**: Recuerda el contexto de la conversación
- **Análisis inteligente**: Detecta patrones y proporciona recomendaciones

### 🖥️ **Doble Interfaz**

- **Web App**: Interfaz moderna con Streamlit (recomendada)
- **CLI**: Versión de línea de comandos para uso rápido en terminal

---

## 🏗️ Arquitectura del Proyecto

```
finance_tracker/
│
├── 📂 assets/              # Recursos estáticos (logo, imágenes)
├── 📂 chatbot/             # Paquete del chatbot con IA
│   ├── chatbot_gemini.py   # Conversación con Google Gemini
│   ├── comandos.py         # Procesamiento de comandos rápidos
│   ├── contexto.py         # Extracción de contexto financiero
│   └── chatbot_analisis.py # Análisis proactivo con IA
│
├── 📂 graficos/            # Módulo de visualizaciones
│   └── graficos.py         # Funciones para gráficos
│
├── 📂 pages/               # Páginas de la aplicación web
│   ├── resumen.py          # Dashboard principal
│   ├── transaccion.py      # Formulario de registro
│   ├── filtro.py           # Filtros de transacciones
│   └── chat.py             # Interfaz del chatbot
│
├── 📄 app.py               # Entrada principal de la web app
├── 📄 csv_file.py          # Gestión de persistencia de datos
├── 📄 data_entry.py        # Validación de entrada de datos
├── 📄 main.py              # CLI - Versión de línea de comandos
├── 📄 version_cli.py       # CLI alternativa
│
├── 📄 finanzas_personales.csv  # Base de datos (generado automáticamente)
├── 📄 requirements.txt     # Dependencias del proyecto
└── 📄 README.md            # Este archivo
```

---

## 🛠️ Tecnologías Utilizadas

| Tecnología                               | Propósito                          |
| ---------------------------------------- | ---------------------------------- |
| **Python 3.12+**                         | Lenguaje principal                 |
| **Streamlit**                            | Framework web interactivo          |
| **Google Gemini (gemini-2.0-flash-exp)** | Modelo de IA para el chatbot       |
| **Pandas**                               | Manipulación y análisis de datos   |
| **Plotly**                               | Gráficos interactivos modernos     |
| **Matplotlib**                           | Gráficos de tendencias             |
| **CSV**                                  | Formato de almacenamiento de datos |

---

## 🚀 Guía de Instalación

### 1️⃣ Clonar el Repositorio

```bash
git clone https://github.com/tu-usuario/finance_tracker.git
cd finance_tracker
```

### 2️⃣ Crear Entorno Virtual (Recomendado)

**En macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**En Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Instalar Dependencias

```bash
pip install -r requirements.txt
```

**Dependencias incluidas:**

- `streamlit` - Framework web
- `pandas` - Análisis de datos
- `google-generativeai` - API de Google Gemini
- `matplotlib` - Gráficos
- `plotly` - Visualizaciones interactivas

### 4️⃣ Configurar API Key de Google Gemini

#### a) Obtener la API Key

1. Ve a [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Inicia sesión con tu cuenta de Google
3. Crea una nueva API Key
4. Copia la clave generada

#### b) Configurar en el proyecto

1. Crea la carpeta de configuración:

   ```bash
   mkdir .streamlit
   ```

2. Crea el archivo de secrets:

   ```bash
   touch .streamlit/secrets.toml
   ```

3. Agrega tu API Key:
   ```toml
   # .streamlit/secrets.toml
   GEMINI_API_KEY = "TU_API_KEY_AQUÍ"
   ```

⚠️ **Importante**: Este archivo está en `.gitignore` y NO se subirá a Git por seguridad.

---

## 💻 Uso

### 🌐 Opción 1: Aplicación Web (Recomendada)

La interfaz web ofrece la experiencia completa con todas las funcionalidades:

```bash
streamlit run app.py
```

Esto abrirá automáticamente tu navegador en `http://localhost:8501`

**Funcionalidades disponibles:**

- ✅ Dashboard con métricas en tiempo real
- ✅ Registro de transacciones con formulario
- ✅ Filtros por fecha
- ✅ Gráficos interactivos con Plotly
- ✅ Chatbot conversacional con IA
- ✅ Comandos rápidos

### 🖥️ Opción 2: Línea de Comandos (CLI)

Para usuarios avanzados o uso rápido desde terminal:

```bash
python main.py
```

o

```bash
python version_cli.py
```

**Funcionalidades CLI:**

- Registrar transacciones
- Ver resumen financiero
- Filtrar por fechas
- Visualizar gráficos en ventana emergente

---

## 📖 Guía de Uso del Chatbot

### Comandos Rápidos

| Comando     | Descripción                           | Ejemplo de respuesta                                        |
| ----------- | ------------------------------------- | ----------------------------------------------------------- |
| `/resumen`  | Resumen general de todas tus finanzas | Muestra ingresos, egresos, balance y total de transacciones |
| `/mes`      | Análisis del mes actual               | Métricas del mes en curso                                   |
| `/semana`   | Resumen de los últimos 7 días         | Actividad financiera reciente                               |
| `/analisis` | Análisis detallado con IA             | Insights, tendencias y recomendaciones                      |
| `/ayuda`    | Lista de comandos disponibles         | Guía completa de comandos                                   |

### Preguntas en Lenguaje Natural

El chatbot entiende preguntas como:

- "¿Cuál es mi balance actual?"
- "¿Cuánto gasté la semana pasada?"
- "¿En qué categoría gasto más?"
- "Analiza mis finanzas del último mes"
- "¿Tengo gastos altos recientes?"
- "¿Cuánto he ahorrado este año?"

### Características del Chatbot

- 🧠 **Memoria conversacional**: Recuerda las últimas 4 interacciones
- 📊 **Análisis contextual**: Accede a tus datos financieros en tiempo real
- 💡 **Recomendaciones**: Detecta patrones y sugiere mejoras
- 🔒 **Privado**: Tus datos nunca salen de tu máquina (excepto el análisis con IA)

---

## 📂 Estructura de Datos

### Formato del CSV

El archivo `finanzas_personales.csv` se genera automáticamente con esta estructura:

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

## 🎨 Capturas de Pantalla

### Dashboard Principal

Visualiza tu situación financiera completa con métricas interactivas y gráficos modernos.

### Chatbot con IA

Interactúa con AdamBot para obtener análisis inteligentes de tus finanzas.

### Filtros de Transacciones

Analiza períodos específicos con gráficos de tendencia temporal.

---

## 🔧 Configuración Avanzada

### Personalizar el tema de Streamlit

Edita `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#1C1C1E"
secondaryBackgroundColor = "#2C2C2E"
textColor = "#FFFFFF"
font = "sans serif"
```

### Cambiar el modelo de IA

En `chatbot/chatbot_gemini.py`, cambia el modelo:

```python
model = genai.GenerativeModel("gemini-1.5-pro")  # Más potente pero más lento
# o
model = genai.GenerativeModel("gemini-1.5-flash")  # Más rápido
```

---

## 🐛 Solución de Problemas

### Error: "Module 'streamlit' not found"

```bash
pip install -r requirements.txt
```

### Error: "Invalid API Key"

Verifica que tu API Key esté correctamente configurada en `.streamlit/secrets.toml`

### El chatbot no responde

1. Verifica tu conexión a internet
2. Asegúrate de tener créditos en tu cuenta de Google AI
3. Revisa que el modelo esté disponible

### CSV corrupto

Si el archivo CSV se corrompe, simplemente elimínalo:

```bash
rm finanzas_personales.csv
```

Se creará uno nuevo automáticamente al iniciar la app.

---

## 🚀 Próximas Funcionalidades

- [ ] Migración a base de datos SQLite
- [ ] Editar y eliminar transacciones
- [ ] Categorías personalizables
- [ ] Exportar reportes a PDF
- [ ] Gráficos de comparación mensual
- [ ] Metas de ahorro
- [ ] Notificaciones automáticas
- [ ] Modo oscuro/claro
- [ ] Autenticación multi-usuario
- [ ] Sincronización en la nube

---

## 📝 Notas de Desarrollo

### Principios de Arquitectura

Este proyecto sigue principios de **Clean Architecture**:

- **Separación de responsabilidades**: Cada módulo tiene un propósito único
- **Modularidad**: Código organizado en paquetes reutilizables
- **Escalabilidad**: Fácil agregar nuevas funcionalidades
- **Testability**: Funciones puras y desacopladas

### Mejores Prácticas Implementadas

- ✅ Arquitectura multi-página con `st.navigation`
- ✅ Separación de UI, lógica y datos
- ✅ Paquetes Python bien estructurados
- ✅ Imports claros y explícitos
- ✅ Código DRY (Don't Repeat Yourself)
- ✅ Manejo de errores robusto

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si quieres mejorar este proyecto:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

## 👤 Autor

**Jose Castro**

- LinkedIn: [José Castro](https://www.linkedin.com/in/josé-castro-b600791a4/)
- GitHub: [@ajcastrob](https://github.com/ajcastrob)

---

## 🙏 Agradecimientos

- [Streamlit](https://streamlit.io/) - Por el increíble framework web
- [Google AI](https://ai.google.dev/) - Por la API de Gemini
- [Plotly](https://plotly.com/) - Por las visualizaciones interactivas

---

## 📞 Soporte

¿Tienes preguntas o problemas?

- 📧 Abre un [Issue](https://github.com/tu-usuario/finance_tracker/issues)
- 💬 Contacta en LinkedIn

---

**⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub!**

---

_Última actualización: Enero 2025_
