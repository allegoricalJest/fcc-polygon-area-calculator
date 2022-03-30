class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return (self.width * self.height)

  def get_perimeter(self):
    return (2 * (self.width + self.height))

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** 0.5)

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      output = ""
      for i in range(0, self.height, 1):
        output += "*" * self.width + "\n"
      return output

  def get_amount_inside(self, obj):
    width = obj.width
    height = obj.height

    lateral = self.width / width
    vertical = self.height / height

    return int(lateral * vertical)

  def __str__(self):
    return "Rectangle(width=" + str(self.width)+", height=" + str(self.height) + ")"
      
class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side

  def set_side(self, side):
    self.width = side
    self.height = side

  def set_width(self, side):
    self.width = side
    self.height = side

  def set_height(self, side):
    self.width = side
    self.height = side
  
  def __str__(self):
    return "Square(side=" + str(self.width) + ")"
