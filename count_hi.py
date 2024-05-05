def double_char(str):
  doubled = ""
  for i in range(len(str)):
    s = str[i]
    doubled += s + s
  return doubled

