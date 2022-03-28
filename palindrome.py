# determines if an integer is palindromic via recursion
def is_palindrome(x):
  x = str(x)
  if len(x) <= 1:
    return True
  if int(x) < 0:
    return False
  else:
    first = x[0:1]
    last = x[-1] # horrid performance
    rest = x[1:]
    if first not in rest:
      return False
    else:
      return (first is last) and is_palindrome(x[1:-1])
