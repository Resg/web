import factory
import factory.django
from .models import Usr


class UserFactory(factory.django.djangoModelFactory):
    class Meta:
        model = Usr

    username = factory.Faker('name')
