
def max_element(lst):

    return max(lst)

# 2. Remove Duplicates from a List
def remove_duplicates(lst):
    return list(set(lst))

# 3. Reverse a List
def reverse_list(lst):
    return lst[::-1]

# 4. Check for Palindromic List
def is_palindrome(lst):
    return "Palindrome" if lst == lst[::-1] else "Not Palindrome"

# 5. Find Common Elements in Two Lists
def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

# 6. Merge Two Sorted Lists
def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)

# 7. Calculate the Sum of List Elements
def sum_elements(lst):
    return sum(lst)

# 8. Count Occurrences of an Element in a List
def count_occurrences(lst, x):
    return lst.count(x)

# 9. Find the Second Largest Element in a List
def second_largest(lst):
    unique_elements = sorted(set(lst))
    return unique_elements[-2] if len(unique_elements) > 1 else None

# 10. Generate a List of Prime Numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers(n):
    return [i for i in range(2, n + 1) if is_prime(i)]

# 11. Add an Element at the Beginning of a List
def add_at_start(lst, x):
    return [x] + lst

# 12. Remove an Element from a List by Value
def remove_element(lst, x):
    return [i for i in lst if i != x]

# 13. Find the Third Largest Element in a List
def third_largest(lst):
    unique_elements = sorted(set(lst))
    return unique_elements[-3] if len(unique_elements) > 2 else None

# 14. Count Negative and Positive Numbers in a List
def count_pos_neg(lst):
    pos = sum(1 for x in lst if x > 0)
    neg = sum(1 for x in lst if x < 0)
    return pos, neg

# 15. Find the Kth Smallest Element in a List
def kth_smallest(lst, k):
    sorted_list = sorted(lst)
    return sorted_list[k - 1] if k <= len(sorted_list) else None

# 16. Remove All Occurrences of an Element in a List
def remove_all_occurrences(lst, x):
    return [i for i in lst if i != x]

# 17. Calculate the Product of List Elements
def product_elements(lst):
    result = 1
    for num in lst:
        result *= num
    return result

# 18. Find the First Non-Repeating Element in a List
def first_non_repeating(lst):
    for x in lst:
        if lst.count(x) == 1:
            return x
    return None

# 19. Split a List into Chunks of a Given Size
def split_list(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]

# 20. Find the Union of Two Lists
def union_lists(lst1, lst2):
    return list(set(lst1) | set(lst2))

# 21. Check if List is Sorted in Non-Decreasing Order
def is_sorted(lst):
    return "Sorted" if lst == sorted(lst) else "Not Sorted"

# 22. Remove Leading Zeros from a List of Integers
def remove_leading_zeros(lst):
    for i, x in enumerate(lst):
        if x != 0:
            return lst[i:]
    return []

# 23. Find the Largest Subarray with Contiguous Elements
def largest_contiguous_subarray(lst):
    max_subarray = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            subarray = lst[i:j]
            if sorted(subarray) == list(range(min(subarray), max(subarray) + 1)):
                if len(subarray) > len(max_subarray):
                    max_subarray = subarray
    return max_subarray

# 24. Find the First Missing Positive Integer
def first_missing_positive(lst):
    nums = set(lst)
    for i in range(1, max(lst + [0]) + 2):
        if i not in nums:
            return i

# 25. Find the Smallest Missing Positive Integer
def smallest_missing_positive(lst):
    nums = set(lst)
    for i in range(1, max(lst) + 2):
        if i not in nums:
            return i

# 26. Find the Longest Subarray with Equal 0s and 1s
def longest_equal_01_subarray(lst):
    max_subarray = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            subarray = lst[i:j]
            if subarray.count(0) == subarray.count(1):
                if len(subarray) > len(max_subarray):
                    max_subarray = subarray
    return max_subarray

# 27. Merge Overlapping Intervals
def merge_intervals(intervals):
    intervals.sort()
    merged = []
    for i in intervals:
        if not merged or merged[-1][1] < i[0]:
            merged.append(i)
        else:
            merged[-1][1] = max(merged[-1][1], i[1])
    return merged

