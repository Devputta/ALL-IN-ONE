names = ["JAYA", "VARMA", "LAKSHI", "RAMJI", "AMAL"]

def p_list(list, ind = 0):
    if(ind == len(list)):
        return
    print(list[ind])
    p_list(list, ind+1)

p_list(names)