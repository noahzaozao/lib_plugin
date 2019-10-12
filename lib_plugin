import importlib


class PluginManager(object):
    """
    插件管理类
    """
    @staticmethod
    def get_module(name, package):
        """
        获取模块
        :param name:
        :param package:
        :return:
        """
        try:
            module_obj = importlib.import_module(name, package)
            if not module_obj:
                return None
            return module_obj
        except ModuleNotFoundError as e:
            print(e)
            return None

    @staticmethod
    def get_class(name, package, cls):
        """
        获取类
        :param name:
        :param package:
        :param cls:
        :return:
        """
        try:
            module_obj = importlib.import_module(name, package)
            if not module_obj:
                return None
            try:
                class_obj = getattr(module_obj, cls)
                if not class_obj:
                    return None
                return class_obj
            except AttributeError as e:
                print(e)
                return None
        except ModuleNotFoundError as e:
            print(e)
            return None


class Module(object):
    """
    插件包装类
    """
    def __init__(self, _plugin_module):
        print('Plugin.__init__', _plugin_module)
        self._plugin = _plugin_module

    def init(self):
        """
        初始化
        :return:
        """
        self._plugin.init()

    def destory(self):
        """
        销毁
        :return:
        """
        self._plugin.destory()


class Plugin(object):
    """
    插件包装类
    """
    def __init__(self, _plugin_class):
        print('Plugin.__init__', _plugin_class)
        self._plugin = _plugin_class()

    def init(self):
        """
        初始化
        :return:
        """
        self._plugin.init()

    def destory(self):
        """
        销毁
        :return:
        """
        self._plugin.destory()



