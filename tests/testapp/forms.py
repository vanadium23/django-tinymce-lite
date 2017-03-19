
from django import forms

from tests.testapp.models import TestPage
from tinymce.widgets import TinyMCE


class TestPageModelForm(forms.ModelForm):
    class Meta:
        model = TestPage
        fields = ['content1']
        widgets = {
            'content1': TinyMCE
        }
