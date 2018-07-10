l_str = [int(str) for str in input("Input X, Y, Z and N => ").split()]
print([[i, j, k]
       for i in range(l_str[0] + 1)
       for j in range(l_str[1] + 1)
       for k in range(l_str[2] + 1)
       if ((i + j + k) != l_str[3])])
