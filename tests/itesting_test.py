import unittest


# 测试类必须要继承TestCase
class ITestingTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("整个测试类只执行一次")

    def setUp(self) -> None:
        print('每个测试开始前执行一次')

    # 测试用例默认已test开头
    def equal_test(self):
        self.assertEqual(1, 1)

    def test_not_equal(self):
        self.assertEqual(1, 0)

    def tearDown(self) -> None:
        print("每个测试用例结束后执行一次")

    @classmethod
    def tearDownClass(cls) -> None:
        print("整个测试类执行一次")