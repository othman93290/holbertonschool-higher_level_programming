#!/usr/bin/python3
""" rectangle """


from models.base import Base


class Rectangle(Base):
    """ rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) not in [int]:
            raise TypeError('width must be an integer')

        if value <= 0:
            raise ValueError('width must be > 0')

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) not in [int]:
            raise TypeError('height must be an integer')

        if value <= 0:
            raise ValueError('height must be > 0')

        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) not in [int]:
            raise TypeError('x must be an integer')

        if value < 0:
            raise ValueError('x must be >= 0')

        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) not in [int]:
            raise TypeError('y must be an integer')

        if value < 0:
            raise ValueError('y must be >= 0')

        self.__y = value

    def area(self):
        """ area """
        return self.width * self.height

    def display(self):
        """ display """
        for _ in range(self.y):
            print()
        line = ' ' * self.x + '#' * self.width
        print('\n'.join([line for _ in range(self.height)]))

    def __str__(self):
        s = ''
        s += '[Rectangle] '
        s += '(%s) ' % (self.id)
        s += '%s/%s' % (self.x, self.y)
        s += ' - '
        s += '%s/%s' % (self.width, self.height)
        return s

    def update(self, *args, **kwargs):
        """ update """

        if not args:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                if k == 'width':
                    self.width = v
                if k == 'height':
                    self.height = v
                if k == 'x':
                    self.x = v
                if k == 'y':
                    self.y = v

            return

        for i, v in enumerate(args):
            if i == 0:
                self.id = v
            if i == 1:
                self.width = v
            if i == 2:
                self.height = v
            if i == 3:
                self.x = v
            if i == 4:
                self.y = v

    def to_dictionary(self):
        """ to dictionary """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y,
        }