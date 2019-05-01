import json
from src.singleton import Singleton
from pprint import pprint

class JsonReader(Singleton):
    """
    Json Reader
    """
    def __init__(self):
        self.__json_data = None

    def read_from_file(self,path):
        """
        Reads the Json data from a file and converting into
        a json string.
        :param path: path to the json
        :return: json string
        """
        with open(path , encoding='utf-8') as f:
            self.__json_data = json.load(f)


    def print_json(self):
        """
        :return: None
        """
        pprint(self.__json_data)

    def get_value(self,key):
        return self.__json_data[key]

