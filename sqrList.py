def main():
    print(square_list([1,3,4,5,19]))
def square_list(x):
    result = []
    for i in range(len(x)):
        result.append(x[i] * x[i])
    return result

if __name__ == "__main__":
    main()
