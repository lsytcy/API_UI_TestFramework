import unittest


class TestToRun(unittest.TestCase):

    def setUp(self):
        # 这里写setUp的方法，通常是打开浏览器
        pass

    def testAssertNotEqual(self):
        self.assertNotEqual(1, 2)
        # 这里写具体的search方法

    def testAssertEqual(self):
        self.assertEqual(1, 1)

    def tearDown(self):
        pass
        # tearDown方法,测试后的清理工具，比如对测试产生的数据
