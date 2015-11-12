from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator
# from captcha.fields import ReCaptchaField

from helpers.forms import UpdateCssMixin


class FeedBackForm(forms.Form, UpdateCssMixin):

    """ Send email with feedback """

    # captcha = ReCaptchaField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._set_errors_css()

    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Имя'}), required=True, max_length=200)
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'Email'}), required=True, max_length=200)
    theme = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Тема'}), required=True, max_length=200)
    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows': '6', 'placeholder': 'Сообщение'}), required=True, max_length=1000)
