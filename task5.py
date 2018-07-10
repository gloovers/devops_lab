keyboard_str = 'qwertyuiopasdfghjklzxcvbnm'
input_l = input("Type a letter => ")
index = keyboard_str.find(str(input_l))
if index == (len(keyboard_str) - 1):
    print("Output => ", keyboard_str[0])
else:
    print("Output => ", keyboard_str[index + 1])
