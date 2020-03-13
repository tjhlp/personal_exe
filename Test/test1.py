# class Demo(object):
#     def __init__(self):
#         self.__age = 10
#
#     def get_age(self):
#         return self.__age
#
#
#     def set_age(self, new_age):
#         self.__age = new_age
#
#     age = property(get_age, set_age)
# d1 = Demo()
# print(d1.age)
# d1.age = 100
# print(d1.age)
class Demo(object):
    def __init__(self):
        self.__age = 10

    @property
    def age_demo(self):
        return self.__age

    @age_demo.setter
    def age_demo(self, new_age):
        self.__age = new_age


d1 = Demo()
print(d1.age_demo)
d1.age_demo = 100
print(d1.age_demo)



