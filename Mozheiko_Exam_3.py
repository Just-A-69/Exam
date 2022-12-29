# Все программы залить на GitHub в репозиторий Exam_3 и выслать ссылку на репозиторий с экзаменом мне

# 1. Напишите функцию, которая запрашивает у пользователя номер
# карты, CVC-код и PIN-код. После этого выводит на экран номер
# карты с первыми четырьмя цифрами, остальные заменены на звездочки,
# CVC-код в виде ###, и PIN-код в виде &&&0 (вместо 0 последняя цифра).

def card_info():

    card_num = (input('Введите номер карты: '))
    pin = list(input('Введите PIN-код карты: '))
    cvc = list(input('Введите CVC-код карты: '))

    protected_card_num = card_num[0:4] + '*' * (len(card_num) - 4)
    protected_cvc = ""
    for i in cvc:
        protected_cvc += '#'

    protected_pin = ''
    for i in range(len(pin) - 1):
        protected_pin += '&'
    protected_pin += pin[-1]

    print('Card: ', protected_card_num)
    print('CVC: ', protected_cvc)
    print('Pin: ', protected_pin)

card_info()

# 2. Напишите функцию, которая возвращает True, если введенный текст читается
# одинаково слева-направо и справа-налево. Иначе – False. Допишите к функции
# декоратор, который выведет имя функции, ее аргумент.
#

def decorator(function):
    def shower(arg):
        print(f'Название функции: {str(function.__name__)}\n'
              f'Аргумент функции: {str(arg)}')
        return function(arg)
    return shower


@decorator
def is_palindrome(text):
    if str(text).lower() == str(text).lower()[::-1]:
        return True
    else:
        return False


print(is_palindrome('Арозаупаланалапуазора'))
print((is_palindrome(123456)))

# 3. Дописать в классы Company, Programmer абстрактные методы
# (хотя бы 1). В коде должны быть Private и Protected методы и свойства.

from time import sleep
from abc import abstractmethod


class Company:

    __money = 0

    levels = {1: 'Junior',
              2: 'Middle',
              3: 'Senior',
              4: 'Lead'}

    def __init__(self, index):
        self._index = index
        self._levels = self.levels[index]

    def _level_up(self):
        if self._index <= 3:
            self._index += 1
            self._levels = self.levels[self._index]
            print('Ты стал', self._levels)
        else:
            print('Ты уже Лид. Теперь пора открывать свою компанию!')

    def is_lead(self):
        if self._index == 4:
            print('Твой уровень: Lead')
        else:
            print('Пока что ты не лид. Ты', self._levels)

    def __get_money(self):
        self.__money += 1000

    def _work_for_money(self):
        print('Молодец, хорошо поработал!')
        self.__get_money()

    def show_money(self):
        print("На счету:", self.__money)

    @abstractmethod
    def go_to_sleep(self):
        pass


x = Company(1)
x.is_lead()


class Programmer(Company):

    def __init__(self, name, age, level):
        super().__init__(level)
        self.name = name
        self.age = age
        self.level = self.levels[level]

    def work(self):
        self._level_up()

    def info(self):
        print(f'Имя: {self.name}\n'
              f'Возраст: {self.age} лет\n'
              f'Квалификация: {self._levels}')

    def knowledge_base(self):
        print('Зачем вставлять какой-то текст, если можно...\n...')
        sleep(1)
        print('Показать что-то стоящее?')
        sleep(1.5)
        print('https://clck.ru/Vmr3g')

    def go_to_sleep(self):
        print('Ты выспался. Теперь неделя без сна!')


q = Programmer("Andrew", 26, 3)
q._work_for_money()
q.info()
q.go_to_sleep()
q.show_money()

# 4. Создайте класс на тему животных. Используйте статические и динамические
# переменные, дочерний (1 или более) классов на конкретное животное. Публичные
# и приватные методы. Полиморфизм (одинаковые названия методов info в обоих
# классах, которые выводят информацию о животных, либо о конкретном животном данного класса).
# Создайте объекты каждого класса и обратитесь к каждому методу. Напишите один staticmethod,
# один classmethod, к которым также обратитесь.


class Animals:

    __name = 'Супер Животное'
    __hunger = 2
    __energy = 2
    __amount_of_food = 0

    def __init__(self, weight, color):
        self.weight = weight
        self.color = color

    def __is_we_alive(self):
        if self.__hunger < 1 or self.__energy < 1:
            print('Животное больше не с нами')
            return False
        else:
            return True

    def eat(self):
        if not self.__is_we_alive():
            print('Мертвое не может есть')
        elif self.__amount_of_food < 1:
            print('Нет еды. Нужно охотиться!')
        else:
            self.__hunger -= 1
            self.__energy += 1
            self.__amount_of_food -= 1
            print('Еда восстановила энергию!')

    def sleep(self):
        if not self.__is_we_alive():
            print('Сон невозможен')
        else:
            self.__energy += 1
            self.__hunger -= 0.5
            print('Сон принес новую энергию')

    def hunting(self):
        if not self.__is_we_alive():
            print('Охота невозможна')
        else:
            self.__energy -= 1
            self.__hunger += 1
            self.__amount_of_food += 1
            print('Еды стало больше')

    def info(self):
        print(f'Голод: {self.__hunger}\n'
              f'Энергия: {self.__energy}\n'
              f'Запас еды: {self.__amount_of_food}')

    @classmethod
    def hand_of_god(cls):
        cls.__energy += 10
        cls.__hunger -= 10
        cls.__amount_of_food += 10
        print('Боги помогли животному!')

    @staticmethod
    def show_name():
        print('Имя: ', Animals.__name)


any_animal = Animals(100, 'green')
any_animal_2 = Animals(69, 'pink')
any_animal.hunting()
any_animal.sleep()
any_animal.eat()
any_animal.hunting()
any_animal.hunting()
any_animal.sleep()
any_animal.info()
any_animal.show_name()
Animals.hand_of_god()
any_animal.info()
any_animal_2.info()


class Elephant(Animals):

    def __init__(self, name, weight, color):
        super().__init__(weight, color)
        self.name = name
        self.weight = weight
        self.color = color

    def info(self):
        print(f'Имя: {self.name}\n'
              f'Цвет: {self.color}')

    def super_info(self):
        Animals.info(self)


z = Elephant('Слон', 800, 'серый')
z.info()
z.hunting()
z.super_info()