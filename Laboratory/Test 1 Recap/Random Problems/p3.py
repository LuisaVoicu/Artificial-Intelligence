# 3. Se da clasa Universitate. Are definite numele, numarul maxim de facultati, anul infiintarii. Facultatea are definite
# nume, anul infiintarii, si o lista de angajati. Clasa angajat are definit nume, prenume, profesie si salar. 
# 
# a. Creati 2 facultati. Angajati in cadrul fiecarei facultati 3 pers. Ulterior, afisati tot personalul unei facultati
# b. O pers demisioneaza
# c. Calculati suma totala a salariilor din Universitate


class Universitate:
    __max_fac = 2
    def __init__(self,nume,an):
        self.nume = nume
        self.an = an
        self.facultati = set()
    def adauga_faculta(self,faculta):
        self.facultati.add(faculta)
        if len(self.facultati) > self.__max_fac:
            self.facultati.remove(faculta)
            print(f'#### nr max de facultati, nu se poate adauga {faculta} ####')
    
    def calculeaza_salar(self):
        
        suma=0

        for f in self.facultati:
            suma +=  sum(a.salar for a in f.angajati)
            
        
        return suma


    def __str__(self):
        string = self.nume + " " +str(self.an) +"\n"
        string += "".join([str(i) for i in self.facultati])
        return string

    
class Facultate:
    def __init__(self,nume,an):
        self.nume = nume
        self.an = an
        self.angajati = set()
    
    def angajeaza(self, angajat):
        self.angajati.add(angajat)

    def demisioneaza(self,angajat):
        if (angajat in self.angajati) == False :
            print(f' #### {angajat} nu lucreaza la {self.nume}, deci nu poate demisiona ###')
        else:
            self.angajati.remove(angajat)
    

    def __str__(self):
        string = self.nume+" "+str(self.an)+"\n"
        string += "".join([str(a) for a in self.angajati])
        return string

class Angajat:
    
    def __init__(self,nume,prenume,profesie,salar):
        self.nume=nume
        self.prenume=prenume
        self.profesie=profesie
        self.salar=salar
    
    def __str__(self):
        string = self.nume+" "+self.prenume+" "+self.profesie+" "+str(self.salar)+"\n"
        return string



if __name__=="__main__":
    u = Universitate("utcn",1213)
    f1 = Facultate("etti",1221)
    f2 = Facultate("ac",1232)
    u.adauga_faculta(f1)
    u.adauga_faculta(f2)

    a1 = Angajat("a","b","c",123)
    a2 = Angajat("d","e","f",124)
    a3 = Angajat("g","h","i",125)
    a4 = Angajat("i","j","k",232)

    f1.angajeaza(a1)
    f1.angajeaza(a2)
    f2.angajeaza(a3)
    f2.angajeaza(a4)

    print(u)

    f1.demisioneaza(a1)
    f1.demisioneaza(a1)

    print("###")
    print(u)

    print(u.calculeaza_salar())