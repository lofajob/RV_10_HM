# /usr/bin/python
# -*- coding: utf-8 -*-


class Singleton(object):
    """Example of singleton pattern from Wiki"""
    obj = None

    def __new__(cls, *dt, **mp):
        """
        if instant not created then call __new__ method
        of parent
        """
        if cls.obj is None:
            cls.obj = object.__new__(cls, *dt, **mp)
        return cls.obj



class NewClass:
    """Example of Singleton pattern by Oleksandr"""
    var1 = 1

    @classmethod
    def change_attr(cls, value):
        cls.var1 = value


if __name__ == "__main__":
    ex = NewClass()
    ex2 = NewClass()

    s = Singleton()
    s2 = Singleton()