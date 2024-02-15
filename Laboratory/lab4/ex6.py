class Complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def add(compl1, compl2):
        new_a=compl1.a + compl2.a
        new_b=compl1.b + compl2.b
        return Complex(new_a,new_b)
    
    def difference(compl1,compl2):
        new_a=compl1.a - compl2.a
        new_b=compl1.b - compl2.b
        return Complex(new_a,new_b)
    
    def product(compl1, compl2):
        new_a=compl1.a*compl2.a - compl1.b*compl2.b
        new_b=compl1.a*compl2.b + compl1.b*compl2.a
        return Complex(new_a,new_b)
    
    def print_complex(self):
        print(self.a,"+i",self.b)


no1=Complex(3,2)
no2=Complex(5,6)
add=Complex.add(no1,no2)
sub=Complex.difference(no1,no2)
prod=Complex.product(no1,no2)
add.print_complex()
sub.print_complex()
prod.print_complex()