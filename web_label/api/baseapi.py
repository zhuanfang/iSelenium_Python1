import json

import requests


class BaseApi:
    params = {}

    def send(self,data):
        raw_data = json.dumps(data)
        for key,value in self.params.items():
            raw_data = raw_data.replase("${"+key+"}",value)
        data = json.loads(raw_data)
        return requests.request(**data).json()


# def test_1(**data):
#     data = {
#         "A":"a",
#         "B":"b",
#         "C":"c"
#     }
#     for key,value in data.items():
#         #print('\n'"{}=={}".format(key,value))
#         print(f"\n{key}=={value}")


