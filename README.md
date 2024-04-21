# Flask Login API

API made to authenticate users with a database.

## Functionalities

- Create user, edit info or delete it.
- Authentication and logout.
- Role based administration.

## Technologies Used

- Python
- SQLAlchemy
- Flask
- Flask-login
- SQLite
- Bcrypt
- Docker

## Installing the Project

```
git clone *projet-url*

cd *projects-directory*

pip3 install -r requirements.txt
```

## Routes

### User Routes

#### Create User

```http
  POST /user
```

| Body Data   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `username` | `string` | **Mandatory**. User name. |
| `password` | `string` | **Mandatory**. User password. |
| `role` | `string` | **Optional**. User role, default is user, can be admin. |

#### Login

```http
  POST /login
```

| Body Data   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `username` | `string` | **Mandatory**. User name. |
| `password` | `string` | **Mandatory**. User password. |

#### Logout

```http
  GET /logout
```

#### Fetch Users Name

```http
  GET /user:id
```

| Param Data   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `integer` | **Mandatory**. User's ID. |


#### Edit User

```http
  PUT /user/:id
```

| Param Data   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `integer` | **Mandatory**. User's ID. |


| Body Data   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `username` | `string` | **Mandatory**. User name. |
| `password` | `string` | **Mandatory**. User password. |
| `role` | `string` | **Optional**. User role, default is user, can be admin. |


#### Delete a User

```http
  DELETE /user/:id
```


| Param Data   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `integer` | **Mandatory**. User's ID. |

