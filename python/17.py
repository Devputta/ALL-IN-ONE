#distionary No order in it Muatable it is unsorted it does't have any index and also not allowed duplicate keys

info = {
    "name" : "mohil",
    "age" : 20,
    "class" : "B.E",
    "subject" : ["C", "Python", "SN"],
    "Marks" : (20,30,40,50)
}

print(info)
print(type(info))

info["name"] = "Mahakal"
print(info)

print(info["name"])
print(info["subject"])
print(info["class"])

info["surname"] = "jai"   #its just works like a append in list
print(info)