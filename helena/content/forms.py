from django import forms

from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

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


    def send_msg(self):
        """ Send email with current form data """
        # render email message
        html_content = render_to_string('email/feedback.html', dict(instance=self, support_email=settings.DEFAULT_FROM_EMAIL, site_url=site_url))
        msg = EmailMultiAlternatives(
            subject='Новое сообщение из формы обратной связи',
            body=strip_tags(html_content), from_email=settings.DEFAULT_FROM_EMAIL, to=to_email, )
        msg.attach_alternative(html_content, 'text/html')
        msg.send(fail_silently=True)
