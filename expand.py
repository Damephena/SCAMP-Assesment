"""A program that returns number in expanded form.
@param: positive integer
@output: string
Example: ex(12)
returns "10 + 2"
"""
def expand(num):
    result = []
    for index, digit in enumerate(str(num)[::-1]):  # pair reversed list of parsed string(num)
        if int(digit) > 0:
            result.append(digit + ('0' * index))
    return ' + '.join(result[::-1])  # reorder string before join

print(expand(12))
print(expand(42))
print(expand(70304))
print(expand(1002001))