from os.path import abspath, dirname, join, normpath

from setuptools import setup


setup(

    # Basic package information:
    name = 'django-ganalytics',
    version = '0.6.0',
    packages = ['ganalytics'],

    # Packaging options:
    zip_safe = False,
    include_package_data = True,

    # Package dependencies:
    install_requires = ['Django>=1.3.1'],

    # Metadata for PyPI:
    author = 'Randall Degges',
    author_email = 'rdegges@gmail.com',
    license = 'UNLICENSE',
    url = 'https://github.com/rdegges/django-ganalytics',
    keywords = 'django google analytics',
    description = 'Simple Google Analytics integration for Django.',
    long_description = open(normpath(join(dirname(abspath(__file__)),
        'README.md'))).read()

)
