l_str = [int(str) for str in input("Input l=> ").split()]
max_count = 0
max_v = None
for element in l_str:
    l_count = l_str.count(element)
    if l_count > max_count:
        max_count = l_count
        max_v = element
print("Max_often =>", max_v)
