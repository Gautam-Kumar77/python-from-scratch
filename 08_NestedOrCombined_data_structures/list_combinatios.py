from django.urls import reverse  #List Combinations with list,tuple,set,dict

#1. list in list: POSSIBLE
lst= [23,45,"PYTHON", [2,5,1,9], 3.5]
print(lst)
print(lst[3])

for i in lst[3]:
    print(i)
for ie in lst:
    print(ie)

x= lst[3].append(10)
x2= lst[3].insert(2,20)
print(lst)

#2. tuple in list:
lst= [23,5,(3,4,2), "Hello", 8.0, True]
print(lst[2])
# p= lst[2]= 34
sl= lst[2][0:1]
print(sl)

s= tuple(sorted(lst[2], reverse = True))
print(s)

#3. set in list
lst= [10, "RS", {4,8,5}, {2,89,50}, True]
print(lst)
for i in lst[3]:
    print(i)

ls= lst[2].add(100)
ls1= lst[3].discard(89)
print(lst)

#4. dict in list
lst= [56,76,{"Course": "MCA", "Roll" :34}, 23]
print(lst, type(lst))

for k,v in lst[2].items():
    print(k,"-->", type(k), v, "-->", type(v), "-->",  type(lst))

print(lst[2], type(lst))

ld= lst[2]["Year"]= 2026
print(lst[2])

ld1=lst.insert(4, {7:23,3:54})
print(lst)
