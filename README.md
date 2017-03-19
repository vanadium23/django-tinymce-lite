django-tinymce-lite
==============

**django-tinymce-lite** is a Django application that contains a widget to
render a form field as a TinyMCE editor.
This package provides same namespace as [django-tinymce](https://github.com/aljosa/django-tinymce/), but grabs latest stable tinymce static files from CDN.

[![PyPi Version](https://img.shields.io/pypi/v/django-tinymce-lite.svg)](https://pypi.python.org/pypi/django-tinymce-lite/)
[![Build Status](https://travis-ci.org/vanadium23/django-tinymce-lite.svg?branch=master)](https://travis-ci.org/vanadium23/django-tinymce-lite/)
[![Test Coverage](https://coveralls.io/repos/vanadium23/django-tinymce-lite/badge.svg?branch=master)](https://coveralls.io/r/vanadium23/django-tinymce-lite/)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/vanadium23/django-tinymce-lite/master/LICENSE.txt)

Quickstart
==========

Install django-tinymce-lite:

```shell
$ pip install django-tinymce-lite
```

Add tinymce to INSTALLED\_APPS in settings.py for your project:

```python
INSTALLED_APPS = (
    ...
    'tinymce',
)
```

In your code:

```python
from django import forms

from tinymce.widgets import TinyMCE

from .models import FooBar

class FooBarModelForm(forms.ModelForm):
    class Meta:
        model = FooBar
        fields = ['content1']
        widgets = {
            'content1': TinyMCE
        }

```

Configuration
========

**django-tinymce-lite** is configured through django settings mechanism.
Following options are availiable:

```python
# Url to tinymce init js
TINYMCE_JS = '//cdn.tinymce.com/4/tinymce.min.js'

# If you need pass extra static files for all tinymce widget
TINYMCE_EXTRA_MEDIA = {
    'js': [],
    'css': {}
}

# Config, that passed to tinyMCE.init functions
TINYMCE_CONFIG = {
    'selector': '.django-tinymce',
    'theme': 'modern',
    'relative_urls': False,
}
```

For tinymce configuration, read more on [site](https://www.tinymce.com/docs/configure/).


Releases
========

Latest release is 1.0.0. It's support python 2.7, 3.4, 3.5, 3.6 and Django
\>= 1.7.


Support and updates
===================

Use github issues <https://github.com/vanadium23/django-tinymce-lite/issues>

License
=======

Originally written by Aljosa Mohorovic.

Much inspired by django-select2.

This program is licensed under the MIT License (see LICENSE)
