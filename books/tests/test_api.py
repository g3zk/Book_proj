import pytest
from books.models import Book
from django.urls import reverse
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_get_book_list(api_client, user, author, publisher):
    Book.objects.create(title='Test book', price=10.00, author=author, publisher=publisher, owner=user)
    response = api_client.get('/api/books/', format='json')
    assert response.status_code == 200
    assert len(response.data) == 1


@pytest.mark.django_db
def test_get_book_by_id(api_client, user, author, publisher):
    book = Book.objects.create(title='Test book', price=10.00, author=author, publisher=publisher, owner=user)
    response = api_client.get(f'/api/books/{book.id}/', format='json')
    assert response.status_code == 200
    assert response.data['title'] == 'Test book'
    assert response.data['price'] == '10.00'


@pytest.mark.django_db
def test_get_book_list_empty(api_client):
    response = api_client.get('/api/books/', format='json')
    assert response.status_code == 200
    assert response.data == []


@pytest.mark.django_db
def test_create_book_no_auth(api_client, author, publisher):
    response = api_client.post(
        '/api/books/',
        {
            'title': 'Test title',
            'price': 15.00,
            'author': author.id,
            'publisher': publisher.id,
        },
        format='json'
    )
    assert response.status_code == 401


@pytest.mark.django_db
def test_create_book_with_token(api_client, user, author, publisher):
    login_url = reverse('token_obtain_pair')
    tokens = api_client.post(
        login_url,
        {
            'username': 'testuser', 'password': 'testpassword',
        },
        format='json'
    ).data

    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {tokens["access"]}')
    response = api_client.post(
        '/api/books/',
        {
            'title': 'Test title',
            'description': 'Test description',
            'price': 15.00,
            'author': author.id,
            'publisher': publisher.id
        },
        format='json'
    )
    assert response.status_code == 201
    assert response.data['owner'] == 'testuser'
    assert response.data['title'] == 'Test title'


@pytest.mark.django_db
def test_create_book_with_invalid_token(api_client, user, author, publisher):
    login_url = reverse('token_obtain_pair')
    tokens = api_client.post(
        login_url,
        {
            'username': 'testuser', 'password': 'testpassword',
        },
        format='json'
    )

    api_client.credentials(HTTP_AUTHORIZATION='Bearer invalidtoken')
    response = api_client.post(
        '/api/books/',
        {
            'title': 'Test title',
            'description': 'Test description',
            'price': 15.00,
            'author': author.id,
            'publisher': publisher.id
        },
        format='json'
    )
    assert response.status_code == 401


@pytest.mark.django_db
def test_create_book_with_incorrect_fields(api_client, user, author, publisher):
    login_url = reverse('token_obtain_pair')
    tokens = api_client.post(
        login_url,
        {
            'username': 'testuser', 'password': 'testpassword',
        },
        format='json'
    ).data

    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {tokens["access"]}')

    response = api_client.post(
        '/api/books/',
        {
            'title': 'Test title',
            'price': 'number',
            'author': author.id,
            'publisher': publisher.id
        },
        format='json'
    )
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_book_no_auth(api_client, user, author, publisher):
    book = Book.objects.create(title='Old title', price=10.00, author=author, publisher=publisher, owner=user)
    response = api_client.put(
        '/api/books/',
        {
            'title': 'Test title',
            'price': 15.00,
            'author': author.id,
            'publisher': publisher.id,
        },
        format='json'
    )
    assert response.status_code == 401


@pytest.mark.django_db
def test_update_book_by_owner(api_client, user, author, publisher):
    book = Book.objects.create(title='Old title', price=10.00, author=author, publisher=publisher, owner=user)
    login_url = reverse('token_obtain_pair')
    tokens = api_client.post(
        login_url,
        {
            'username': 'testuser', 'password': 'testpassword',
        },
        format='json'
    ).data

    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {tokens["access"]}')
    response = api_client.put(
        f'/api/books/{book.id}/',
        {
            'title': 'New title',
            'price': 15.00,
            'author': author.id,
            'publisher': publisher.id
        },
        format='json'
    )
    assert response.status_code == 200
    assert response.data['title'] == 'New title'


@pytest.mark.django_db
def test_update_book_by_not_owner(api_client, user, user2, author, publisher):
    book = Book.objects.create(title='Old title', price=10.00, author=author, publisher=publisher, owner=user2)

    login_url = reverse('token_obtain_pair')
    tokens = api_client.post(
        login_url,
        {
            'username': 'testuser', 'password': 'testpassword',
        },
        format='json'
    ).data

    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {tokens["access"]}')
    response = api_client.put(
        f'/api/books/{book.id}/',
        {
            'title': 'New title',
            'description': 'test description',
            'price': 15.00,
            'author': author.id,
            'publisher': publisher.id
        },
        format='json'
    )
    assert response.status_code == 403


@pytest.mark.django_db
def test_update_book_with_incorrect_fields(api_client, user, author, publisher):
    book = Book.objects.create(title='Old title', price=10.00, author=author, publisher=publisher, owner=user)
    login_url = reverse('token_obtain_pair')
    tokens = api_client.post(
        login_url,
        {
            'username': 'testuser', 'password': 'testpassword',
        },
        format='json'
    ).data

    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {tokens["access"]}')
    response = api_client.put(
        f'/api/books/{book.id}/',
        {
            'title': 'New title',
            'price': 'number',
            'author': author.id,
            'publisher': publisher.id
        },
        format='json'
    )
    assert response.status_code == 400


@pytest.mark.django_db
def test_delete_book_no_auth(api_client, user, author, publisher):
    book = Book.objects.create(title='Test book', price=10.00, author=author, publisher=publisher, owner=user)
    response = api_client.delete(f'/api/books/{book.id}/')
    assert response.status_code == 401


@pytest.mark.django_db
def test_delete_book_by_owner(api_client, user, author, publisher):
    book = Book.objects.create(title='Test book', price=10.00, author=author, publisher=publisher, owner=user)

    login_url = reverse('token_obtain_pair')
    tokens = api_client.post(
        login_url,
        {
            'username': 'testuser', 'password': 'testpassword',
        },
        format='json'
    ).data

    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {tokens["access"]}')
    response = api_client.delete(f'/api/books/{book.id}/')
    assert response.status_code == 204


@pytest.mark.django_db
def test_delete_book_by_not_owner(api_client, user, user2, author, publisher):
    book = Book.objects.create(title='Test book', price=10.00, author=author, publisher=publisher, owner=user2)

    login_url = reverse('token_obtain_pair')
    tokens = api_client.post(
        login_url,
        {
            'username': 'testuser', 'password': 'testpassword',
        },
        format='json'
    ).data

    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {tokens["access"]}')
    response = api_client.delete(f'/api/books/{book.id}/')
    assert response.status_code == 403


@pytest.mark.django_db
def test_delete_non_existent_book(api_client, user):
    login_url = reverse('token_obtain_pair')
    tokens = api_client.post(
        login_url,
        {
            'username': 'testuser', 'password': 'testpassword',
        },
        format='json'
    ).data

    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {tokens["access"]}')
    response = api_client.delete('/api/books/10/')
    assert response.status_code == 404
