import string
import random
a=string.ascii_letters+string.digits
b= random.sample(a,9)
print('первая буква:', a[0], 'последняяя буква:',a[-1])
print('первая третья:', a[2],'\n' 'последняяя третья:',a[-2])
print('первые 8:', a[0:8])
print('первые 9,10:', a[9:11])
print('8-10:', a[0:8]+a[9:11])
l=int(len(a)/2)
print (l)
print('середина списка:', a[l])
print(b)
print('Каждая третья из спискаэ:', b[::3])
print('Весь список', a[:])
print('Реверс списка', a[::-1])
