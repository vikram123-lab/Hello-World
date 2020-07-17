import pytest
import requests
import json
url = 'http://api.zippopotam.us/us/90210'

def test_get():
    response = requests.get(url)
    json_response = json.loads(response.text)
    print(json_response)

    assert response.status_code == 200

