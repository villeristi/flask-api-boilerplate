from flask import make_response, jsonify


def respond_with(response, status=200):
    """
    Format response to JSON
    :param response: dict
    :param status: integer
    :return: Response
    """
    return make_response(jsonify(response), status)
