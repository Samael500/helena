from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator
# from captcha.fields import ReCaptchaField


class FeedBackForm(forms.Form):

    """ Send email with feedback """

    required_msg = 'Обязательное поле.'
    email_invalid = 'Введите корректный адрес электронной почты.'

    # captcha = ReCaptchaField()

    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Имя'}), required=True, max_length=200)
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'Email'}), required=True, max_length=200, error_messages=dict(invalid=email_invalid))
    theme = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Тема'}), required=True, max_length=200)
    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows': '6', 'placeholder': 'Сообщение'}), required=True, max_length=1000)
