import glob
import pytest

# 测试类
class Sample(object):

    def test_equal(self):
        assert 1 == 1

    def test_not_equal(self):
        assert 1 != 1
