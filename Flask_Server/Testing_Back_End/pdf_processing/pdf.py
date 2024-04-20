import json

def test (path: str) -> json:
    data = {
        "courses": ["cmsc131", "cmsc132", "cmsc216"],
        "policies": [{"testing": "you will fail lol"}, {"cheating": "get out"}]
    }
    return json.dumps(data)