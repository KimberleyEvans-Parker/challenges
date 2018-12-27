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


main()
