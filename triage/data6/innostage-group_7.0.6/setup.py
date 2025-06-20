from setuptools import setup, find_packages
import requests
import json
import os
import socket



if __name__ == '__main__':
    setup(
        name='innostage-group',
        version=os.getenv('PACKAGE_VERSION', '7.0.6'),
        package_dir={'': 'src'},
        packages=find_packages('src', include=[
            'innostage-group*'
        ]),
        description='A demo package.',
        install_requires=['']
    )