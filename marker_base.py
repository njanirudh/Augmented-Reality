from abc import ABC, abstractmethod

class MarkerBase(ABC):

    @abstractmethod
    def set_marker_file(self,path):
        pass

    @abstractmethod
    def set_json_parameters(self,params):
        pass