def inc():
    x = 10
    def fn():
        # 仅读取x的值:
        nonlocal x
        x = x + 1
        return x
    return fn

f = inc()
print(x)

ans = f()
print(ans)