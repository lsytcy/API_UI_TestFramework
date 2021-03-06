import os
import unittest
from tests.test_to_run import TestToRun
from tests.itesting_test import ITestingTest
from common.html_reporter import GenerateReport
import glob
import pytest

'''
os.path.dirname(os.path.abspath(__file__))--不包含文件名
D:\\python-project\\python-func
os.path.abspath(__file__)--包含文件名
D:\\python-project\\python-func\\test-os.py
'''


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


# 查找所有待执行的测试用例
def find_modules_from_folder(folder):
    absolute_f = os.path.abspath(folder)
    module_names = glob.glob(os.path.join(absolute_f, "*.py"))
    return [f for f in module_names if os.path.isfile(f) and not f.endswith('__init__.py')]


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

    '''
    # 动态查找测试用例
    loader = unittest.defaultTestLoader
    # 生成测试用的suite
    suite = loader.discover(os.path.join(os.path.abspath('.'), 'tests'), top_level_dir=os.path.abspath('.'))
    # 指定runner为TextTestRunner
    runner = unittest.TextTestRunner(verbosity=2)
    # 运行suite
    runner.run(suite)
    '''

    '''
    1、unittest.TestLoader().loadTestsFromModule(m)这种方式并不是只导入“test”开头的模块，在运行时itesting_test.py也被加载了！
    2、unittest.defaultTestLoader.discover这种方式才是默认加载test开头的模块
    3、loader.testMethodPrefix = 'equal'控制的是加载的py文件中的testcase; patter控制的是加载的py文件
    '''

    # 破除默认的pattern
    # loader = unittest.defaultTestLoader
    # 设置运行仅以equal开头的测试用例
    # loader.testMethodPrefix = 'equal'
    """
    suite = unittest.defaultTestLoader.discover(os.path.join(os.path.abspath("."), 'tests'), pattern='*baidu.py',
                                                top_level_dir=os.path.abspath('.'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)    
    """

    # 使用HMTLTestRunner生成测试报告
    """
    suite = unittest.defaultTestLoader.discover(os.path.join(os.path.abspath("."), 'tests'), pattern='*haihuadao.py',
                                                top_level_dir=os.path.abspath('.'))
    html_report = GenerateReport()
    html_report.generate_report(suite)    
    """

    # 在程序中运行pytest
    """
    # 得出测试文件夹地址
    test_folder = os.path.join(os.path.dirname(__file__), 'tests')
    # 得出测试文件夹下的所有测试用例
    target_file = find_modules_from_folder(test_folder)
    # 直接运行所有的测试用例
    pytest.main([*target_file, '-v'])      
    """






