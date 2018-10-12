list1=[11,11,11,1,1,2,3,8,0]
print (list1)
s=list(set(list1))
print(s)

str="abcdefghijk"
st=set(str)
print(st)


s={1,2,3}
t={5}
s.update(t)
print (s)


s.add(8)
print(s)

s.remove(5)
print(s)


s.discard(2)
print(s)


s.add(9)
s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)

t={99,52}
s={1,2,3,4,8,9,6,7,6,9}
print(5 in s)
print(s.issubset(t))
print(s.issuperset(t))


q=s.union(t)
print(q)


print(s.intersection(t))


print(t.difference(s))
s={1,2,3,4,5,6,7}
t={5,6,7,8,9,10}
print(s.symmetric_difference(t))













