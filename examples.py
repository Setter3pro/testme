# class Complex:

#     def __init__(self,r=0,img=0):
#         self.real = r
#         self.img = img

#     def __str__(self):
#         sign = '+'
#         if self.img < 0:
#             sign = '-'
#         if self.img == 0:
#             return f'{self.real}'   
#         return f'{self.real} {sign} {abs(self.img)}i'

#     def __add__(self,other):
#         r = self.real + other.real
#         i = self.img + other.img
#         result = Complex(r,i)
#         return result

#     def __mul__(self,other):
#         r = self.real * other.real - self.img * other.img
#         i = self.real * other.img + other.real * self.img
#         result = Complex(r,i)
#         return result

#     def conjugate(self):
#         r = self.real**2 + self.img**2
#         i = 0
#         result = Complex(r,i)
#         return result

# c1 = Complex(2,-3)
# c2 = Complex(-1,5)
# print(c1+c2)
# print(c1*c2)
# print(c1.conjugate())


# class Library:
#     def __init__(self,members={},books={},amanati={}):
#         self.members = members
#         self.books = books
#         self.amanati = amanati

#     def addbook(self,id,name):
#         self.books[id] = name

#     def addmember(self,id,name):
#         self.members[id] = name

#     def get(self,member_id,book_id):
#         self.amanati[member_id] = self.amanati.get(member_id,[])
#         self.amanati[member_id].append(book_id)

#     def List(self,member_id):
#         return member_id

# x = Library()

# while True:

#     a = input().split()

#     if a[0] == 'addBook':
#         x.addbook(a[1],a[2])
        
#     if a[0] == 'addMember':
#         x.addmember(a[1],a[2])

#     if a[0] == 'get':
#         x.get(a[1],a[2])

#     if a[0] == 'List':
#         w = a[1]
#         break


# for i in x.amanati[w]:
#     print(i,x.books[i])

class Students:
    def __init__(self,Id,Family,Birthday='1998/1/1',Name):
        self.Name = Name
        self.Family = Family
        self.Id = Id
        self.Birthday = Birthday
        


class Courses:
    def __init__(self,Name,Unit_Number,Id ,Teacher):
        self.Name = Name
        self.Unit_Number = Unit_Number
        self.Id = Id
        self.Teacher = Teacher


a = input().split()
if a[0] == 'Register':
    x1 = Students(a[1],a[2])

