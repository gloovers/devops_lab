l_str = [int(str) for str in input("Input left and right values=> ").split()]
range_s = [str(i) for i in range(l_str[0], l_str[1] + 1)]
flag = 0
for element in range_s:
    if "0" not in element:
        for pos in range(len(element)):
            if int(element) % int(element[pos]) != 0:
                range_s[range_s.index(element)] = "N"
                break
    else:
        range_s[range_s.index(element)] = "N"

for element in range(range_s.count("N")):
    range_s.remove("N")
print(range_s)
