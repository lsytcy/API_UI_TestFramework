import importlib.util
import os
import unittest


# 解析tests文件夹，并且返回module的字符串列表
def get_module_name_string(file_dir):
    return_list = []
    for root, dirs, file in os.walk(file_dir):
        for i in file:
            if not (i.endswith("__init__.py") or i.endswith(".pyc")) and i.startswith("test"):
                f = os.path.join(root, i)
                print(f)
                # Windows 的用法
                mod = 'tests.' + f.split('\\tests\\')[1].replace('.py', '').replace('\\', '.')
                # Mac的用法
                # mod = 'test.' + f.split('tests')[1].replace('.py', // '').replace('/', '')
                return_list.append(mod)
    return return_list


if __name__ == '__main__':
    '''
    test
    # 定义suits
    suites = unittest.TestSuite()
    # 获取所有的module的string, 类似package.mod的方式
    mod_string_list = (get_module_name_string(os.path.join(os.path.abspath('.'), 'tests')))
    # 遍历每个mod string, import并且把它加入test case 中来
    for mod_string in mod_string_list:
        m = importlib.import_module(mod_string)
        test_case = unittest.TestLoader().loadTestsFromModule(m)
        suites.addTests(test_case)
    # 指定runner为TextTestRunner
    runner = unittest.TextTestRunner(verbosity=2)
    # 运行
    runner.run(suites)
    '''

    # 动态查找测试用例
    loader = unittest.defaultTestLoader
    # 生成测试用的suite
    suite = loader.discover(os.path.join(os.path.abspath('.'), 'tests'), top_level_dir=os.path.abspath('.'))
    # 指定runner为TextTestRunner
    runner = unittest.TextTestRunner(verbosity=2)
    # 运行suite
    runner.run(suite)
