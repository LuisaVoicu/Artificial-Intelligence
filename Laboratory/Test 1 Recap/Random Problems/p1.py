# 1. Se da o lista de tuple, fiecare tupla continand un numar n de stringuri. Gasiti tupla in care lungimea 
# stringurilor sa fie cea mai mare. Ulterior, extrageti ultimul string din tupla si returnati un string continand
# concatenarea de 3 ori a jumatatii stangi de caractere ale stringului.


def rezolva(lista,n):

    maxim = max(lista, key = lambda lista: sum(len(i) for i in lista))
    print("this is maxim",maxim)
    something = maxim[-1]
    print( something[:len(something)//2]*3)

lista = [("ab", "123456", "lok"), ("et", "rapso9aaaaaaaaaaa18!", "incomprehensibil"), ("12!", "vestejel")]
rezolva(lista,3)