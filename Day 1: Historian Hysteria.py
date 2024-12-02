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


def part1():
    list1, list2 = get_lists()

    total_diff = 0
    for i in range(len(list1)):
        total_diff += abs(list1[i] - list2[i])

    print(f"Part 1: {total_diff}")

def part2():
    list1, list2 = get_lists()

    similarity_score = 0

    for num in list1:
        similarity_score += num * list2.count(num)

    print(f"Part 2: {similarity_score}")

part1()
part2()
