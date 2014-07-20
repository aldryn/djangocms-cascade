# -*- coding: utf-8 -*-
from aldryn_client import forms

class Form(forms.BaseForm):
    def to_settings(self, data, settings):
        settings['CMS_CASCADE_PLUGINS'] = data.get('cms_cascade_plugins', '')
        return settings
