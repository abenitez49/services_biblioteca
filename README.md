# 📚 Sistema de Gestión de Biblioteca - Django + DRF

Proyecto de backend en Python usando Django y Django REST Framework, que permite la administración de una biblioteca con funcionalidades para manejar libros, autores y clasificaciones. También permite almacenar PDFs y realizar análisis sobre valoraciones usando Pandas.

---

## 🚀 Instalación paso a paso

1. Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
Crear entorno virtual e instalar dependencias:

bash
Copiar
Editar
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
Si no tenés un requirements.txt, podés instalar manualmente con:

bash
Copiar
Editar
pip install django
pip install djangorestframework
pip install djangorestframework-simplejwt
pip install django_extensions
pip install psycopg
pip install psycopg2
pip install django-cors-headers
Migraciones e iniciar servidor:

bash
Copiar
Editar
python manage.py migrate
python manage.py runserver
🧠 ¿Qué hace este sistema?
Alta, baja, modificación y listado de libros.

Asociación de libros con autores y clasificaciones.

Carga y almacenamiento de PDFs de libros en carpeta storage/.

Endpoint de búsqueda de libros por ID con validación de existencia.

Clasificaciones con modelo de embebido (por implementar).

API limpia y funcional, con JWT para autenticación.

📁 Estructura del proyecto
bash
Copiar
Editar
biblioteca/
├── libros/
│   ├── models.py  # Modelos de Libro, Autor, Clasificación
│   ├── views.py   # API CRUD
│   └── serializers.py
├── storage/       # PDFs almacenados
└── manage.py
📸 Capturas del código y funcionamiento
📘 Crear un libro
python
Copiar
Editar
# views.py
class LibroCreateAPIView(APIView):
    def post(self, request):
        # lógica para crear libro...

📚 Listado de libros
python
Copiar
Editar
# views.py
class LibroListAPIView(APIView):
    def get(self, request):
        # lógica para listar libros...

📊 Valoraciones y análisis con Pandas
Usamos Pandas para analizar valoraciones de libros:

python
Copiar
Editar
import pandas as pd

df = pd.read_csv('valoraciones.csv')
valoradas = df.groupby("genero")["puntuacion"].mean()
print(valoradas)
📈 Gráficos generados
Género más valorado


Pregunta de análisis libre
¿Cuáles son los autores con más libros valorados positivamente?


💡 Sugerencias por género
Al seleccionar un género, el sistema puede recomendar libros del mismo género que hayan sido bien valorados.

🧪 Embedding de calificaciones (pendiente)
📝 Sección vacía – próximamente se integrará un sistema de embeddings para análisis semántico de valoraciones.

🐼 Integración avanzada con Pandas (pendiente)
📝 Sección vacía – se agregará procesamiento adicional de datasets con Pandas, exploración de patrones, etc.

🔒 Licencia
Este proyecto está bajo la licencia Alexis. Consultá el archivo LICENSE para más información.
