# lib_plugin

## python dynamic load moudle and class

#### demo.py

```python
from lib_plugin import Plugin, Module, PluginManager


if __name__ == '__main__':
    _module = PluginManager.get_module('.', 'demo_module')
    if _module:
        module = Module(_module)
        module.init()
        module.destory()

    _plugin_classA = PluginManager.get_class('.', 'demo_module', 'ClsA')
    if _plugin_classA:
        pluginA = Plugin(_plugin_classA)
        pluginA.init()
        pluginA.destory()

    _plugin_classB = PluginManager.get_class('.', 'demo_module', 'ClsB')
    if _plugin_classB:
        pluginB = Plugin(_plugin_classB)
        pluginB.init()
        pluginB.destory()
```


#### demo_module.py

```python
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
```