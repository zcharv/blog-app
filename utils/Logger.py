class Logger():
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(Logger, cls).__new__(cls)
    return cls.instance
  
  def __init__(self, level='info', file='logs.txt'):
      self.level = level
      self.file = file

  def log(self, message):
      log = f"{self.level}: {message}"
      print(log)
      with open(self.file, "a") as file:
        file.write(log + "\n")

