import timeit

test_code = '''
A.__mul__(A)
'''
test_code2 = '''
A.qmul(A)
'''

setup = '''
from umatrix import matrix
order = 4
A = matrix(*([r * order + c for c in range(order)] for r in range(order)))
'''

if __name__ == "__main__":
    time = timeit.timeit(test_code, setup=setup, number=50000)
    print(time)
    time = timeit.timeit(test_code2, setup=setup, number=50000)
    print(time)
