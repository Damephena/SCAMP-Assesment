def fib(number):
    count = 0
    if number <= 0:
        print('Please enter a positive integer.')
    elif number == 1:
        return 0
    elif number == 2:
        return
    else:
        return fib(number - 1) + fib(number - 2)

number = int(input('Enter a valid number: \n'))

print("Fibonacci value is: ", fib(number))
