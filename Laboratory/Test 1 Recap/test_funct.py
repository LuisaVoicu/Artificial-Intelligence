def test(a):
    a.add(64)

def test1(a):
    a=1



class Clasa:
    varsta=24
    def __init__(self,nume):
        self.nume=nume
    def fct(self):
        print("ma numesc {}".format(self.nume))


# a=[4,2,3]
# a={"luisa":1,"voicu":2}
a={1,2,3,4}
print(a)
test(a)
print(a)

b=2
print(b)
test1(b)
print(b)

a=Clasa("luisa")
Clasa.fct(a)
a.fct()