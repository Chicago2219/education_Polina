# class Cat:
#     name = "Кошачьи"
#     sex = None
#
#     def __init__(self, name=None, color=None):  # конструктор класса
#         self.name = name
#         self.color = color
#
#
# cat_1 = Cat("Муся", "Тигристый")  # объект
# cat_2 = Cat("Барсик", "Рыжий")  # экземпляр класса
# print(Cat.__dict__)
# print(cat_1.__dict__)
# print(cat_2.__dict__)
# print(cat_2.name)
# print(cat_1.name)
# print(cat_1.sex)
# cat_3 = Cat()
# print(cat_3.__dict__)

# Парадигмы ООП
# 1. Наследование
# 2. Полиморфизм
# 3. Инкапсуляция
# 4. Абстракция

# C++: int n = 10;  -> 1010 -> [1010]
# Python: n = 10 -> class <'int'> -> 1010 -> [1010]
# print(int)
# print(float)
# print(str)
# print(bool)
# Наследование
# class Dad:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def voice(self):
#         return type(self), "Ну-ну"
#
#
# class Daughter(Dad):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#
#
# dad_1 = Dad("Иван", 37)
# daughter_1 = Daughter("Анна", 7)
# print(dad_1.__dict__)
# print(dad_1.voice())
# print(daughter_1.__dict__)
# print(daughter_1.voice())
# print(type(dad_1))
# print(type(daughter_1))

# Полиморфизм

# class Dad:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def voice(self):
#         return type(self), "Ну-ну"
#
#
# class Daughter(Dad):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#
#     def voice(self):
#         return "У лукоморья дуб зеленый..."
#
#
# dad_1 = Dad("Иван", 37)
# daughter_1 = Daughter("Анна", 7)
# print(dad_1.__dict__)
# print(dad_1.voice())
# print(daughter_1.__dict__)
# print(daughter_1.voice())
# print(type(dad_1))
# print(type(daughter_1))

from accessify import private
# Инкапсуляция
'''
1. Полный доступ income, count, data
2. Ограниченный доступ _income, _count, _data
3. Полный запрет __income, __count, __data
pip install accessify
'''


# class Tesla:
#     count = 1_000_000
#     model = "Tesla 3"
#     _price = 35_000
#     __income = 35_000 * count * 0.65
#
#     def __init__(self, id):
#         self.id = id
#
#     @private
#     def show_speed(self):
#         return "Moscow"
#
#
# tesla_1 = Tesla(32554363521129)
# # print(tesla_1.__dict__)
# # print(Tesla.__dict__)
# # print(tesla_1._price)
# # print(tesla_1._Tesla__income)
# print(tesla_1.show_speed())


# class Cat:
#     count = 0
#
#     def __init__(self, name=None, color=None):
#         self.name = name
#         self.color = color
#         Cat.add_count()
#
#     @staticmethod
#     def voice():
#         return "Мяу-мяу"
#
#     def test(self):
#         pass
#
#     @classmethod
#     def add_count(cls):
#         cls.count += 1
#
#
# cat_1 = Cat()
# cat_2 = Cat()
# cat_3 = Cat()
# print(Cat.count)
# print(cat_1.voice())
# print(Cat.voice())
# print(cat_2.voice())

# Django, FastAPI, Flask
# from flask import Flask
#
#
# app = Flask(__name__)
#
#
# @app.route("/")
# def index():
#     return "<h1>Hello, world!</h1><br><a href='/about'>О нас</a>"
#
#
# @app.route("/about")
# def about():
#     return "<h1>Мы старт-апп, поддержите нас!</h1>"
#
#
# @app.route("/api/v1/<int:x>/<int:y>")  # json, xml
# def api(x, y):
#     return f'''{x} + {y} = {x + y}<br>
#                 {x} - {y} = {x - y}<br>
#                 {x} * {y} = {x * y}'''
#
#
# if __name__ == "__main__":
#     app.run()


# data = {"Полина": 4.75, "Иван": 2.47}
# print(data["Иван"])
