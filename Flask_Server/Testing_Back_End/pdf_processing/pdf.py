import json

def test (path: str) -> json:
    """TO BE IMPLEMENTED

    Args:
        path (str): path to the pdf file

    Returns:
        json: returns a json file with the data
    """    
    data = {
        "courses": ["cmsc131", "cmsc132", "cmsc216"],
        "policies": [{"testing": "you will fail lol"}, {"cheating": "get out"}]
    }
    return json.dumps(data)