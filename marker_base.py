from abc import ABC, abstractmethod

class MarkerBase(ABC):

    @abstractmethod
    def set_input_image(self, input):
        pass

    @abstractmethod
    def set_json_parameters(self,params):
        pass

    @abstractmethod
    def process_image(self):
        pass

    @abstractmethod
    def get_output_image(self):
        pass