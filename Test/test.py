a = {
    range(1, 5): range(10, 15),
    range(11, 16): range(21, 26)
}

for key in a.keys():
    x = 3
    if x in key:
        print("x")
        idx = key.index(x)
        print("yay ", a[key])
