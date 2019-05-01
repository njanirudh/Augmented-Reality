
# https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python

class Singleton(object):
    """
    Singleton class 
    """
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance


