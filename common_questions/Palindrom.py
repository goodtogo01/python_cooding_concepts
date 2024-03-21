
# Input string and check is it palindrom or not?
def strPal():
    s = str(input("Enter your word : "))
    rev = "".join(reversed(s))
    if (s == rev):
        print(f"[{s}] is a palindrome.")
    else:
        print(f"[{s}] is not a palindrome.")
    return rev

strPal()

# Input string and check is it palindrom or not?
def intPal():
    i = int(input("Enter your number : "))
    s = str(i)
    s = "".join(reversed(s))
    rev = int(s)
    if (i == rev):
        print(f"[{i}] is a palindrome.")
    else:
        print(f"[{i}] is not a palindrome.")
    return rev

intPal()