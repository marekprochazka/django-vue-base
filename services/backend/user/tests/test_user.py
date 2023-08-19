import pytest

from user.models import User
from user.tests.factories import UserFactory


@pytest.mark.django_db()
class TestUser:
    def test_create_user_from_factory(self):
        user = UserFactory()
        assert user.pk is not None

    def test_create_user_normal(self):
        user = User.objects.create_user(
            username="test@email.cz",
            password="heslo",
        )
        assert user.pk == User.objects.get(username=user.username).pk
