from src.lib.utils import temp_file

from src.webserver import create_app

from src.domain.asocia import AsociaRepository


def test_should_save_a_user():
    asocia_repository = AsociaRepository(temp_file())
    app = create_app(repositories={"asocia": asocia_repository})
    client = app.test_client()

    response = client.get("/api/asocia")

    assert response.json == []