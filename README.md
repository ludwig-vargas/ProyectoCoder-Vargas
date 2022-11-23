# ProyectoCoder-Vargas
Proyecto Final my_blog Ludwig Vargas Garcia

Pasos para probar el blog
1. Creamos el entorno virtual y lo activamos
python -m venv venv
.\venv\Scripts\activate

2. Instalamos los requerimientospara el correcto funcionamiento del blog
pip install -r.\requeriments.txt

cd my_blog
3. Creamos las migraciones
python manage.py migrate

4. Creamos un super usuario
python manage.py createsuperuser

5. Para que las imagenes se guarden en el proyecto en la carpeta de media se crearan dos subcarpetas
media->product
media->service
media->avatar
