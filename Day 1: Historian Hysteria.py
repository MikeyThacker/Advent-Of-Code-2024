def get_lists():
    list1 = []
    list2 = []

    with open("Day1Nums.txt", "r") as f:
        while True:
            current_nums = f.readline()
            if current_nums == "":
                break

            list1.append(int(current_nums[0:5]))
            list2.append(int(current_nums[8:]))
    return sorted(list1), sorted(list2)


def main():
    list1, list2 = get_lists()

    total_diff = 0
    for i in range(len(list1)):
        total_diff += abs(list1[i] - list2[i])

    print(total_diff)


main()
