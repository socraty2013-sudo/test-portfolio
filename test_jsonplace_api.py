
def test_jsonplace_post(jsonplace_api):
    body = {"title":"测试标题","body":"测试内容","userId":1}
    res = jsonplace_api.post(path= "/posts", body= body) 
    assert res.status_code == 201
    data = res.json()
    assert "id" in data
    
    
def test_jsonplace_put(jsonplace_api):
    body = {"title":"PUT-测试标题","body":"PUT-测试内容","userId":1}
    res = jsonplace_api.put(path = "/posts/1", body =body)
    assert res.status_code == 200
    data = res.json()
    assert data["title"] == body["title"]


def test_jsonplace_del(jsonplace_api):
    res =jsonplace_api.delete(path="/posts/1")
    assert res.status_code == 200