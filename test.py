
class Animal:
    animals: list = []

    def __init__(self, name: str):
        self.name = name

        Animal.animals.append(self)

    def __repr__(self) -> str:
        return f'{self.name}'


a1 = Animal('doggy')
a2 = Animal('Kitty')

print(Animal.animals)