'''
HTML_REPORT
author:test_cy
'''

import os
import time
import HTMLTestRunner


class GenerateReport:

    def __init__(self):
        now = time.strftime("%Y-%m-%d-%H-%M", time.localtime(time.time()))
        self.report_name = 'test_report_' + now + ".html"
        self.test_base = os.path.dirname(os.path.dirname(__file__))
        self.testReport_path = os.path.join(self.test_base, "test_report")
        print(self.test_base)
        if os.path.exists(os.path.join(self.testReport_path, self.report_name)):
            os.remove(os.path.join(self.testReport_path, self.report_name))
        fp = open(os.path.join(self.testReport_path, self.report_name), 'a')
        fp.close()

    def generate_report(self, test_suites):
        fp = open(os.path.join(self.testReport_path, self.report_name), 'a', encoding='utf-8')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test_report', description="Auto_test_report")
        runner.run(test_suites)
