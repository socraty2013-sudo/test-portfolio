import os
import requests
import pytest


case_datas = [(False,60),(True,5000)]

@pytest.mark.parametrize("use_token,expected_min",case_datas)
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

