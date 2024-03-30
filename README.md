# API_UI_TestFramework介绍

# 基于pytest,requests,appium,selenium框架的自动化测试项目
## 环境需求
* 需要python3.10+
* 安装pip install -r requirements.txt
* 在当前项目根目录下执行会下载依赖，完成后会生成.venv的虚拟环境目录
* IDE里配置一下python环境，选择项目中的.venv/bin/python作为虚拟环境

## 目录说明
- 测试用例统一放下在tests目录下，每个业务线各创建一个子目录，各自放自己的用例。接口测试用例放test_api,移动端自动化用例放test_appium,Web端自动化放test_selenium
- 资源类静态文件统一放在resources目录下
- common中存放公共方法, test_report中存放测试报告
- 非测试用例的代码，建议放在test_scripts目录下
- sample.py是作为示例的测试用例，可以根据实际情况保留或删除

## 测试编写
- 测试用例文件名必须是`test_*.py`或者`*_test.py`的格式，测试用例统一使用类来编写
- 测试方法必须以`test`开头，并建议为每个测试方法添加`@pytest.mark.case`装饰器来声明用例的基本信息，如作者、psm等，也可以通过添加`@pytest.mark.tags`来为用例打tag

## 执行测试
- 对于单个用例的执行，可以通过测试类的run_test()方法来执行，例如TestExample().run_test()
- 批量执行则使用框架提供的命令`pytest test`来执行测试，"test"命令后可以带上多个目录（必须是tests的子目录，如tests/doc），不传目录则默认运行整个tests的测试用例。默认在output目录生成测试报告，在logs目录生成日志文件
- 如果在平台上执行，可以使用`bash run_test.sh`作为执行命令

## 代码提交、分支管理
- 平时的代码编写合入main分支
- 需要新增用例到正式测试中时，提merge request，由相关负责人review并合并代码
