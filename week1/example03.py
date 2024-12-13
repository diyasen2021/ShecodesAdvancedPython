class User:

  def __init__(self, name, birth_year):
    self.name = name
    self.birth_year = birth_year

  def greet(self):
    print(
        f"Welcome {self.name}, you were born in the {self.calculate_century()}"
    )

  def calculate_century(self):
    if self.birth_year < 2000:
      return "20th century"
    elif self.birth_year < 2100:
      return "21st century"


diya = User("Diya", 1981)
diya.greet()

newbie = User("Newbie", 2019)
newbie.greet()
