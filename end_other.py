def end_other(a, b):
  l = len(a)
  lb = len(b)
  if (a[-lb:].lower()) == (b[-l:].lower()):
    return True
  return False

