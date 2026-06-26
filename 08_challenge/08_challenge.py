class FizzBuzz:
    "Class to implement FizzBuzz for multiples of 3 and 5"

    def fizzbuzz(self, max_num):
        three_mul = 'fizz'
        five_mul = 'buzz'
        num1 = 3
        num2 = 5 

        for i in range(1, max_num + 1):
            if i % num1 == 0 and i % num2 == 0:
                print(i, three_mul + five_mul)
            elif i % num1 == 0:
                print(i, three_mul)
            elif i % num2 == 0:
                print(i, five_mul)


if __name__ == '__main__':
    fizzbuzz_obj = FizzBuzz()
    fizzbuzz_obj.fizzbuzz(100)