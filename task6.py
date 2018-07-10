base_27 = ["0", "1", "2", "3", "4", "5", "6", "7", "8",
           "9", "A", "B", "C", "D", "E", "F", "G", "H",
           "I", "J", "K", "L", "M", "N", "O", "P", "Q"]

alpha_27 = ["a", "b", "c", "d", "e", "f", "g", "h",
            "i", "j", "k", "l", "m", "n", "o", "p", "q",
            "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

output_str = []
input_str = list(input("Input encrypted word => "))
i = 0

for element in input_str:
    i += 1
    index_n = base_27.index(element)
    index_d = (abs(index_n - i) % 27)
    output_str.append(alpha_27[index_d - 1])

print("Output word => ", ''.join([s for s in output_str]))
