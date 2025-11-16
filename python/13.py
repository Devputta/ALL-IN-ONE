#list and tuples in python (apnacollege)
# in list string are not immuatable (which means can't change) it can be accable but values can't changeable
# in list list are muatable (which means it can be change) it can be done both
# in list slicing possiable

marks = [20.3, 25.34, 29.45, 67.48]
print(marks)
print(type(marks))

print(marks[3])
print(len(marks))

str = ["maha", 36 , "Arjun", 40]
print(len(str))
print(str)

str[0] = "jayaramji"
print(str)

# slicing

mark =[20,30,49,59,60,82,47]
print(mark[0:-1])

#list meathods 
#append (it will add value at end)
a = [20,30,40,50,60]
print(a)
a.append(20)
print(a)

#sort meathod
b = [6,3,9,4,6,2,7,4,0,2]
f = ["kiwi", "banana", "papaya", "apple"]
print(len(b))
print(len(f))
print(b)
print(f)

b.sort()
f.sort()
print(b)
print(f)

#reverse
b.sort(reverse=True)
f.sort(reverse=True)
print(b)
print(f)

#direct reverse 
b.reverse()
f.reverse()
print(b)
print(f)


#examples
s = ["d", "r", "g", "y", "u", "s", "a"]
print(s)
s.reverse()
print(s)

# insert method 
o = [1,4,6,2,5]
o.insert(5, 10)
print(o)

y = ["yamin", "jaya", "maha", "raju"]
print(y)
y.insert(4, "mahesh")
print(y)


#remove (it will remove the first occurence of 1st value) it takes value

p = [2 ,4 ,4 ,6 ,7, 0, 3, 6]
print(p)
p.remove(0)
print(p)

# another Method POP it takes index

p.pop(3)
print(p)

#TUPLES ( insted of [ 
t = (1, 3, 4, 6, 0, 1, 3)
print(type(t))

print(t[1])
print(t[0])

#slicing in tuples
print(t[0:2])
print(t[3:6])

#index it will show the index of the 1st occurence
print(t.index(6))
print(t.count(0))