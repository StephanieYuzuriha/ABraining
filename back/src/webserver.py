from unittest import result
from flask import Flask, request
from flask_cors import CORS

from src.lib.utils import object_to_json

def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/info", methods=["GET"])
    def info_get():
        info = repositories["info"].get_info()
        return object_to_json(info)

    

    # @app.route("/api/user", methods=["GET"])
    # def info_get():
    #     info = repositories["info"].get_info()
    #     return object_to_json(info)

    @app.route("/api/asocia", methods=["GET"])
    def get_results():
        asocia = repositories["asocia"].get_asocia_game()
        return object_to_json(asocia)
    
    # @app.route("/api/results", methods=["GET"])
    # def get_results():
    #     results = repositories["user"].get_user_results()
    #     return object_to_json(result)

    # @app.route("/api/round", methods=["POST"])
    # def round_post():
    #     body = request.json
    #     round = Round(
    #         id = body["id"],
    #         id_game = body["id_game"],
    #         id_user = body["id_user"],
    #         successes= body["successes"]
    #         )
    #     repositories["round"].save_round()
    #     return ""

    return app
