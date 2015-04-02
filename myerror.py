class MyError(Exception):
    def __init__(self):
        self.message = "Error: unable to fecth data"

    def __str__(self):
        return repr(self.message)