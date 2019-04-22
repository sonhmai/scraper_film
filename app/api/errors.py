from flask import jsonify


def bad_request(message):
    payload = {
        'error': 'Bad Request'
    }
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = 400
    return response
