HELLO = 'hello'


class Thappulu(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        self.message = args

    def __str__(self):
        return ('\n [THAPPU CHESTUNNAVU!!]: %s' % self.message)

# class CustomError()
