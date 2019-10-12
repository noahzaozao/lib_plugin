
def init():
    print('module.init()')


def destory():
    print('module.destory()')


class ClsA(object):
    def __init__(self):
        super(ClsA, self).__init__()
        print('ClsA.__init__')

    def init(self):
        print('ClsA.init()')

    def destory(self):
        print('ClsA.destory()')


class ClsB(object):
    def __init__(self):
        super(ClsB, self).__init__()
        print('ClsB.__init__')

    def init(self):
        print('ClsB.init()')

    def destory(self):
        print('ClsB.destory()')
