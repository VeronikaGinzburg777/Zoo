# 1. Создайте базовый класс `Animal`, который будет содержать общие
# атрибуты (например, `name`, `age`) и методы (`make_sound()`,
# `eat()`) для всех животных.
#
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`. Добавьте специфические атрибуты и
# переопределите методы, если требуется (например, различный звук для `make_sound()`).
#
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
#
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать
# информацию о животных и сотрудниках. Должны быть методы для добавления животных
# и сотрудников в зоопарк.
#
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper`
# и `heal_animal()` для `Veterinarian`).


class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass
    def eat(self):
        print(f"{self.name} кушает")

class Bird(Animal):
    def __init__(self, name, age, feater_color):
        super().__init__(name, age)
        self.feater_color = feater_color

    def make_sound(self):
        print(f"{self.name} щебечет")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} издает звуки животного")

class Reptile(Animal):
    def __init__(self, name, age, scale_color):
        super().__init__(name, age)
        self.scale_color = scale_color

    def make_sound(self):
        print(f"{self.name} шипит")

class ZooKepper():
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")

class Veterenarian():
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")

class Zoo():
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)


bird = Bird("Воробей","2", "коричневый")
mammal = Mammal("Медведь", "3", "коричневый")
reptile = Reptile("Питон","4","зеленый")
animals = [bird, mammal, reptile]

zoo_keeper = ZooKepper("Григорий")
vet = Veterenarian("Алиса")

zoo = Zoo("Наш зоопарк")

zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

zoo.add_staff(zoo_keeper)
zoo.add_staff(vet)

for animal in zoo.animals:
    animal.make_sound()

for staff_member in zoo.staff:
    if isinstance(staff_member, ZooKepper):
        staff_member.feed_animal(bird)
    elif isinstance(staff_member, Veterenarian):
        staff_member.heal_animal(mammal)










