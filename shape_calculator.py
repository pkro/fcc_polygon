class Rectangle:
  def __init__(self, width, height):
    self.set_width(width)
    self.set_height(height)

    pass

  def set_width(self, width):
    self.width = width
    

  def set_height(self, height):
    self.height = height
    

  def get_area(self):
    '''Returns area (width * height)'''
    return self.width * self.height

  def get_perimeter(self): 
    '''Returns perimeter (2 * width + 2 * height)'''
    return 2 * self.width + 2 * self.height

  def get_diagonal(self): 
    '''Returns diagonal'''
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self, fill=True): 
    '''Returns a string that represents the shape using lines of "*". The number
    of lines should be equal to the height and the number of "*" in each line
    should be equal to the width. There should be a new line (\n) at the end of
    each line. If the width or height is larger than 50, this should return the
    string: "Too big for picture.".'''
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    
    rows = ['*'*self.width]
    filler = '*' if fill else ' '

    if self.height >2:
      rows[1:] = [f'*{filler*(self.width-2)}*' for i in range(self.height-2)]
    
    if self.height > 1:
      rows.append(rows[0])
    
    return "\n".join(rows) + '\n'
  
  def __str__(self):
    return f'{type(self).__name__}(width={self.width}, height={self.height})'

  
  def get_amount_inside(self, shape): 
    '''Takes another shape (square or rectangle) as an argument. Returns the
    number of times the passed in shape could fit inside the shape (with no
    rotations). For instance, a rectangle with a width of 4 and a height of 8
    could fit in two squares with sides of 4.'''
    w = shape.width
    h = shape.height
    times_w = self.width // w
    times_h = self.height // h
    return times_w * times_h

class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)
  
  def set_side(self, side):
    super().set_height(side)
    super().set_width(side)

  def __str__(self):
    return f'{type(self).__name__}(side={self.width})'

