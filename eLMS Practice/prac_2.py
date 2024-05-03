def _make_gen():
    for x in range(100):
        yield x**2
gen = _make_gen()


for i in gen:
    print(i)