# 测试作用域

def foo():
    for i in range(3):
        sum = i
        if i == 2:
            x = 222

    print(i)
    print(222)

foo()