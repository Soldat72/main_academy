import random
import math
a = random.sample(range(100, 200), 5)
f = random.uniform(2, 10)
m = max(a)
r = m // f
r1 = m % f
factor = math.factorial(int(r1))
print(a)
print('max element is: {0}'.format(m))
print('cлучайное число float', f)
print('целая часть от деления (integer part) //: {0},остаток от деления % : {1}'.format(r, r1))
print('факториал', factor)


