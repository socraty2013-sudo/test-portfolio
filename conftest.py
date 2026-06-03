import pytest
import os

from config.settings import Config
from common.request_handler import RequestHandler
import os

@pytest.fixture
def github_api():
    return RequestHandler(Config.BASE_URL)

@pytest.fixture
def jsonplace_api():
    return RequestHandler(Config.JSONPLACE_URL)

@pytest.fixture
def recountries_api():
    return RequestHandler(Config.RESTCOUNTTIES_URL)

@pytest.fixture
def github_api_token():
    token = os.environ.get("GITHUB_TOKEN")
    return RequestHandler(Config.BASE_URL, token)



# 一些 allure 相关的命令，和上方的文件无关。仅找个地方记录，以防后面忘记了，可以回来看一眼。

# #1.安装python包
# pip install allure-pytest
# #2.安装allure客户端（windows：scoop/choco 或官网下 zip 配置环境变量）
# brew install allure
# #3.执行用例生成json
# pytest ./test_xxx.py --alluredir=reports/allure   （pytest -v --alluredir=reports/allure-results）
# #4.生成并打开html
# allure generate reports -o allure-report --clean && allure open allure-report
#allure serve reports/allure-results