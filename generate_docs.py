import os
import django
import pydoc
import importlib

def generate_doc(module_name, output_path):
    mod = importlib.import_module(module_name)
    pydoc.writedoc(mod)  # Esto genera un archivo .html en el directorio actual
    filename = module_name + ".html"
    if os.path.exists(filename):
        os.rename(filename, output_path)

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_site.settings')
    django.setup()

    if not os.path.exists("docs"):
        os.makedirs("docs")

    generate_doc('blog.models', 'docs/models.html')
    generate_doc('blog.views', 'docs/views.html')

    print("Documentación generada en la carpeta docs/")
