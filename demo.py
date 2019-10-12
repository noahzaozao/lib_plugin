
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
