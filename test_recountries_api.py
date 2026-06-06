

def test_recountries(recountries_api,countryname = "china"):
    res = recountries_api.get(f"/v3.1/name/{countryname}")
    assert res.status_code == 200
    data = res.json() # data为列表
    assert "China" in data[0]["name"]["common"]
    assert "capital" in data[0]
    assert "population" in data[0]
    assert "region" in data[0]


def test_check_env(env):
    """测试自定义cli参数env"""
    print(f"当前环境是：{env}")
    assert env in ("dev","test","prod")

#⬆️该测试用例执行：
# 测试执行：pytest --env=prod test_recountries_api.py::test_check_env    ————通过--env自行设置环境为dev、test。不传则默认为test
# 终端输出：test_recountries_api.py::test_check_env 当前环境是：prod    PASSED