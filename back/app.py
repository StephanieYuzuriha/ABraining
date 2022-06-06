import sqlite3
from src.domain.round import RoundsRepository
from src.webserver import create_app
from src.domain.info import InfoRepository
from src.domain.asocia import AsociaRepository


database_path = "data/database.db"

repositories = {
    "info": InfoRepository(database_path),
    "asocia": AsociaRepository(database_path),
    "rounds" : RoundsRepository(database_path)
}

app = create_app(repositories)

app.run(debug=True, host="0.0.0.0", port="5000")
