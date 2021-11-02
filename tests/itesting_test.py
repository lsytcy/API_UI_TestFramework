import unittest

flag = False


# 测试类必须要继承TestCase
class ITestingTest(unittest.TestCase):

    """"
    @unittest.skip() 执行时直接忽略掉被装饰的测试用例
    @unittest.skipIf() 如果 skipIf 里的条件成立，执行时直接忽略掉被装饰的测试用例
    @unittest.skipUnless() 永久在执行时忽略被装饰的测试用例，除非 skipUnless 里的条件成立；
    @unittest.expectedFailure期望被装饰的测试用例是失败的，如果是失败的，则此条测试用例将被标记为测试通过
    """

    @classmethod
    def setUpClass(cls) -> None:
        print("整个测试类只执行一次")

    def setUp(self) -> None:
        print('每个测试开始前执行一次')

    # 测试用例默认已test开头
    @unittest.skip("直接跳过该测试用例")
    def equal_test(self):
        self.assertEqual(1, 1)

    @unittest.skipIf(flag, "flag为True则skip")
    def test_not_equal(self):
        self.assertEqual(1, 0)

    @unittest.skipUnless(flag, "flag为false则skip")
    def test_not_equal1(self):
        self.assertEqual(1, 0)

    @unittest.expectedFailure
    def test_not_equal2(self):
        self.assertEqual(1, 0)

    def tearDown(self) -> None:
        print("每个测试用例结束后执行一次")

    @classmethod
    def tearDownClass(cls) -> None:
        print("整个测试类执行一次")