import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from books.models import Author, Publisher

@pytest.fixture(scope="function")
def api_client():
    yield APIClient()

@pytest.fixture(scope="function")
def user():
    yield User.objects.create_user(username='testuser', password='testpassword')

@pytest.fixture(scope="function")
def user2():
    yield User.objects.create_user(username='testuser2', password='testpassword2')

@pytest.fixture(scope="function")
def author():
    yield Author.objects.create(name='test author', biography='test biography')

@pytest.fixture(scope="function")
def publisher():
    yield Publisher.objects.create(name='test publisher', address='test address')