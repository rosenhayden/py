def main():
    print(merge_lists([1,2,3,4], ["a","b","c","d"]))
def merge_lists(a, b):
    mergedList = []
    for i in range(len(a)):
        mergedList.append(a[i])
        mergedList.append(b[i])
    return mergedList
if __name__ == "__main__":
    main()
