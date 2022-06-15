from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.round import RoundsRepository

def test_save_a_round_by_post_method():
    round_repository = RoundsRepository(temp_file())
    app = create_app(repositories={"rounds": round_repository})
    client = app.test_client()
    
    body =  {
            "game_name" : "Match",
            "id_user" : "01",
            "wrong_matches" : "4"
            }
    
    response = client.post("/api/results", json = body, headers={"Authorization": "01"})
    
    assert response.status_code == 200    
    
def test_save_a_round_by_post_method_with_different_user_id_auth():
        round_repository = RoundsRepository(temp_file())
        app = create_app(repositories={"rounds": round_repository})
        client = app.test_client()

        body =  {
                "game_name" : "Match",
                "id_user" : "01",
                "wrong_matches" : "4"
                }

        response = client.post("/api/results", json = body, headers={"Authorization": "3"})

        assert response.status_code == 401   
