nums = [10, 20, 30, 40, 50]

print(nums[0])  # 10 (Indexing)
print(nums[-1])  # 50 (Last element)
nums.append(60)  # Add element
nums.remove(20)  # Remove element
nums.insert(1, 15)  # Insert at index 1
print(nums)  # [10, 15, 30, 40, 50, 60]
print(len(nums))  # 6 (Length)
print(30 in nums)  # True (Check existence)
nums.sort()  # Ascending
nums.reverse()  # Descending
new_list = nums + [70, 80]  # Concatenation

#Tuple
t = (1, 2, 3, 4, 5)

print(t[0])  # 1 (Indexing)
print(len(t))  # 5
print(t.count(2))  # 1 (Count occurrences)
print(t.index(3))  # 2 (Find index of 3)

#dictionary
student = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print(student["name"])  # Alice
student["age"] = 26  # Modify value
student["gender"] = "Female"  # Add new key-value
print(student.keys())  # dict_keys(['name', 'age', 'city', 'gender'])
print(student.values())  # dict_values(['Alice', 26, 'New York', 'Female'])
print(student.items())  # dict_items([('name', 'Alice'), ('age', 26), ('city', 'New York'), ('gender', 'Female')])

#set
s = {1, 2, 3, 4, 5, 5, 5}  # Duplicate 5 is removed
print(s)  # {1, 2, 3, 4, 5}

s.add(6)  # Add element
s.remove(3)  # Remove element
print(2 in s)  # True (Check if 2 is in set)

#set operation
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)  # Union: {1, 2, 3, 4, 5, 6}
print(A & B)  # Intersection: {3, 4}
print(A - B)  # Difference: {1, 2}
print(A ^ B)  # Symmetric Difference: {1, 2, 5, 6}
