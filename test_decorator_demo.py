def my_logger(func):
    def wrapper():
        print("调用前…")
        func()
        print("调用后…")
    return wrapper


# @my_logger
def say_hello():
    print("Hello")

f = my_logger(say_hello)   # 等效于@my_logger。分解的话，f=wrapper ，没有括。意思是把wrapper赋给f，但不执行。
f()   # 这里等同于 wrapper()，才执行。实现装饰器+被装饰函数的功能。
