from django.conf import settings
import os
if not 'DJANGO_SETTINGS_MODULE' in os.environ:
    settings.configure()

from mock import patch, call
from django.db.models import Manager

class DjangoModelObjectsMock:
    def start(self):
        self.djangoManger_get_patcher = patch.object(Manager, 'get')
        self.djangoManger_filter_patcher = patch.object(Manager, 'filter')
        self.djangoManger_get = self.djangoManger_get_patcher.start()
        self.djangoManger_filter = self.djangoManger_filter_patcher.start()
        self.djangoManger_get.side_effect = self.mock_django_get
        self.presetValueForCalls = []

    def stop(self):
        self.djangoManger_get_patcher.stop()
        self.djangoManger_filter_patcher.stop()
        
    def call(self, *args, **kwargs):
        kall = call(*args, **kwargs)
        self.presetValueForCalls.append(kall)
        return kall

    def mock_django_get(self, *args, **kwargs):
        currentCall = call(*args, **kwargs)
        for kalls in self.presetValueForCalls:
            if kalls == currentCall:
                return kalls.return_value
        return self.djangoManger_get.return_value    
    