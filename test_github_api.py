import pytest
from common.logger import logger

@pytest.mark.smoke
@pytest.mark.parametrize("username", ["octocat","torvalds","gaearon"])
def test_github_user(github_api,username):
    logger.info("开始查询用户：%s", username)
    res = github_api.get(f"/users/{username}")
    logger.info("状态码: %d", res.status_code)
    assert res.status_code == 200
    data = res.json()
    assert data["login"] == username
    logger.info("用户 %s 验证通过", username)

@pytest.mark.regression
def test_github_user_repos(github_api, username = "octocat"):
    res = github_api.get(f"/users/{username}/repos")
    assert res.status_code == 200
    data = res.json()
    assert isinstance(data,list)
    assert len(data)>0

    first_repo = data[0]
    assert "name" in first_repo
    assert "id" in first_repo
    assert "full_name" in first_repo

@pytest.mark.smoke
def test_github_not_found_user(github_api, username = "this-user-does-not-exist"):
    res = github_api.get(f"/users/{username}")
    assert res.status_code == 404
    if res.status_code >=400:
        logger.error("GET %s → %d (失败)", username ,res.status_code)
    else:
        logger.info("GET %s → %d", username ,res.status_code)

def test_github_api_token(github_api_token):
    res = github_api_token.get("/user")
    data =res.json()
    assert data["login"] == "socraty2013-sudo"
