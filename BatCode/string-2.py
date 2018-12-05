# Given a string, return a string where for every char in the original, there are two chars.

def double_char(str):
  new_str = ""
  for char in str:
    new_str += char*2
  return new_str

# Return the number of times that the string "hi" appears anywhere in the given string.
def count_hi(str):
    return str.count("hi")

# Return the number of times that the string "code" appears anywhere in the given string, 
# except we'll accept any letter for the 'd', so "cope" and "cooe" count.
def count_code(str):
  count = 0
  i=0
  while "co" in str[i:]:
    if len(str[i+str[i:].index("co"):]) >= 4 and str[i+3+str[i:].index("co")] == "e":
      count += 1
    i += str[i:].index("co")+3
  return count


# Given two strings, return True if either of the strings appears at the very end of the other string,
# ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
# Note: s.lower() returns the lowercase version of a string.
def end_other(a, b):
  long_s, short_s = (a,b) if len(a) >= len(b) else (b,a)
  return long_s.lower().endswith(short_s.lower())

# Return True if the string "cat" and "dog" appear the same number of times in the given string.
def cat_dog(str):
    return str.count("cat") == str.count("dog")


# Return True if the given string contains an appearance of "xyz" where the xyz is not directly 
# preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
def xyz_there(str):
    if str[:3] == "xyz":
        return True             
    for i in range(1, len(str) - 2):
        if str[i-1] != "." and str[i:i+3] == "xyz":
            return True                                 
    return False
