import os
import requests
import pytest


case_datas = [(False,60),(True,5000)]

# ids，是给参数的命名，一一对应。方便终端输出的打印查看。
@pytest.mark.parametrize("use_token,expected_min",case_datas,ids=["无token", "有token"])
def test_session_demo(use_token,expected_min):
    s = requests.Session()
    if use_token:
        token = os.environ["GITHUB_TOKEN"]
        s.headers.update({"Authorization": f"token {token}"})

    res = s.get("https://api.github.com/rate_limit")
    data = res.json()
    assert data["rate"]["limit"] == expected_min

def test_session_persistence():
    token = os.environ["GITHUB_TOKEN"]
    s2 = requests.Session()
    s2.headers.update({"Authorization": f"token {token}"})

    # 下方两个接口请求均自动在 header 带上上述的token，体现了"登录一次，全局生效"
    res1 = s2.get("https://api.github.com/rate_limit")
    assert res1.status_code == 200

    res2 = s2.get("https://api.github.com/user")
    assert res2.status_code ==200

@pytest.mark.skip   # 直接跳过，无理由
def test_skip_demo():
    assert 1 == 2  # 这行永远不会执行

@pytest.mark.skipif("GIT_TOKEN" not in os.environ, reason="没配置token时，则不执行")
def test_skipif_demo():
    assert True
