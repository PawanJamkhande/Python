

# data = [[[1,2],[3,4]],[[5,6],[7,8]]]
# def fun(m):
#     v = m[0][0]
#     for row in m:
#         for element in row:
#             if v < element: v = element
#     return v
# print(fun(data[0]))

# arr = [[1,2,3,4],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
# for i in range(0,4):
#     print(arr[i].pop())

# def f(i, values = []):
#     values.append(i)
#     print(values)
# f(1)
# f(2)
# f(3)


# arr = [1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1] = arr[i]
# for i in range(0,6):
#     print(arr[i], end = " ")

# fruit_list1 = ['Apple','Berry','Cherry','Papaya']
# fruit_list2 = fruit_list1 #list alising every elements in list 1 will be transmitted to 2 and if we change any element in list 1 or 2 it will be changed in other list too
# fruit_list3 = fruit_list1[:]
# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'

# sum = 0
# for ls in (fruit_list1,fruit_list2,fruit_list3):
#     if ls[0] == 'Guava':
#         sum+=1
#     if ls[1] == 'Kiwi':
#         sum+=20
# print(sum)


class CRUD:
    def __init__(self):
        print("Student Management System")
        self.studentId=[]
        self.studentRollno=[]
        self.studentName=[]
        self.studentCity=[]
    
    def addStudent(self):
        studentId = input("Enter Student ID: ")
        studentRollno = input("Enter Student Roll No: ")
        studentName = input("Enter Student Name: ")
        studentCity = input("Enter Student City: ")
        self.studentId.append(studentId)
        self.studentRollno.append(studentRollno)
        self.studentName.append(studentName)
        self.studentCity.append(studentCity)
        print("Student added successfully!")


obj = CRUD()
print(obj.addStudent)

   




