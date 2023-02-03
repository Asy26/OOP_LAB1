import doctest


class Cat:
    count_legs = 4

    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color

    def say_purr(self):
        ...

    def say_meow(self):
        ...


class Tree:

    def __init__(self, name: str, age: int, height: float):
        self.name = name
        self.age = age
        self.height = height

    def check_age(self, age: int) -> None:
        ...
# метод принимает аргумент age и возвращает фразу "Возраст дерева - {age}"

    def cut_down(self):
        ...


class Pizza:

    def __init__(self, count_of_pieces: int, ingredients: list):
        self.count_of_pieces = count_of_pieces
        self.ingredients = ingredients

    def add_ingredients(self, ingredient: str) -> None:
        ...
# метод принимает аргумент ingredient и добавляет его в список ingredients

    def eat_pieces(self, count_of_pieces: int, pieces_eaten: int) -> None:
        ...

    """Usage examples:
        >>> pizza = Pizza(10, ['cheese', 'meat']
        >>> pizza.eat_pieces(10, 2)
        8
        """

# метод принимает два аргумента - изначальное количество кусочков и сколько было съедено и возвращает количество
# кусочков, которые остались

if __name__ == "__main__":
    doctest.testmod()