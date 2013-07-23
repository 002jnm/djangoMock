from djangoMock import DjangoModelObjectsMock
from django.db import models
import unittest
from mock import Mock

class MyModel(models.Model):
    pass
class TestObjectsGet(unittest.TestCase):

    def test_should_get_a_mock_when_the_modelObject_mock_is_applied(self):
        objectsMock = DjangoModelObjectsMock()
        objectsMock.start()
        result = MyModel.objects.get()
        self.assertIsInstance(result, Mock)
        objectsMock.stop()
        
    def test_should_get_the_assigned_value(self):
        objectsMock = DjangoModelObjectsMock()
        objectsMock.start()
        objectsMock.when_called_with(name = 'value').return_value = 'assigned_value'
        result = MyModel.objects.get(name = 'value')
        self.assertEqual('assigned_value', result)
        objectsMock.stop()
