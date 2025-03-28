#find the duplicate value in a list
def find_duplicate(lst):
    return [item for item in set(lst) if lst.count(item) > 1]

list = [1,1,2,3,4,5,5]
print(find_duplicate(list))  # Output: [1, 5]