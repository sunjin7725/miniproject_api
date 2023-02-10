from fastapi.encoders import jsonable_encoder


def success_response(return_dict):
    return jsonable_encoder(
        {
            "code": 200,
            'result': return_dict
        }
    )


def error_response(return_dict):
    return jsonable_encoder(
        {
            "code": 200,
            'result': return_dict
        }
    )