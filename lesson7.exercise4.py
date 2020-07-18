def sqr_but_not_thirteen(n):
    if n == 13:
        raise ValueError('number 13 is caught')
    elif not 1 <= n <= 100:
        raise ValueError('your number is out of [1-100]')
    else:
        return n ** 2


try:
    num = int(input("input number [1-100]: "))
    print(f'the square of {num} is {sqr_but_not_thirteen(num)}')
except ValueError as e:
    print(f'Error: {e}')
