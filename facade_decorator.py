def facade_decorator(method):
    def wrapper(self):
        instance.do_smth()
        instance2.do_smth()
        instance3.do_smth()
    return wrapper



class Ex1():
    """Just class"""
        
    def do_smth(self):
        print "Hello"

    @facade_decorator
    def __call__(self):
        pass


class Ex2():
    """Another class"""
    
    def do_smth(self):
        print "World"

    @facade_decorator
    def __call__(self):
        pass


class Ex3():
    """Third class"""
    
    def do_smth(self):
        print "and Universe"

    @facade_decorator
    def __call__(self):
        pass


if __name__ == "__main__":
    instance = Ex1()
    instance2 = Ex2()
    instance3 = Ex3()
