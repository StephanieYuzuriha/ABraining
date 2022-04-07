
import sqlite3
from src.lib.utils import object_to_json, temp_file

from src.webserver import create_app

from src.domain.asocia import AsociaQuestion, AsociaRepository


def test_should_return_empty_list_of_asocia_questions():
    asocia_repository = AsociaRepository(temp_file())
    app = create_app(repositories={"asocia": asocia_repository})
    client = app.test_client()

    response = client.get("/api/asocia")

    assert response.json == []

    
def test_should_return_list_of_asocia_questions():

    asocia_repository = AsociaRepository(temp_file())
    app = create_app(repositories={"asocia": asocia_repository})
    client = app.test_client()

    question1 = AsociaQuestion(
        img_id="apple.jpg",
        description="Red"
    )
    question2 = AsociaQuestion(
        img_id="treeLeaf.jpg",
        description="Green"
    )

    asocia_repository.save(question1)
    asocia_repository.save(question2)

    response = client.get("/api/asocia")

    assert response.json == [
        {"id":1, "img_id":"apple.jpg","description":"Red"},
        {"id":2, "img_id":"treeLeaf.jpg","description":"Green"}
        ]
