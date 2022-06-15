from flask import Flask, request, jsonify
from flask_cors import CORS
from src.lib.utils import object_to_json
from datetime import date
from src.domain.round import Round
from src.domain.user import User


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/auth/login", methods=["POST"])
    def login():
        body = request.json
        user = repositories["users"].get_by_id(body["user"])
        if user is None or (body["password"]) != user.password or body["user"] == "":
            return "", 401
        
        return user.to_dict(), 200


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
        user_id = request.headers.get("Authorization")
        body = request.json
        print(user_id, body["id_user"] )
        if user_id == body["id_user"]:
            round = Round(
                game_name = body["game_name"],
                id_user = body["id_user"],
                wrong_matches= body["wrong_matches"],
                date = date.today()
                )
            repositories["rounds"].save(round)
            return "", 200
        return "", 401
    
    @app.route("/api/results", methods=["GET"])
    def get_results():
        user_id = request.headers.get("Authorization")
        results = repositories["rounds"].get_all_rounds_by_user(user_id)
        return object_to_json(results)
    
    
    @app.route("/api/user", methods=["POST"])
    def post_user():
        body = request.json
        print(body)
        user = User(
            id = body["id"],
            name = body["user"],
            password = body["password"],
            
            )
        
        verifyUser = repositories["users"].get_by_id(user.id)
        
        if verifyUser == None:
            repositories["users"].save(user)
            return "", 200
        return "", 401
    
    @app.route("/api/profile/<user_id>", methods=["GET"])
    def user_get(user_id):
        user = repositories["users"].get_by_id(user_id)
        return object_to_json(user)
     
    # @app.route("/api/img_list", methods=["GET"])
    # def get_asocia_img_random_list():
    #     img_list = repositories["asocia"].get_asocia_img_with_id()        
    #     return object_to_json(img_list)
    
    # @app.route("/api/desc_list", methods=["GET"])
    # def get_asocia_desc_random_list():
    #     desc_list = repositories["asocia"].get_asocia_desc_with_id()
        
    #     return object_to_json(desc_list)

       
    


    return app
