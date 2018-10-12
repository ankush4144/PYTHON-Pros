dict={'1990':8,'1991':18,'1992':5,'1993':6,'1994':8,'1995':7,'1996':9,'1997':11,'1998':13,'1999':19,'2000':21,'2001':18}

for key in dict:
    print (key)

print(dict.keys())

for key in dict:
    print(key,dict[key],end='\t')

del dict["1990"]
print (dict)

del dict
print (dict)

dict1={'1990':8,'1991':18,'1992':5,'1993':6,'1994':8,'1995':7,'1996':9,'1997':11,'1998':13,'1999':19,'2000':21,'2001':18}

dict1.pop("1999")
print(dict1)

n=len(dict1)
print(n)

dict2=dict1.copy()
print(dict2)

print(str(dict1))

print(dict1.get('2002'))
print(dict1.get('1992'))

print(dict1.items())

print(dict1.keys())

dict1.update(dict2)
print (dict1)

print(dict1.values())

print("1996" in dict1)
