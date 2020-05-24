"""A program that repeats letters in a string,
@param: string
@output: titled string
"""

def accum(string):
    result = [(letter * index) for index, letter in enumerate(string, 1)]
    return '-'.join(result).title()
    
# single line code
def accum(string):
    return '-'.join([(letter * index) for index, letter in enumerate(string, 1)]).title()
    

print(accum('backend'))
print(accum('sca'))
print(accum('Ifenna'))