
def read_list(file_name):
    list1 = []
    list2 = []
    with open(file_name, "r") as f:
        for line in f:
            num1, num2 = map(int, line.split())
            list1.append(num1)
            list2.append(num2)
    return list1, list2

def day1_p1(filename):
    l, r = read_list(filename)
    sorted_l=sorted(l)
    sorted_r=sorted(r)

    diffs = []
    for i in range(len(sorted_l)):
        diffs.append(abs(sorted_r[i] - sorted_l[i]))
    return sum(diffs)

def day1_p2(filename):
    l, r = read_list(filename)

    similarity_score = []
    for i in range(len(l)):
        similarity_score.append(r.count(l[i])*l[i])
    return sum(similarity_score)

if __name__ == "__main__":
    print(f'Day 1 Part1 Answer: {day1_p1("day1_input.txt")}')
    print(f'Day 2 Part2 Answer: {day1_p2("day1_input.txt")}')