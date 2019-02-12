import json
from src.singleton import Singleton
from pprint import pprint

class JsonReader(Singleton):
    """

    """
    def __init__(self):
        self.__json_data = None


    def read_from_file(self,path):
        """

        :param path:
        :return:
        """
        with open(path , encoding='utf-8') as f:
            self.__json_data = json.load(f)


    def print_json(self):
        pprint(self.__json_data)

    def get_value(self,key):
        return self.__json_data[key]

