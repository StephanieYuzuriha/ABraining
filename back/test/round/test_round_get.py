from datetime import date
from src.lib.utils import temp_file

from src.webserver import create_app

from src.domain.round import RoundsRepository, Round

def test_get_rounds_should_return_all_rounds():
    round_repository = RoundsRepository(temp_file())
    app = create_app(repositories={"rounds": round_repository})
    client = app.test_client()
    
    round = Round (
            game_name = "Match",
            id_user = "01",
            wrong_matches = "4",
            date = date(2020, 12, 25))
    
    round2 = Round (
            game_name = "Match",
            id_user = "01",
            wrong_matches = "3",
            date = date(2020, 12, 25))
    
    round3 = Round (
            game_name = "Match",
            id_user = "02",
            wrong_matches = "1",
            date = date(2020, 12, 25))
    
    round_repository.save(round)
    round_repository.save(round2)
    
    resp = client.get("/api/results", headers={"Authorization": "01"})
    assert resp.status_code == 200
    assert resp.json == [{
            "game_name" : "Match",
            "id_user" : "01",
            "wrong_matches" : "4",
            "date" : "2020-12-25"},
            {
            "game_name" : "Match",
            "id_user" : "01",
            "wrong_matches" : "3",
            "date" : "2020-12-25"}]


def test_save_round_without_mistakes_mistakes_should_be_0():
        
    round_repository = RoundsRepository(temp_file())
    app = create_app(repositories={"rounds": round_repository})
    client = app.test_client()
    
    round = Round (
            game_name = "Match",
            id_user = "01",
            wrong_matches = "",
            date = date(2020, 12, 25))
    
    round_repository.save(round)
    
    resp = client.get("/api/results", headers={"Authorization": "01"})
    assert resp.status_code == 200
    assert resp.json == [{
            "game_name" : "Match",
            "id_user" : "01",
            "wrong_matches" : "0",
            "date" : "2020-12-25"}]  