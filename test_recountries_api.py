

def test_recountries(recountries_api,countryname = "china"):
    res = recountries_api.get(f"/v3.1/name/{countryname}")
    assert res.status_code == 200
    data = res.json() # data为列表
    assert "China" in data[0]["name"]["common"]
    assert "capital" in data[0]
    assert "population" in data[0]
    assert "region" in data[0]


