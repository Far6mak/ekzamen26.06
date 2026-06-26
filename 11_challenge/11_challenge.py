def fizzbuzz(max_num):
    for i in range(1, max_num + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(i, "fizzbuzz")
        elif i % 3 == 0:
            print(i, "fizz")
        elif i % 5 == 0:
            print(i, "buzz")


if __name__ == '__main__':
    fizzbuzz(100)