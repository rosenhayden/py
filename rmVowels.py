def main():
    print(remove_caps("FOKKA:LSJFLKSA:JF"))

def remove_vowels(s):
    result = ""
    vowels = [ "a", "e", "i", "o", "u"]
    for c in s:
        
        if not c.lower() in vowels:
            result += c
    else:
        result += c


def make_lower(s):
    str = ""
    for i in range (len(s)):
        str += s[i].lower()
    return str

def remove_caps(s):
    result = ""
    for c in s:
        if not c.isupper():
            result += c
    return result
if __name__ == "__main__":
    main()
