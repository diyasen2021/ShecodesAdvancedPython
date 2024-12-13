class User:

  def __init__(self, fname, lname):
    print("New user initialised")
    self.fname = fname
    self.lname = lname

  def full_name(self):
    print(f"{self.fname} {self.lname}")

  def change_fname(self, newname):
    self.fname = newname


diya = User(fname="Diya", lname="Sen")
diya.full_name()

suvra = User(fname="Suvra", lname="Sen")
suvra.full_name()
suvra.change_fname("Heman")
suvra.full_name()
