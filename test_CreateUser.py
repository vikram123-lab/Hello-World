import requests
import json
import jsonpath
import pytest
# API URL
url = "https://reqres.in/api/users"

def test_create_new_user():
    #read input json file
    file = open('C:\\Users\\Lenovo\\PycharmProjects\\API_TEST\\File_folder\\CreateUser.json','r')
    json_input = file.read()
    requests_json = json.loads(json_input)
    response=requests.post(url,requests_json)
    assert response.status_code==201


def test_create_othe_user():
    #read input json file
    file = open('C:\\Users\\Lenovo\\PycharmProjects\\API_TEST\\File_folder\\CreateUser.json','r')
    json_input = file.read()
    requests_json = json.loads(json_input)
    response=requests.post(url,requests_json)
    print(response.headers.get('Content-Length'))
    response_json=json.loads(response.text)
    id = jsonpath.jsonpath(response_json,'id')
    print(id[0])