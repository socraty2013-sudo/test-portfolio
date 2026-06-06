import pytest
from requests import session

from config.settings import Config
from common.request_handler import RequestHandler
import os

# pytest_addoption — pytest 的固定钩子名，pytest 启动时会自动调用
# parser.addoption("--env", ...) — 注册一个 --env 参数，跟 argparse 一样的风格
# request — 内置 fixture，不需要 import。它的作用就是"读取当前这次 pytest 执行的上下文(即pytest执行的配置、执行的用例等等)"，其中一个功能就是 getoption 拿 CLI 参数值。
# request.config.getoption("--env") — 取出你传的值

def pytest_addoption(parser):
    """给 pytest 命令行加自定义/注册参数"""
    parser.addoption("--env",
                     action="store", # 把命令行后面跟的值，存进变量。命令行：pytest --env=prod，则pytest 自动把字符串"prod"存起来。后续下方函数去取env时，才能渠道对应值
                     default="test", # default:不传时的默认值
                     help = "环境：dev, test, prod")

@pytest.fixture(scope="session")
def env(request):
    """该fixture将钱面馆注册的env值取出来"""
    return  request.config.getoption("--env")  # requst是内置fixture，下面有一个getoption的功能，能拿到前面CLI的参数值



@pytest.fixture(scope="session")  # 如只写@pytest.fixture，则是默认的funtion级别
def github_api():
    handler = RequestHandler(Config.BASE_URL)
    yield handler
    handler.session.close()

@pytest.fixture(scope="session")  # 指整个会话中，只创建一次，其他时候都直接复用，以节省资源
def jsonplace_api():
    handler = RequestHandler(Config.JSONPLACE_URL)
    yield handler
    handler.session.close()  #Session 底层有 TCP 连接，长时间不关会占着连接。故在执行外用例后，回来把它关闭

@pytest.fixture(scope="session")
def recountries_api():
    handler = RequestHandler(Config.RESTCOUNTTIES_URL)
    yield handler
    handler.session.close()

@pytest.fixture(scope="session")
def github_api_token():
    token = os.environ.get("GITHUB_TOKEN")
    handler =  RequestHandler(Config.BASE_URL, token)
    yield handler
    handler.session.close()