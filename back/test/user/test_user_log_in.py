from src.lib.utils import temp_file

from src.webserver import create_app

from src.domain.user import UsersRepository, User

def setup():
    user_repository = UsersRepository(temp_file())
    app = create_app(repositories={"users": user_repository})
    client = app.test_client()

    steph = User(id='user1', name='Steph', password='pass')
    user_repository.save(steph)

    return client

def test_should_validate_login():
    client = setup()
    print("a")
    body = {
        "user": "user1",
        "password": "pass"
    }
    
    response = client.post(
        "/auth/login", json=body
    )
    print("a")
    assert response.status_code == 200
    assert response.json == {
        'id': 'user1',
        'name': 'Steph',

    }

# def test_should_fail_if_invalid_password():
#     client = setup()

#     body = {
#         "user": "Steph",
#         "password": "ivalid"
#     }
    
#     response = client.post(
#         "/auth/login", json=body
#     )

#     assert response.status_code == 401

# def test_should_fail_if_user_not_exists():
#     client = setup()

#     body = {
#         "user": 'user-not-exists',
#         'password': 'pass'
#     }
#     response = client.post(
#         "/auth/login", json=body
#     )

#     assert response.status_code == 401
