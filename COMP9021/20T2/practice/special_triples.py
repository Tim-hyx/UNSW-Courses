# Finds all triples of consecutive positive three-digit integers
# each of which is the sum of two squares.


# Insert you code here
all_nums = []
for n in range(100, 998):
    for i in range(0, 31):
        for j in range(i, 32):
            if i ** 2 + j ** 2 == n:
                all_nums.append(n)
all_nums = sorted(set(all_nums))
target_nums = []
for n in range(len(all_nums) - 2):
    if all_nums[n] + 1 == all_nums[n + 1] and all_nums[n + 1] + 1 == all_nums[n + 2]:
        for i in range(0, 31):
            for j in range(i, 32):
                if i ** 2 + j ** 2 == all_nums[n]:
                    target_nums.append((all_nums[n], i, j))
        for i in range(0, 31):
            for j in range(i, 32):
                if i ** 2 + j ** 2 == all_nums[n] + 1:
                    target_nums.append((all_nums[n] + 1, i, j))
        for i in range(0, 31):
            for j in range(i, 32):
                if i ** 2 + j ** 2 == all_nums[n] + 2:
                    target_nums.append((all_nums[n] + 2, i, j))
first = target_nums[0]
delete_nums = []
for second in target_nums[1:]:
    if first[0] == second[0]:
        delete_nums.append(second)
    first = second
for i in delete_nums:
    target_nums.remove(i)
for i in range(0, len(target_nums), 3):
    print(
        f'({target_nums[i][0]}, {target_nums[i + 1][0]}, {target_nums[i + 2][0]}) (equal to ({target_nums[i][1]}^2+{target_nums[i][2]}^2, {target_nums[i + 1][1]}^2+{target_nums[i + 1][2]}^2, {target_nums[i + 2][1]}^2+{target_nums[i + 2][2]}^2)) is a solution.')

