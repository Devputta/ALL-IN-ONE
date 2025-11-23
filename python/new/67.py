count = 0
total_even_num = 0
with open("num.txt", "r") as f:
    data = f.read()
    print(data)


new = data.split(",")
print(new)
for val in new:
    if(int(val) % 2 == 0):
        count += 1
        total_even_num += int(val)
print(count)
print(total_even_num)


