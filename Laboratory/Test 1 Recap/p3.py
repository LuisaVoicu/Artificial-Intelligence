# 3. Se da clasa Universitate. Are definite numele, numarul maxim de facultati, anul infiintarii. Facultatea are definite
# nume, anul infiintarii, si o lista de angajati. Clasa angajat are definit nume, prenume, profesie si salar. 

# a. Creati 2 facultati. Angajati in cadrul fiecarei facultati 3 pers. Ulterior, afisati tot personalul unei facultati
# b. O pers demisioneaza
# c. Calculati suma totala a salariilor din Universitate

class Universitate:
    def __init__(self,nume,maxFac,an):
        self.nume=nume
        self.maxFac=maxFac
        self.an=an
        self.facultati=[]
    def adauga_facultate(self,facultate):
        # print(numeFac,anFac)
        self.facultati.append(facultate)
    
    def calculeaza_salarii(self):
        suma = 0
        something=[]
        for f in self.facultati:
            suma += sum([a.salariu for a in f.angajati])
        return suma
    
class Facultate(Universitate):
    def __init__(self,uni,numeFac,anFac):
        self.numeFac=numeFac
        self.anFac=anFac
        self.angajati=[]

    def angajeaza(self,angajat):
        self.angajati.append(angajat)

    def demisioneaza(self,angajat):
        self.angajati.remove(angajat)

    def __str__(self):
        string=self.numeFac+" "+str(self.anFac)+"\nangajati:\n"
        for a in self.angajati:
            string += str(a)
        return string

class Angajat:
    def __init__(self,nume,prenume,profestie,salariu):
        self.nume=nume
        self.prenume=prenume
        self.profesie=profestie
        self.salariu=salariu
    def __str__(self):
        string = self.nume+" "+self.prenume+" "+self.profesie+" "+str(self.salariu)+"\n"
        return string

    
uni = Universitate("utcn",20,1900)
uni.adauga_facultate(Facultate(uni,"ac",1980))
uni.adauga_facultate(Facultate(uni,"etti",1989))

a1 = Angajat("popescu","ion","profesor",20000)
a2 = Angajat("pop","daniela","profesor",20000)
a3 = Angajat("avram","maria","instalator",10000)
a4 = Angajat("abc","def","instalator",10000)
a5 = Angajat("ghi","jkl","profesor",10000)
a6 = Angajat("mno","pqr","profesor",10000)
uni.facultati[0].angajeaza(a1)
uni.facultati[0].angajeaza(a2)
uni.facultati[0].angajeaza(a3)
uni.facultati[1].angajeaza(a4)
uni.facultati[1].angajeaza(a5)
uni.facultati[1].angajeaza(a6)

print(uni.facultati[0])
print(uni.facultati[1])

uni.facultati[0].demisioneaza(a1)

print("va demisiona",a1)
print(uni.facultati[0])


print("------------")
print("total salarii", uni.calculeaza_salarii())


