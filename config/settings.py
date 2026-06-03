import os

class Config:
    BASE_URL = "https://api.github.com"
    JSONPLACE_URL = "https://jsonplaceholder.typicode.com"

    CURRENT_ENV = os.environ.get("ENV", "test")  # 这一步是从全局环境数据中，通过 key：ENV查找对应值，默认情况下为 test（兜底）
    RESTCOUNTTIES_URL = {
        "dev" : "https://localhost:3000",
        "test": "https://restcountries.com",
        "prod": "https://restcountries.com",
    }[CURRENT_ENV]   # 这里相当于:(用dev举例) RESTCOUNTTIES_URL.["test"] = 从RESTCOUNTTIES_URL这个字典中获取对应环境的值（链接）
