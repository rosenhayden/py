
def dec_three():
    n = 100
    while n >= 0:
        print(n)
        n -= 3

def square(x):
    for i in range(len(x)):
        if (x[i] % 2 != 0):
            print(x[i] * x[i])
            ++i

def main():
    x = [1, 3, 54, 12, 4, 9]
    square(x)

if __name__ == "__main__":
    main()

        






