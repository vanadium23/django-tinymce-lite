# coding: utf-8

from __future__ import absolute_import, unicode_literals

import json

from django import VERSION, forms

from .conf import settings


class TinyMCE(forms.Textarea):

    def __init__(self, attrs=None, mce_attrs=None, **kwargs):
        super(TinyMCE, self).__init__(attrs)
        self.mce_attrs = mce_attrs or {}
        if VERSION < (1, 11):
            self.build_attrs = self._old_build_attrs
        else:
            self.build_attrs = self._new_build_attrs

    def _add_tinymce_attrs(self, attrs):
        """Add tinymce data attributes."""
        if 'class' in attrs:
            attrs['class'] += ' django-tinymce'
        else:
            attrs['class'] = 'django-tinymce'

        tinymce_confing = settings.TINYMCE_CONFIG
        tinymce_confing.update(self.mce_attrs)
        attrs['data-django-tinymce-config'] = json.dumps(tinymce_confing)

        return attrs

    def _new_build_attrs(self, base_attr, extra_attrs=None):
        attrs = super(
            TinyMCE,
            self
        ).build_attrs(base_attr, extra_attrs=extra_attrs)

        return self._add_tinymce_attrs(attrs)

    def _old_build_attrs(self, extra_attrs=None, **kwargs):
        attrs = super(
            TinyMCE,
            self
        ).build_attrs(extra_attrs=extra_attrs, **kwargs)

        return self._add_tinymce_attrs(attrs)

    def _get_media(self):
        """
        Construct Media as a dynamic property.
        .. Note:: For more information visit
            https://docs.djangoproject.com/en/1.8/topics/forms/media/#media-as-a-dynamic-property
        """
        js = [settings.TINYMCE_JS, 'django_tinymce/django_tinymce.js']
        js += settings.TINYMCE_EXTRA_MEDIA['js']
        css = settings.TINYMCE_EXTRA_MEDIA['css']
        return forms.Media(
            js=js,
            css=css,
        )

    media = property(_get_media)
