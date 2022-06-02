from pydoc import cli
from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.round import RoundsRepository

def test_save_a_round_round_by_post_method():
    round_repository = RoundsRepository(temp_file())
    app = create_app(repositories={"round": round_repository})
    client = app.test_client()
    
    body =  {"game_numer" : "1",
            "game_name" : "Match",
            "id_user" : "01",
            "wrong_matches" : "4",
            "date" : (2020, 12, 25)}
    
    response = client.post("/api/results", json = body)
    
    assert response.status_code == 200    
    