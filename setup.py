import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-grappelli-filters',
    version='0.3.0',
    packages=['grappelli_filters'],
    include_package_data=True,
    install_requires=['django', 'django-grappelli'],
    license='Unlicense',
    description='Additional filters for Djagno Grappelli admin',
    long_description=README,
    url='https://gitlab.com/miguelcumpa/django-grappelli-filters',
    author='Fran Hrzenjak',
    author_email='fran@changeset.hr',
    maintainer='Miguel A. Cumpa A.',
    maintainer_email='miguel.cumpa@yandex.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: Freeware',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
