import factory

from user.models import User


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: "user_%s@email.com" % n)

    class Meta:
        model = User
       