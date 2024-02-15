def ex1(dict,lista):
    price = sum(dict[prod]*price for (prod,price) in lista)
    print(price)

def ex2(lista):
    my_set=set()
    print([i for (i,p) in lista])
    print("set:",my_set)
  
    [my_set.add(i) for (i,p) in lista]
    print("set:",my_set)

def ex3(nb):
    print([i if int(nb)%2 == 0 else i*i for i in range(int(nb))])

def ex4(string,nb):
    nb=int(nb)
    my_dict = dict()

    [my_dict.update({i:string[i]}) for i in range(min(nb,len(string)))]
    print(my_dict)


def ex5(string):
    lista = list(string)
    # lista_noua = [chr(ord(i))+1 for i in lista]
    lista=[chr(ord(i)+1) for i in lista]
    string_nou = "".join(lista)
    print(string_nou)

def ex6(namef1,namef2):
    with open(namef1,"r") as f:
        text = f.read()
    
    f = open(namef2,"r+")
    lista = text.split("\n")
    f.write(text.upper())
    # for i in lista:
    #     f.writelines(i.upper())

    f.close()
    print(lista)
    
if __name__=="__main__":
    price = {'apples':10,'milk':12,'bread':5}
    lista = [('apples',2),('milk',2)]
    ex1(price,lista)
    print("---ex2")
    friends=[("andrew",10),("george",20),("andrew",5),("ann",10)]
    ex2(friends)
    # print("--ex3:")
    # ex3(input())
    # print("--ex4:")
    # ex4(input(),input())
    print("--ex5:")
    ex5("abcdef ghi")

    print("--ex5:")
    ex6("a.txt","b.txt")