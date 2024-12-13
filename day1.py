
def read_list(file_name):
    list1 = []
    list2 = []
    with open(file_name, "r") as f:
        for line in f:
            num1, num2 = map(int, line.split())
            list1.append(num1)
            list2.append(num2)
    return list1, list2

def day1(filename):
    l, r = read_list(filename)
    sorted_l=sorted(l)
    sorted_r=sorted(r)

    diffs = []
    for i in range(len(sorted_l)):
        diffs.append(abs(sorted_r[i] - sorted_l[i]))
    return sum(diffs)

if __name__ == "__main__":
    print(f'Day 1 Answer: {day1("day1_input.txt")}')