# Bookstore

---

### Authentication

#### `POST /register`

* **Usage**: Registration a new user
* **Method**: POST
* **Request body**:
    ```json
    {
    "username": "user",
    "first_name": "example",
    "last_name": "example",
    "email": "user@gmail.com",
    "password": "password",
    "password_check": "password"
    }
    ```
* **Response status**: `201 Created`
* **Response body**:
    ```json
    {
    "username": "user",
    "first_name": "example",
    "last_name": "example",
    "email": "user@gmail.com"
    }
    ```

#### `POST /login`

* **Usage**: Log in
* **Method**: POST
* **Request body**:
    ```json
    {
    "username": "user",
    "password": "password"
    }
    ```
* **Response status**: `200 OK`
    ```json
    {
    "refresh": "example_refresh",
    "access": "example_access"
    }
    ```
  
#### `POST /token/refresh`

* **Usage**: New refresh token
* **Method**: POST
* **Request body**:
    ```json
    {
    "refresh": "example_refresh"
    }
    ```
* **Response status**: `200 OK`
    ```json
    {
    "refresh": "new_example_refresh",
    }
    ```

---

### Books

#### `GET api/books`

* **Usage**: Get a list of books
* **Method**: GET
* **Response status**: `200 OK`
* **Response body**: `List of books`

#### `POST api/books` (owner)

* **Usage**: Add a new book
* **Method**: POST
* **Request body**:
    ```json
    {
    "title": "Example book title",
    "description": "A description of book.",
    "price": "200.00",
    "author": 1,
    "publisher": 1
    }
    ```
* **Response status**: `201 Created`
* **Response body**:
    ```json
    {
    "id": 1,
    "title": "Example book title",
    "description": "A description of book.",
    "price": "200.00",
    "author": 1,
    "publisher": 1,
    "owner": "current_username",
    "created_at": "Created time"
    }
    ```

#### `GET api/books/{id}`

* **Usage**: Get detailed information about a book
* **Method**: GET
* **Response status**: `200 OK`
* * **Response body**:
    ```json
    {
    "id": 1,
    "title": "Example book title",
    "description": "A description of book.",
    "price": "200.00",
    "author": 1,
    "publisher": 1,
    "owner": "current_username",
    "created_at": "Created time"
    }
    ```

#### `PUT api/books/{id}` (owner)

* **Usage**: Update book information
* **Method**: PUT
* **Request body**:
    ```json
    {
    "title": "Update example book title",
    "description": "A description of book.",
    "price": "150.00",
    "author": 1,
    "publisher": 1
    }
    ```
* **Response status**: `200 OK`
* **Response body**:
    ```json
    {
    "id": 1,
    "title": "Update example book title",
    "description": "A description of book.",
    "price": "150.00",
    "author": 1,
    "publisher": 1,
    "owner": "current_username",
    "created_at": "Created time"
    }
    ```

#### `DELETE api/books/{id}` (owner)

* **Usage**: Delete a book
* **Method**: DELETE
* **Response status**: `204 No Content`

---

### Authors

#### `GET api/authors`

* **Usage**: Get a list of authors
* **Method**: GET
* **Response status**: `200 OK`
* **Response body**: `List of authors`

#### `POST api/authors` 

* **Usage**: Add a new author
* **Method**: POST
* **Response status**: `201 Created`
* **Request body**:
    ```json
    {
    "name": "Example author name",
    "biography": "Example biography author"
    }
    ```
* **Response status**: `201 Created`
* **Response body**:
    ```json
    {
    "id": 1,
    "name": "Example author name",
    "biography": "Example biography author",
    "created_at": "Created time"
    }
    ```

#### `GET api/authors/{id}`

* **Usage**: Get information about an author
* **Method**: GET
* **Response status**: `200 OK`
* **Response body**:
    ```json
    {
    "id": 1,
    "name": "Example author name",
    "biography": "Example biography author",
    "created_at": "Created time"
    }
    ```
#### `PUT api/authors/{id}`

* **Usage**: Update author information
* **Method**: PUT
* **Request body**:
    ```json
    {
    "name": "Update example author name",
    "biography": "Update example biography author"
    }
    ```
* **Response status**: `200 OK`
* **Response body**:
    ```json
    {
    "id": 1,
    "name": "Update example author name",
    "biography": "Update example biography author",
    "created_at": "Created time"
    }
    ```

#### `DELETE api/authors/{id}`

* **Usage**: Delete a author
* **Method**: DELETE
* **Response status**: `204 No Content`

---

### Publishers

#### `GET api/publishers`

* **Usage**: Get a list of authors
* **Method**: GET
* **Response status**: `200 OK`
* **Response body**: `List of publishers`

#### `POST api/publishers` 

* **Usage**: Add a new publisher
* **Method**: POST
* **Response status**: `201 Created`
* **Request body**:
    ```json
    {
    "name": "Example publisher name",
    "address": "Example address publisher"
    }
    ```
* **Response status**: `201 Created`
* **Response body**:
    ```json
    {
    "id": 1,
    "name": "Example publisher name",
    "address": "Example address publisher",
    "created_at": "Created time"
    }
    ```

#### `GET api/publishers/{id}`

* **Usage**: Get information about an publisher
* **Method**: GET
* **Response status**: `200 OK`
* **Response body**:
    ```json
    {
    "id": 1,
    "name": "Example publisher name",
    "address": "Example address publisher",
    "created_at": "Created time"
    }
    ```
#### `PUT api/publishers/{id}`

* **Usage**: Update publisher information
* **Method**: PUT
* **Request body**:
    ```json
    {
    "name": "Update example publisher name",
    "address": "Update example address publisher"
    }
    ```
* **Response status**: `200 OK`
* **Response body**:
    ```json
    {
    "id": 1,
    "name": "Update example publisher name",
    "address": "Update example address publisher",
    "created_at": "Created time"
    }
    ```

#### `DELETE api/publishers/{id}`

* **Usage**: Delete a publisher
* **Method**: DELETE
* **Response status**: `204 No Content`

---

# How to Run Tests

1. **Install dependencies:**
```
pip install -r requirements.txt
```

2. **Run tests:**
```
pytest
```
3. **Run coverage test:**
```
coverage run -m pytest
coverage report
```
