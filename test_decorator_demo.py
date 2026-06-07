import functools
import time


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
# f()   # 这里等同于 wrapper()，才执行。实现装饰器+被装饰函数的功能。


# 重试装饰器
def retry(max):
    def decorator(func):
        @functools.wraps(func)  # 位置固定，格式固定，入参固定。自定义装饰器必写。作用：复刻原函数的元信息，伪装成原函数（__name__、__doc__、函数签名）。否则，都会输出为下一行的函数的信息。
        def wrapper(*args,**kwargs):  # 接收任意参数。*args：把多余的【位置参数】装进元组。**kwargs：把多余的【关键字参数】装进字典。
            for i in range(max):
                try:
                    return func(*args, **kwargs)  # 如不用 return，wrapper 吞掉了返回值
                except Exception:   # Exception：通用异常基类，捕获大部分常规报错（索引、值、类型错误等）。
                                    # 常见的错误类型有：ValueError、TypeError、IndexError、KeyError等
                    if i == max -1:
                        raise   # 不做固定报错内容，上一行报什么错，这里就输出什么错
        return wrapper
    return decorator


@retry(max=3)
def unreliable():
    print("尝试中……")
    raise ValueError("又失败了")




fail_count = 0  # 函数外部的变量


@retry(max=3)
def flaky_but_ok():
    global fail_count   # Python规则：函数内部【读】外部变量不需要声明，【改】外部变量必须声明 global
    fail_count += 1
    print(f"第{fail_count}次尝试……")
    if fail_count <3:
        raise ValueError("还没好")   # 是抛出异常对象，不是 print。@retry 里，前两次失败进 except 后走了 if 判断——不是最后一次，所以既不 print 也不 raise，异常就被吞了，循环继续。
    return "成功了"



# 下面两个函数同属调用时，会出现：unreliable() 第三次失败后 raise，异常没人抓，程序直接终止。第 48 行永远不会执行
# unreliable()          ← 这里抛异常，程序死了
# flaky_but_ok()        ← 永远到不了

# 故需要把第一个示例的调用更改一下，就可以同时调用两个函数了：
# try:
#     unreliable()
# except ValueError:
#     pass              # 抓住异常，接着往下走


# unreliable()  # 需要改成下方63～66行的调用方式，则两个函数均生效
# flaky_but_ok()

# print(unreliable.__name__)
# print(flaky_but_ok.__name__)




# ——————————————————————————————————————————————————————-

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)   # 存下原函数的返回值result
        elapsed = time.time() - start
        print (f"{func.__name__} 执行耗时为：{elapsed:.2f}秒")
        return result  # 把值交给调用方（给代码用），可能要用到
    return wrapper

@timer
def test_timer_demo():
    time.sleep(1)
    return "done"

test_timer_demo()



# ------------------

def logger(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        print(f"调用函数：{func.__name__}({args} {kwargs}) -> 返回：{result}")
        return result
    return wrapper

@logger
def add (a,b):
    return a + b

add(1,2)