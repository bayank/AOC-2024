
def read_list(file_name):
    list1 = []
    list2 = []
    with open(file_name, "r") as f:
        for line in f:
            num1, num2 = map(int, line.split())
            list1.append(num1)
            list2.append(num2)
    return list1, list2

if __name__ == "__main__":
    l, r = read_list("day1_input.txt")
    sorted_l=sorted(l)
    sorted_r=sorted(r)

    diffs = []
    for i in range(len(sorted_l)):
        diffs.append(abs(sorted_r[i] - sorted_l[i]))
    print(sum(diffs))