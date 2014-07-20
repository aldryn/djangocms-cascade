# -*- coding: utf-8 -*-
from aldryn_client import forms

class Form(forms.BaseForm):
    cms_cascade_plugins = forms.CharField('Cascade Plugins', required=False)

    def to_settings(self, data, settings):
        settings['CMS_CASCADE_PLUGINS'] = data.get('cms_cascade_plugins', '')
        return settings
