def ex1(lista):
    mean = sum(lista)/len(lista)
    return mean

def ex2(lista):
    positive=[l for l in lista if l>=0]
    negative=[l for l in lista if l<0]
    print(positive)
    print(negative)

def ex3(lista):
    return sum(lista[:-2])

def ex4(lista):
    return [e for i,e in enumerate(lista) if i%2!=0]

def ex5(lista):
    minim=lista[0]
    for i in lista:
        if i < minim:
            minim = i
    print(minim)
    
        

if __name__=="__main__":
    lista = [11,-2,3,-41,5]
    print(ex1(lista))
    ex2(lista)
    print(ex3(lista))
    print(ex4(lista))
    ex5(lista)

