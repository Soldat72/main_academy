import string
import random
a=string.ascii_letters
#b= random.sample(a,5)
print('первая буква:', a[0], 'последняяя буква:',a[-1])
print('первая третья:', a[2], 'последняяя третья:',a[-2])
print('первые 8:', a[0:8])
print('первые 9,10:', a[9:11])
print('8-10:', a[0:8]+a[9:11])
l=int(len(a)/2)
print (l)
print('середина', a[l])