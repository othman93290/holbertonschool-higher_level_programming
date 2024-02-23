#!/usr/bin/python3
""" square """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ square """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        r = ''
        r += '[Square] '
        r += '(%s) ' % (self.id)
        r += '%s/%s' % (self.x, self.y)
        r += ' - '
        r += '%s' % (self.width)
        return r

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value

    def update(self, *args, **kwargs):
        """ update """
        if args:
            for i, v in enumerate(args):
                if i == 0:
                    self.id = v
                if i == 1:
                    self.size = v
                if i == 2:
                    self.x = v
                if i == 3:
                    self.y = v
        else:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                if k == 'size':
                    self.size = v
                if k == 'x':
                    self.x = v
                if k == 'y':
                    self.y = v

    def to_dictionary(self):
        """ to dictionary """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y,
        }