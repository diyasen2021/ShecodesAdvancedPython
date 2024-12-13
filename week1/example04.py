# Class inheritance

class User:

  def __init__(self, name):
    self.name = name


# Inheritance
class FrenchUser(User):

  def greet(self):
    print(f"Bonjour - {self.name}")


# Inheritance
class SpanishUser(User):

  def greet(self):
    print(f"Hola - {self.name}")


diya = FrenchUser("Diya")
diya.greet()

luciano = SpanishUser("luciano")
luciano.greet()
