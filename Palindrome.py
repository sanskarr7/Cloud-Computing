# Check if a string is a palindrome
def is_palindrome(string):
    return string == string[::-1]

user_input = input("Enter a string: ").lower()
if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome!')
else:
    print(f'"{user_input}" is not a palindrome.')
