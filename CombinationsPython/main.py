from itertools import combinations

print("Please enter a number , and we will find different combinations to make that number: ")
number = input()
list = [1, 5, 3, 7, 9, 2, 3, 4, 3]

def findNumbers(list, sum):
    output = []
    for i in combinations(list, 2):
        if i[0] + i[1] == sum:
            output.append((i[0], i[1]))
    return output


print(findNumbers(list, number))