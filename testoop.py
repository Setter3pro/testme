# class Student:
#     def __init__(self,name,id,mark):
#         self.id = id
#         self.mark = mark
#         self.name = name.upper()

#     def show(self):
#         return f"Hello baby {self.name}"




class Complex:
    def __init__(self,r,img):
        self.real = r
        self.img = img
        
    def add(self,other):
        r = self.real + other.real
        i = self.img + other.img
        result = Complex(r,i)
        return result

    def __str__(self):
        if self.img > 0:
            return f'{self.real} + {self.img}i'
        if self.img < 0:
            return f'{self.real} - {abs(self.img)}i'
        if self.img == 0:
            return f'{self.real}'

    def __add__(self,other):
        r = self.real + other.real
        i = self.img + other.img
        result = Complex(r,i)
        return result

    def __eq__(self, other):
        if self.real == other.real and self.img == other.img:
            return True
        else:
            return False

    def __sub__(self,other):
        r = self.real - other.real
        i = self.img - other.img
        result = Complex(r,i)
        return result

    def __mul__(self,other):
        r = self.real * other.real
        i = self.img * other.img
        result = Complex(r,i)
        return result

    def __truediv__(self,other):
        r = self.real / other.real
        i = self.img / other.img
        result = Complex(r,i)
        return result
    


# c1 = Complex(1,8)
# c1.real = 10

# c2 = Complex(2,7)

# print(c1 / c2)

class Student:
    def __init__(self,fname,lname,id,field,courses = []):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.field = field
        self.courses = courses

    def __str__(self):
        return f'{self.lname} {self.id}'

    def add_courses(self,course):
        self.courses.append(course)


# s1 = Student('Sina','Beigi',98673417,'Mechanics',['Programme'])

# print(s1.courses)

# s1.add_courses('Electricite')

# print(s1.courses)



class c(Complex):
    def __init__(self, r, img,absolute):
        super().__init__(r, img)
        self.absolute = absolute

x = c(4,9,10)
print(x)
print(x.absolute)