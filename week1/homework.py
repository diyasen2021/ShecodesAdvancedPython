class Weather:

  def __init__(self, city):
    self.city = city

  def set_weather(self, temp, con):
    self.temp = temp
    self.con = con

  def display_weather(self):
    print(f"City: {self.city}")
    print(f"Temperature: {self.temp}")
    print(f"Condition: {self.con}")

weather1 = Weather("Paris")
weather1.set_weather(25, "Sunny")
weather1.display_weather()
