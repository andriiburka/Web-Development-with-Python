def palindrome(string, index):
    if index >= len(string):
        if True:
            print(f"{string} is a palindrome")
        else:
            print(f"{string} is not a palindrome")
        return
    palindrome(string, index + 1)

    # ре_КУР_сивна задача, някво такова
