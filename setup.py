import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

setup(
    name='django-mercadolibre',
    version='0.1',
    packages=['django_mercadolibre'],
    description='api y registro web mercadolibre',
    long_description=README,
    author='Julian David Toro',
    author_email='julian@rapigo.co',
    url='https://github.com/fulit103/django-mercadolibre',
    license='MIT',
    install_requires=[
        'Django>=1.8',
    ]
)