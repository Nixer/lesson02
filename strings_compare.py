def strings_compare(str1, str2):
    if isinstance(str1, str) and isinstance(str2, str):
        if str1 == str2:
            return 1
        elif str1 != str2:
            if len(str1) > len(str2):
                return 2
            elif str2 == "learn":
                return 3
            else:
                return "Cool!"
    else:
        return 0


print(strings_compare(0, 'abc'))
print(strings_compare('abc', 'abc'))
print(strings_compare('abcd', 'abc'))
print(strings_compare('abcd', 'learn'))
print(strings_compare('abcd', 'learnad'))

