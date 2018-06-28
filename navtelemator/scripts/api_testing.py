import requests
import json


telemator_base = 'http://srv-telemator.ikt.uninett.no:8080/telemator/equipment/'



def get_telemator_equipment(id):
    response = requests.get(telemator_base + id)
    return response


def post_telemator_equipment():
    url = 'http://srv-telemator.ikt.uninett.no:8080/telemator/equipment/'
    payload = {
        "Equipment" : {"addr1": "test", "End": "1"}
    }
    headers = {'content-type': 'application/json; charset=utf-8'}

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response)


if __name__ == '__main__':
    post_telemator_equipment()