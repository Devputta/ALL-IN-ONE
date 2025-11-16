#set is unique and immuatable it can't store dist and list it can store int,float,booliean,tuples,strings
#unoederd and it will ignore the duplicates
collection = {1,2,3,4,5,7,8,"ragi","ramya","rakshitha",1,3,4,7,8}
print(len(collection))
print(type(collection))
print(collection)
print(list(collection))


#creating empty sets
q = set()


q.remove
print(type(q))
print(q)

#methode add,remove,pop
q.add(1)
q.add("maha")
q.add(4)
q.add((1,3,5,7,8,9))

print(q)

q.remove(1)
print(q)

q.clear()
print(q)

print(collection.pop())
print(collection.pop())
print(collection)


#imp union 

set1 = {1,3,5,6}
set2 = {3,3,5,1,6}

print(set1.union(set2)) #unique
print(set1.intersection(set2)) #common

