

class complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
                    
    def __str__(self):
        if self.img > 0:
            self.img = abs(self.img)
            return (f"{self.real} + {self.img}i")
        if self.img <0:
            self.img = abs(self.img)
            return (f"{self.real} - {self.img}i")
        if self.img == 0:
            return (f"{self.real}")

    def add(self,ect):
        main = self.real + ect.real
        minor = self.img + ect.img
        C = complex(main,minor)
        return C
    def __add__(self,ect):
        r = self.real + ect.real
        i = self.img + ect.img
        C = complex(r,i)
        return C
    
C1 = complex(-1,5)

C2 = complex(4,-1)

C3 = C1 + C2

print(C3.real)

print(C1)
