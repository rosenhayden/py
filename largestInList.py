def find_largest(numbers):
    result = 1 
    for n in numbers:
        if n > result:
            result = n
    return result

def find_sum(numbers):
    result = 0 
    for n in numbers:
        result += n
    return result

def find_prod(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result

def make_dashed(s):
    result = ""
    for i in s:
        if i == " ":
            result += "-"
        else:
            result += i
    return result

def main():
    x = [6, 4, 3, 5, 7, 19]
    largest = find_largest(x)
    print(largest)
    sum = find_sum(x)
    print(sum)

    prod = find_prod(x)
    print(prod)
    print(make_dashed("I'm going to fart"))

if __name__ == "__main__":
    main() 
