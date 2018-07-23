import json
from singleton import Singleton
from pprint import pprint


class JsonReader(Singleton):

    json_data = None

    def __init__(self):
        pass

    def read_from_file(self,path):

        with open(path , encoding='utf-8') as f:
            self.json_data = json.load(f)


    def print_json(self):
        pprint(self.json_data)

    def get_value(self,key):
        return self.json_data[key]

