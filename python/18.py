#EMPTY DIST
dist = {}

dist["NAME"] = "JAVAN"
dist["age"] = 24

print(dist)

#nested dist

dist1 = {
    "name" : "maha",
    "age" : 24,
    "subject" : {
        "java" : 24,
        "c" : 35,
        "cn" : 35,
    }
}

print(dist1["subject"])
print(dist1)


#METHODS key it will only displays the keys

print(dist.keys())

#type costing dist to list

print(list(dist1.keys()))

#same like prev changing type dist to tuples

print(tuple(dist1.keys()))

print(len(dist1))


#method 2 values it only shows the values

print(dist1.values())

#method 2 items() it will showes the key and pair values 

print(dist1.items())

p = list(dist1.items())
print(p[0])

#method 4 get it will get the value of the given key

print(dist1.get("name"))
print(dist1.get("age"))
print(dist1.get("subject"))

#5 method update

new_d = {
    "place" : "maharaj",
}
print(dist1.update(new_d))
print(dist1)