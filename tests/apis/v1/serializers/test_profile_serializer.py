import pytest

from internet_speed.apis.v1.serializers.profile import ProfileSerializer


@pytest.mark.django_db
def test_serialize_profile(user):
    serializer = ProfileSerializer(user)
    assert serializer.data == {
        "name": user.name,
        "email": user.email
    }
