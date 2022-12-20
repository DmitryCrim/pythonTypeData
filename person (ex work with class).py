# class Person():
#     """Модель человека"""
#
#     def __init__(self, name, age):
#         """Инициализация атрибутов человека: имя, возраст"""
#         self.name = name
#         self.age = age
#         print('Человек создан')
#
#     def sing(self):
#         """Просим человека спеть"""
#         print(self.name + " поёт")
#
#     def dance(self):
#         """Просим человека станнцевать"""
#         print(self.name + " танцует")
#
# man = Person ('Victor', 32)
# woman = Person ('Victorya', 28)
# print(man.name)
# man.dance()
# woman.sing()

class Person():
    """Создаем человека"""

    def __init__(self, name, age, height, weight):
        """Инициализируем атрибуты"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        """Можно использовать дефолтные значения self.weight = 100, но в атрибутах данный показатель удаляем"""

    def description_person (self):
        """Описание человека"""
        description = self.name + "ему" + str(self.age) + " его рост" + str(self.height) + "его вес " + str(self.weight)
        print(description)

    def get_weight(self):
        print("Вес человека "  + str(self.weight))

    def update_weight(self, kg):
        self.weight = kg

man = Person('Alex', 30, 188, 100)
# man.weight = 110 cмотри описание дефолтного значения
man.description_person()
man.get_weight()



