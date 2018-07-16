def search_max_count(lst):
    max_count = 0
    max_v = None
    for element in lst:
        l_count = lst.count(element)
        if l_count > max_count:
            max_count = l_count
            max_v = element
    return max_v


if __name__ == '__main__':
    print("Max_often =>",
          search_max_count([int(strr)
                            for strr in input("Input l=> ").split()]))
