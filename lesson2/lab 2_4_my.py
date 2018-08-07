import string
a = list(string.ascii_letters + string.digits)
print (a)
print('Первый элемент :{0}\n последний єлемент :{1}\n третий :{2} \nтретий с конца: {3}'. format(a[0], a[-1], a[2], a[-3]))
print(a[:10])
print(a[::2])
print (".".join(a))
int_a = []
for i in a:
    try:
        int(i)
        int_a.append(int(i))
    except:
         pass
print(int_a)
print(int_a[::-1]) # реверсная печать
c = '-'.join(a)
print(c)