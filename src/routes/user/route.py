from flask import Blueprint

user_bp = Blueprint('user2',__name__)

@user_bp.route("/",methods=["GET"])
def say_hello():
    return jsonify({"msg":"hola"})