
class Person:
    def __init__(self):
        self.name = "kacker"


def foo(l):
    l.append(1)

def bar(d):
    d["name"] = "kacker"

def he(a):
    m = {"a":1}
    for i in m:
        print(i)


if __name__ == '__main__':
    # a = [0]
    # foo(a)

    # a = {}
    # bar(a)

    a = Person()
    he(a)

    print(a.name)
