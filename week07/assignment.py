from abc import ABC, abstractmethod


class Animal(ABC):
  def __init__(self, name, genre, body, characteristic):
    self.name = name
    self.genre = genre
    self.body = body
    self.characteristic = characteristic

  @abstractmethod
  def cry(self):
    pass

  def is_beast(self):
    body_size_dict = {
      '小': 1,
      '中等:': 2,
      '大': 3,
      '巨大': 4
    }

    if self.genre == '食肉' and self.characteristic == '凶猛':
      body_size = body_size_dict[self.body]
      if body_size >= 2:
        return True
    return False


class Cat(Animal):
  def cry(self):
    print('meow')

  def is_fit_for_pet(self):
    return True


class Zoo:
  def __init__(self, name):
    self.name = name
    self.animals = []

  def _is_in_zoo(self, animal_name):
    for a in self.animals:
      if type(a).__name__ == animal_name:
        return True
    return False

  def add_animal(self, animal: Animal):
    if not self._is_in_zoo(type(animal).__name__):
      self.animals.append(animal)

  def __getattr__(self, item):
    return self._is_in_zoo(item)


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')
    is_beast = cat1.is_beast()
    print('a')
