#!/usr/bin/env python
import codecs
import os
from setuptools import find_packages, setup

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def read_file(filename):
    with codecs.open(os.path.join(BASE_DIR, filename), encoding='utf-8') as f:
        content = f.read()
    return content


README = read_file('README.md')

PACKAGE = 'tinymce'
NAME = 'django-tinymce-lite'
DESCRIPTION = 'TinyMCE widget for Django'
AUTHOR = 'Ivan Chernov'
AUTHOR_EMAIL = 'chernoffivan@gmail.com'
URL = 'https://github.com/vanadium23/django-tinymce-lite'
VERSION = __import__(PACKAGE).__version__


setup(
    name=NAME,
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=README,
    license='MIT License',
    keywords='django widget tinymce',
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    url=URL,
    install_requires=[
        'django-appconf>=0.6.0',
    ],
)
