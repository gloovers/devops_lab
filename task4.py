n = int(input("Input n=> "))
if (1 >= n or n >= 10**5):
    print("The value of 'n' has been exceeded.")
    exit(1)
l_str = []
l_t = []
count = []
c_lenght = 0
for i in range(n):
    str_v = input()
    c_lenght += len(str_v)
    if c_lenght > 10**6:
        print("The sum of the lengths of all the words has been exceeded.")
        exit(1)
    if str_v.islower():
        l_str.append(str_v)
    else:
        print("Incorrect input. Program has been closed with error.")
        exit(1)
for stroka in l_str:
    if stroka not in l_t:
        l_t.append(stroka)
        count.append(l_str.count(stroka))
print(count)
