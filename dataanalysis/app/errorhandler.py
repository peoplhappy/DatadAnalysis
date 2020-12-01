"""
  注册错误处理方式
"""
from flask import Blueprint, jsonify
from common.reponsedata import InvalidUsage
errorhandler = Blueprint('error', __name__)

@errorhandler.app_errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

