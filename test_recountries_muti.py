import json

import pytest


# 三种数据文件，都是"打开→解析→列表/字典"
# json.load(open("xxx.json"))
# yaml.safe_load(open("xxx.yaml"))
# csv.DictReader(open("xxx.csv"))

countries = json.load(open("data/countries.json"))

@pytest.mark.parametrize("country", countries)
def test_recoutires_muti(recountries_api,country):
    res = recountries_api.get(f"/v3.1/name/{country}")
    assert res.status_code == 200
    data = res.json()
    assert country in data[0]["name"]["common"]
    assert "capital" in data[0]
    assert "population" in data[0]
    assert "region" in data[0]