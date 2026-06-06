import jsonschema  # jsonschema:第三方库，与定义好的"结构规则"去比对 JSON 数据，不符合就报错
import pytest

@pytest.mark.xfail
def test_jsonplace_chain(jsonplace_api):
    body = {"title": "foo", "body": "bar", "userId": 1}
    res = jsonplace_api.post(path="/posts", body=body)
    data = res.json()
    id = data["id"]

    res_check = jsonplace_api.get(path=f"/posts/{id}")
    data_check = res_check.json()

    assert data_check["title"] == "foo"
    assert data_check["body"] == "bar"

def test_res_schema(jsonplace_api):
    res = jsonplace_api.get("/posts/1")
    data = res.json()

    # 先定义期望的数据结构
    schema = {
        "type": "object",  # 就是上方的 data的数据结构必须是个对象，也就是最外层是 {}的
        "properties": {  # 里面有哪些字段,对应的数据类型
            "id": {"type": "integer"},  # id → 必须是整数
            "title": {"type": "string"},  # title → 必须是字符串
            "body": {"type": "string"},  # body → 必须是字符串
            "userId": {"type": "integer"},  # userId → 必须是整数
        },
        "required": ["id", "title", "body", "userId"]  # 这四个字段缺一不可
    }

    jsonschema.validate(data, schema)  # validate:结构。