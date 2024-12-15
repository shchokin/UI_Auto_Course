def test_equal_2(generate_code):
    assert 1 == generate_code


def test_factorial():
    f = 1
    a = int(input("Enter number >"))
    for i in range(1, a + 1):
        f *= i
    print(f)


def test_fibonachi():
    f = [0, 1]
    a = int(input("Enter number >"))
    for i in range(2, a + 1):
        f.append(f[i-2] + f[i-1])
    print(f)
