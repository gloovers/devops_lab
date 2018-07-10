n = int(input("Input n=> "))
if (1 >= n or n >= 10**5):
    print("The value of 'n' has been exceeded.")
    exit(1)
l_str = []
l_t = []
count = []
c_lenght = 0
for i in range(n):
    str = input()
    c_lenght += len(str)
    if c_lenght > 10**6:
        print("The sum of the lengths of all the words has been exceeded.")
        exit(1)
    if str.islower():
        l_str.append(str)
    else:
        print("Incorrect input. Program has been closed with error.")
        exit(1)
for str in l_str:
    if str not in l_t:
        l_t.append(str)
        count.append(l_str.count(str))
print(count)
