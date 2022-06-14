from http import client
from urllib import response
from src.lib.utils import temp_file

from src.webserver import create_app

from src.domain.user import UsersRepository

def test_should_save_a_user_by_post_method():
        user_repository = UsersRepository(temp_file())
        app = create_app(repositories={"users": user_repository})
        client = app.test_client()
        
        user = {"id":"01",
                "user": "Steph",
                "password": "passw"}
        
        response = client.post("/api/user" ,  json = user)
        assert response.status_code == 200   
    
def test_shouldnt_save_user_with_same_id():
        user_repository = UsersRepository(temp_file())
        app = create_app(repositories={"users": user_repository})
        client = app.test_client()
        
        user = {"id":"1",
                "user": "Steph",
                "password": "pass"}
        
        user2 = {"id":"1",
                "user": "Steph",
                "password": "pass"}
        
        response = client.post("/api/user" ,  json = user)
        response = client.post("/api/user" ,  json = user2)
        assert response.status_code == 401