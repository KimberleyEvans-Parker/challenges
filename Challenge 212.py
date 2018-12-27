def main():
    s = input("Enter the string: ")
    vowels = "aeiouyAEIOUY "
    s2 = ""
    for char in s:
        if char in vowels:
            s2 += char
        else:
            s2 += char + "o" + char.lower()
    print(s2)
    s3 = "".join(char if char in vowels else char +
                 "o" + char.lower() for char in s)
    print(s3)


main()
