from djangoMock import DjangoModelObjectsMock
from django.db import models
import unittest
from mock import Mock

class MyModel(models.Model):
    pass
class TestObjectsGet(unittest.TestCase):

    def test_Should_get_a_mock_when_the_modelObject_mock_is_applied(self):
        objectsMock = DjangoModelObjectsMock()
        objectsMock.start()
        result = MyModel.objects.get()
        self.assertIsInstance(result, Mock)
        objectsMock.stop()
