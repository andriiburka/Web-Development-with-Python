def palindrome(string, index):
    if index >= len(string):
        print(f"{string} is a palindrome")
        return
    palindrome(string, index + 1)

    s