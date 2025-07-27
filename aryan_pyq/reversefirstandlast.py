def change_string(str1):
    new_str = str1[-1:] + str1[1:-1] + str1[:1]
    print("New string:", new_str)
    return new_str
