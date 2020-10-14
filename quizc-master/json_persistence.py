from json import JSONEncoder


class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


myclass = MyClass(44, 44)
son = MyEncoder().encode(myclass)
with open("myform.json", "a") as f:
    f.write(son)

