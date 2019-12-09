def f():
    for _ in range(4):
        yield _

g1 = f()
g2 = f()
print(sum(g1)+sum(g2))