# 28. Rearrange Elements in Zigzag Order
def zigzag_order(lst):
    lst.sort()
    for i in range(1, len(lst) - 1, 2):
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst

# 29. Find the Maximum Subarray Sum
def max_subarray_sum(lst):
    max_sum = float('-inf')
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            max_sum = max(max_sum, sum(lst[i:j + 1]))
    return max_sum

# 30. Find All Duplicates in a List
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for x in lst:
        if x in seen:
            duplicates.add(x)
        seen.add(x)
    return list(duplicates)


#### WITH GIVEN INPUTS #####
# Example Input
my_list = [3, 8, 1, 10, 5]
#OR user_list = list(map(int, input("Enter numbers separated by space: ").split()))


# Call Functions
print("Max Element:", max_element(my_list))                 # Output: 10
print("Remove Duplicates:", remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]
print("Reversed List:", reverse_list(my_list))              # Output: [5, 10, 1, 8, 3]
print("Is Palindrome:", is_palindrome([1, 2, 3, 2, 1]))     # Output: Palindrome
print("Common Elements:", common_elements([1, 2, 3], [3, 4, 5]))  # Output: [3]
print("Merged Sorted Lists:", merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]
print("Sum of Elements:", sum_elements(my_list))            # Output: 27
print("Count Occurrences of 2:", count_occurrences([1, 2, 2, 3, 2, 4], 2))  # Output: 3
print("Second Largest Element:", second_largest(my_list))   # Output: 8
print("List of Prime Numbers:", prime_numbers(20))          # Output: [2, 3, 5, 7, 11, 13, 17, 19]
print("Add at Start:", add_at_start(my_list, 0))            # Output: [0, 3, 8, 1, 10, 5]
print("Remove Element:", remove_element(my_list, 3))        # Output: [8, 1, 10, 5]
print("Third Largest Element:", third_largest(my_list))     # Output: 5
print("Count Positives and Negatives:", count_pos_neg([-1, -2, 3, 4, 5]))  # Output: (3, 2)
print("Kth Smallest (K=3):", kth_smallest(my_list, 3))      # Output: 5
print("Remove All Occurrences:", remove_all_occurrences([1, 2, 2, 3, 4, 2], 2))  # Output: [1, 3, 4]
print("Product of Elements:", product_elements([2, 3, 4]))  # Output: 24
print("First Non-Repeating Element:", first_non_repeating([1, 2, 3, 2, 1, 4, 5]))  # Output: 3
print("Split List in Chunks:", split_list([1, 2, 3, 4, 5, 6, 7, 8], 3))  # Output: [[1, 2, 3], [4, 5, 6], [7, 8]]
print("Union of Two Lists:", union_lists([1, 2, 3], [3, 4, 5]))  # Output: [1, 2, 3, 4, 5]
print("Is Sorted:", is_sorted([1, 2, 3, 3, 4, 5]))          # Output: Sorted
print("Remove Leading Zeros:", remove_leading_zeros([0, 0, 1, 2, 3, 0, 4]))  # Output: [1, 2, 3, 0, 4]
print("Largest Contiguous Subarray:", largest_contiguous_subarray([1, 2, 3, 4, 6, 7, 8, 9, 10]))  # Output: [1, 2, 3, 4]
print("First Missing Positive Integer:", first_missing_positive([3, 4, -1, 1]))  # Output: 2
print("Smallest Missing Positive Integer:", smallest_missing_positive([7, 8, 9, 11, 12]))  # Output: 1
print("Longest 0s and 1s Subarray:", longest_equal_01_subarray([0, 1, 0, 0, 1, 1, 0]))  # Output: [0, 1, 0, 0, 1, 1]
print("Merged Intervals:", merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))  # Output: [[1, 6], [8, 10], [15, 18]]
print("Zigzag Order:", zigzag_order([4, 3, 7, 8, 6, 2, 1]))  # Output: [3, 7, 4, 8, 2, 6, 1]
print("Max Subarray Sum:", max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6
print("Find Duplicates:", find_duplicates([4, 3, 2, 7, 8, 2, 1, 5, 5]))  # Output: [2, 5]

f=open("test.txt","w")
print("name of file",f.name)
print("File mode",f.mode)
print("readable",f.readable())
print("Writeable",f.writable())
print("File is close",f.closed)
f.close()
print("File is close",f.closed)

WRITE OPERATION-Overwrites previous data

f=open("test.txt","w")
f.write("\n Dubai is a smart city")
f.close()
print("File operation is done")


APPEND OPERATION - DOES NOT OVERWRITE PREVIOIUS Data

f=open("test.txt","a")
f.write("\n Dubai is a smart city")
f.close()
print("File operation is done")

Append a list

f=open("covid.txt","a")
my_list=["apple ","mango ","cherry "]
names={"sharmeen":"khan","Shri":"mane","mandar":"mawale"}
tup=('hey','there')
f.writelines(my_list)
f.writelines(names)
f.writelines(tup)
print("List is inserted")
f.close()

READING DATA FROM FILE

f=open("covid.txt","r")
print(f.read())
f.close()



WITH STATEMENT-CLOSES THE FILE AUTOMATICALLY

with open("test.txt","w") as f:
    f.write("Amit\n")
    f.write("Ashsish\n")
    print("File is close",f.closed)
print("File is close",f.closed)


Image Handling

f1=open("anki.png","rb")
f2=open("rossom.png","wb")
data=f1.read()
f2.write(data)
print("New image is available with the name: ",f2.name)


Operation with CSV file

import csv

f=open("sudent.csv","a",newline="")
a=csv.writer(f)
a.writerow(["StudentId","ROll no","Name","Mobile No"])
num=int(input("Enter number of records: "))
for i in range(num):
    stu=int(input("Enter your id: "))
    roll=int(input("Enter your roll no: "))
    name=input("Enter your name: ")
    mobile=int(input("Enter your phone number: "))
    a.writerow([stu,roll,name,mobile])
f.close()

#TASK => Coloumn name: SID,studentname,studentbranch,p1,p2,p3,p4,p5,total,pervcentange,grade,result
accept => SID,studentname,studentbranch,p1,p2,p3,p4,p5
calculate => total,percentage,grade,result


import csv

def calculate_results(p1, p2, p3, p4, p5):
    total = p1 + p2 + p3 + p4 + p5
    percentage = (total / 500) * 100
    
    if percentage >= 90:
        grade = 'A'
        result = 'Pass'
    elif percentage >= 80:
        grade = 'B'
        result = 'Pass'
    elif percentage >= 70:
        grade = 'C'
        result = 'Pass'
    elif percentage >= 60:
        grade = 'D'
        result = 'Pass'
    elif percentage >= 50:
        grade = 'E'
        result = 'Pass'
    else:
        grade = 'F'
        result = 'Fail'
    
    return total, percentage, grade, result

def save_to_csv(filename, student_data):
    header = ["sid", "studentname", "studentbranch", "p1", "p2", "p3", "p4", "p5", "total", "percentage", "grade", "result"]
    
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        file.seek(0, 2)  # Move cursor to the end of file
        if file.tell() == 0:
            writer.writerow(header)  # Write header only if file is empty
        writer.writerow(student_data)

def main():
    sid = input("Enter Student ID: ")
    studentname = input("Enter Student Name: ")
    studentbranch = input("Enter Student Branch: ")
    p1 = int(input("Enter marks for P1: "))
    p2 = int(input("Enter marks for P2: "))
    p3 = int(input("Enter marks for P3: "))
    p4 = int(input("Enter marks for P4: "))
    p5 = int(input("Enter marks for P5: "))
    
    total, percentage, grade, result = calculate_results(p1, p2, p3, p4, p5)
    student_data = [sid, studentname, studentbranch, p1, p2, p3, p4, p5, total, percentage, grade, result]
    
    save_to_csv("student.csv", student_data)
    print("Student record saved successfully!")
    
if __name__ == "__main__":
    main()

##Prints where the space comes 
name = 'abcdfjgerjab cdfijger'
def stringvarify(name):
    for i in range(len(name)):
        if name[i] == ' ':
            return name[i-1]
#name = input ('')
result = stringvarify(name)
if result:
    print(result)
else:
    print('NA')
