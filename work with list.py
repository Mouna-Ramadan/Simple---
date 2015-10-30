"""a=['spam','eggs',100,1234]

a[2]=a[2]+23
print(a)

a[1:1]=['A','B']
print(a)

a = [123,1234]
a[1:1]=['A','B']
 shift and insert without remove

print(a)

a = [123,1234]
a[1:2]=[10,20]
print(a)"""

Q = [2,3]
P = [1,Q,4]
print(P)

print(P[1][0])

Q.append(5)
print(P)

P[1].append(15)
print(P)

P[1].extend(['Extra'])
print(P)

P[1].append(['Extra'])
print(P)

P=P[1][-1]
print(P)



word = 'Help' + 'A'
print('<' + word*5 +'>')
st= ' s tr '.strip()+'ing'
print('<' + st*5 +'>')

print(word[2:4])
print(word[:2])
print(word[:2]+word[2:])
print('x'+word[1:])
print(word[1:100])
print(word[10:])
print(word[2:1])
print(word[-0])
print(word[-1:0])










