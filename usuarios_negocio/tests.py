import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Usuario

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
@pytest.mark.django_db
def usuario(db):
    return Usuario.objects.create(username='testuser', password='password')


@pytest.mark.django_db
def test_list_usuarios(api_client, usuario):
    url = reverse('list-usuarios')
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 1


@pytest.mark.django_db
def test_delete_usuario(api_client, usuario):
    url = reverse('delete-usuario', args=[usuario.id])
    response = api_client.delete(url)
    assert response.status_code == 204
    assert not Usuario.objects.filter(id=usuario.id).exists()