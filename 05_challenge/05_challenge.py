def fizzbuzz():
    three_mul = 'fizz'
    five_mul = 'buzz'

    with open('mifile.txt', 'r') as f:
        print('file loaded')

        num1 = int(f.readline().strip())
        num2 = int(f.readline().strip())
        max_num = int(f.readline().strip())

    for i in range(1, max_num):
        if i % num1 == 0 and i % num2 == 0:
            print(i, three_mul + five_mul)
        elif i % num1 == 0:
            print(i, three_mul)
        elif i % num2 == 0:
            print(i, five_mul)


if __name__ == '__main__':
    fizzbuzz()