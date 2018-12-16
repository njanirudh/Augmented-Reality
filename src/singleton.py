
# https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python

# Singleton base class
class Singleton(object):
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance


