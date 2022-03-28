from collections import deque

# determines if parentheses (regular, hard bracket, curly brace) are matched
# is_matched: String -> Boolean
def is_matched(s):
  opening_chars = {"(", "[", "{"}
  closing_chars = {")", "]", "}"}
  level = 0
  stack = deque()
  for x in s:
    if x in opening_chars:
      level += 1
      stack.append(x)
    if x in closing_chars:
      stack_char = stack.pop()
      match x:
        case ')':
          if (stack_char != '('):
            return False
        case "}":
          if (stack_char != "{"):
            return False
        case "]":
          if (stack_char != "["):
            return False
        case _:
          return False
  return True

print(is_matched('()')) # expect True
print(is_matched('(}')) # expect False
print(is_matched('[({})()]')) # expect True
print(is_matched('([]{})')) # expect True
print(is_matched('({[)}]')) # expect False
print(is_matched('(]')) # expect False
