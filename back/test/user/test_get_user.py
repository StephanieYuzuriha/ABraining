from src.lib.utils import temp_file

from src.webserver import create_app

from src.domain.user import UsersRepository, User


def test_should_save_a_users_and_return_an_specific_user():
    user_repository = UsersRepository(temp_file())
    app = create_app(repositories={"users": user_repository})
    client = app.test_client()
    
    user = User(id = "1",
            name =  "Steph",
            password = "pass")
    
    user2 = User(id = "2",
            name = "Adri",
            password = "pass")
    
    user_repository.save(user)
    user_repository.save(user2)

    response = client.get("/api/profile/1")

    assert response.status_code ==  200
    assert response.json == {"id":"1", "name":"Steph"}
#     assert response["id"] == "1"
#     assert response["name"] == "Steph"
    
