def validate(password_input):
    is_enough_chars = False
    is_in_valid_chars_list = True
    is_enough_digits = False

    valid_chars_list = []
    [valid_chars_list.append(chr(num)) for num in range(ord('0'), ord(':'), 1)]
    [valid_chars_list.append(chr(upper_letter)) for upper_letter in range(ord('A'), ord('['), 1)]
    [valid_chars_list.append(chr(lower_letter)) for lower_letter in range(ord('a'), ord('{'), 1)]

    # 1 - Check length
    if not 6 <= len(password_input) <= 10:
        print('Password must be between 6 and 10 characters')
    else:
        is_enough_chars = True

    # 2 - Check if character is number ot letter
    for character in password_input:
        if character not in valid_chars_list:
            is_in_valid_chars_list = False
            break

    if not is_in_valid_chars_list:
        print('Password must consist only of letters and digits')

    # 3 - Check if digits are 2 at least
    digits_count = 0
    for character in password_input:
        if character.isdigit():
            digits_count += 1

    if digits_count >= 2:
        is_enough_digits = True
    else:
        print('Password must have at least 2 digits')

    if is_enough_chars and is_in_valid_chars_list and is_enough_digits:
        print('Password is valid')


# start program
password = input()
validate(password)
