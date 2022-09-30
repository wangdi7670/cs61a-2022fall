l = ['a',  'b', 'c', 'd']

for i in range(len(l)) :
    print(l[i])

for i, val in enumerate(l):
    print(i, val)

s = "ad"
print("ad" == s)


s = '.'
print(s.isalpha())

s = 'a \tc'
print(s.split())