
class UpdateCssMixin(object):

    """
    Mixin for update css string in field widget attrs
    """

    def _set_additional_css(self, css_data):
        """
        :param css_data: dictionary, key - field name, value - additional css string
        """
        for name, css_string in css_data.items():
            self._update_cssclass(name, css_string)

    def _update_cssclass(self, field_name, css_string):
        if field_name not in self.fields:
            return
        self.fields[field_name].widget.attrs['class'] = \
            (self.fields[field_name].widget.attrs.get('class', '') + ' ' + css_string).strip()

    def _set_cssclass(self, field_name, css_string):
        if field_name not in self.fields:
            return
        self.fields[field_name].widget.attrs['class'] = css_string

    def _set_errors_css(self):
        for field in self:
            if field.errors:
                self._update_cssclass(field.name, 'error')

    def _remove_cssclass(self, field_name, css_string):
        if field_name not in self.fields:
            return
        self.fields[field_name].widget.attrs['class'] = \
            (self.fields[field_name].widget.attrs.get('class', '').replace(css_string, '')).strip()
