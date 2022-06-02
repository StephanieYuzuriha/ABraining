from flask import Flask, request
from flask_cors import CORS
from src.lib.utils import object_to_json
from datetime import date, datetime
from src.domain.asocia import AsociaRepository, AsociaQuestion
from src.domain.round import Round, RoundsRepository

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

    
    @app.route("/api/asocia", methods=["GET"])
    def get_asocia_game():
        game = repositories["asocia"].get_asocia_game()
        return object_to_json(game)
    
    @app.route("/api/results", methods=["POST"])
    def post_results():
        body = request.json
        round = Round(
            game_name = body["game_name"],
            id_user = body["id_user"],
            wrong_matches= body["wrong_matches"],
            date = datetime.today()
            )
        repositories["round"].save(round)
        print(round)
        return ""
    
    @app.route("/api/results", methods=["GET"])
    def get_results():
        results = repositories["results"].get_results()
        return object_to_json(results)
     
    # @app.route("/api/img_list", methods=["GET"])
    # def get_asocia_img_random_list():
    #     img_list = repositories["asocia"].get_asocia_img_with_id()        
    #     return object_to_json(img_list)
    
    # @app.route("/api/desc_list", methods=["GET"])
    # def get_asocia_desc_random_list():
    #     desc_list = repositories["asocia"].get_asocia_desc_with_id()
        
    #     return object_to_json(desc_list)

       
    # @app.route("/api/user", methods=["GET"])
    # def info_get():
    #     info = repositories["info"].get_info()
    #     return object_to_json(info)


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
