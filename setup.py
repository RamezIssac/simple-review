import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-simple-review',
    version='0.1',
    packages=find_packages("src"),
    package_dir = {
        "": "src",
    },
    include_package_data=True,
    license='MIT License',  # example license
    description='A Django extension for review feedback that use jQuery.raty. Batteries included..',
    long_description=README,
    url='http://radev.io/',
    author='Ramez Ashraf',
    author_email='ramezashraf@gmailcom',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django<1.9',
        'simplejson',
    ],
)
