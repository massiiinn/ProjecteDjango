# Blog Django · My Site

Aquest és un projecte de blog desenvolupat amb Django com a part de l'assignatura **M3 - UF6**.

## Funcionalitats

- Llistat de posts amb títol, imatge i fragment de text.
- Detall de cada post amb contingut complet.
- Autors amb les seves dades i llistat dels seus posts.
- Etiquetes (tags) associades a cada post.
- Filtres de posts per tag.
- Dades carregades des de fixtures (`initial_data.json`).
- Ús de Bootstrap 5 per al disseny visual.

## Estructura del projecte

my_site/
├── blog/
│ ├── migrations/
│ ├── static/blog/img/
│ ├── templates/blog/
│ ├── admin.py
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── fixtures/initial_data.json
├── my_site/
│ ├── settings.py
│ └── urls.py
├── db.sqlite3
└── manage.py

## Instal·lació ràpida

git clone https://github.com/massiiinn/ProjecteDjango.git
cd ProjecteDjango

python -m venv venv
source venv/bin/activate

Per Windows: venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py loaddata initial_data.json


## Execució del projecte
python manage.py runserver
http://127.0.0.1:8000

## Documentació amb Pydoc

Documentació models.py: https://massiiinn.github.io/ProjecteDjango/docs/models.html
Documentació views.py: https://massiiinn.github.io/ProjecteDjango/docs/views.html
