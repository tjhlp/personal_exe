class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, status_number):
        self.status_number = status_number


s1 = Singleton(status_number=2)
s2 = Singleton(status_number=5)
print(s1.status_number)
print(s2.status_number)
