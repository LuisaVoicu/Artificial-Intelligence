def rezolvare(fname1,fname2):
    f1 = open(fname1,"r")
    f2 = open(fname2,"r")

    text1 = f1.readline()
    text2 = f2.readline()
    lista = []
    while text1 != '' and text2 != '':
        lista.append(text1)
        lista.append(text2)
        text1 = f1.readline()
        text2 = f2.readline()

    while text1!= '':
        lista.append(text1)
        text1 = f1.readline()
    
    while text2!='':
        lista.append(text2)
        text2 = f2.readline()

    f1.close()
    f2.close()
    return lista

def pune_in_fisier(lista, fname):
    f = open(fname,"r+")
    f.writelines(lista)
    f.close()

def rezolva_frecv(fname):
    content = ""
    with open(fname,"r") as f:
        content = f.read()
    
    dir_fr = dict()
    for i in content:
        val = 1
        if i in dir_fr:
            val = dir_fr[i] + 1
        dir_fr.update({i:val})
    
    print(dir_fr)
        


pune_in_fisier(rezolvare("p21.txt","p22.txt"),"p23.txt")
test = input()
rezolva_frecv(test)

