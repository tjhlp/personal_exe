class Tag:
    def __init__(self, id):
        self.id = id

    def __getitem__(self, item):
        print('这个方法被调用')
        return self.id


a = Tag('This is id')
print(a.id)
print(a['python'])